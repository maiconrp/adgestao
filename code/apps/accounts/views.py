from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, reverse
from .forms import UsuarioForm
from .permissions import set_permission
from .models import Usuario, SolicitacaoCadastro
from django.contrib import messages

@login_required
def obterUsuario(request):
    user = False
    if Usuario.is_authenticated:
        try: 
            user = request.user.id
            user = Usuario.objects.get(id=user)
        except: 
            pass
    return user

def home(request):
    return render(request, "home.html")

def solicitar_cadastro(request):
    """
    View para solicitação de cadastro.

    Esta view pode ser acessada por qualquer usuário.
    """    
    if request.method == "POST":
        form_solicitacao = UsuarioForm(request.POST)
        
        if form_solicitacao.is_valid():
            usuario = form_solicitacao.save(commit=False)
            
            usuario.is_active = False
            usuario.save()
            
            usuario = set_permission(usuario)
                        
            solicitacao, _ = SolicitacaoCadastro.objects.get_or_create(
                usuario = usuario,
            )
            
            messages.success(request, 'Solicitação de cadastro enviada com sucesso! Aguarde a aprovação de um administrador.')
            
            
            return HttpResponseRedirect(reverse('acompanhar_cadastro', args=[solicitacao.id]))
    
    form_solicitacao = UsuarioForm()
        
    context={
        'form': form_solicitacao
    }
    return render(request, 'solicitacoes/cadastro.html', context)

    
    
def acompanhar_cadastro(request, solicitacao_id):
    """
    View para acompanhamento de cadastro.

    Esta view pode ser acessada por qualquer usuário.
    """
    solicitacao = SolicitacaoCadastro.objects.get(id=solicitacao_id)
    context={
        'solicitacao': solicitacao
    }
    print(solicitacao.situacao)
    return render(request, 'solicitacoes/acompanhar.html', context)


@login_required
@permission_required('accounts.tesoureiro_sede')
def listar_cadastros(request):
    """
    View para listar cadastros.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    pendentes = SolicitacaoCadastro.objects.filter(situacao = "Pendente")
    aprovadas = SolicitacaoCadastro.objects.filter(situacao = "Aprovada")
    negadas = SolicitacaoCadastro.objects.filter(situacao = "Negada")

    context = {
        'pendentes': pendentes,
        'aprovadas': aprovadas,
        'negadas': negadas
    }
    return render(request, 'solicitacoes/listar.html', context)

@login_required
@permission_required('accounts.tesoureiro_sede')
def detalhar_cadastro(request, solicitacao_id):
    """
    View para detalhar cadastros.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    solicitacao = SolicitacaoCadastro.objects.get(id=solicitacao_id)
    context = {
        'solicitacao': solicitacao,
    }

    return render(request, 'solicitacoes/detalhar.html', context)

@login_required
@permission_required('accounts.tesoureiro_sede')
def responder_cadastro(request, solicitacao_id, acao):
    """
    View para responder cadastro.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    solicitacao = SolicitacaoCadastro.objects.get(id=solicitacao_id)
    
    if acao == 'autorizar':
        solicitacao.usuario.is_active = True
        solicitacao.situacao = 'Aprovada'
        solicitacao.usuario.save()
        solicitacao.save()
        messages.success(request, 'Cadastro autorizado com sucesso!')

    elif acao == 'negar':
        solicitacao.usuario.is_active = False
        solicitacao.situacao = 'Negada'
        solicitacao.usuario.save()
        solicitacao.save()
        messages.error(request, 'Cadastro negado com sucesso!')
    
    else:
        raise Exception('Açao deve ser negar ou autorizar')
   
    return HttpResponseRedirect(reverse('listar_cadastros'))
