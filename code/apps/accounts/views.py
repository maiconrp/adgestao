from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from . forms import UsuarioForm
from .permissions import set_permission
from .models import Usuario, SolicitacaoCadastro


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
            
            usuario = set_permission(usuario)
            
            usuario.save()
            
            solicitacao, _ = SolicitacaoCadastro.objects.get_or_create(
                usuario = usuario,
            )   
            
            context={
                'form_solicitacao': form_solicitacao
            }
            
            return HttpResponseRedirect("cadastro/acompanhar")
    else:
        form_solicitacao = UsuarioForm()
        
        context={
                'form_solicitacao': form_solicitacao
            }
        
        return render(request, 'accounts/register.html', context)


def solicitar_cadastro(request):
    
    return HttpResponse("Cadastro de Usuários")

def acompanhar_cadastro(request):
    """
    View para acompanhamento de cadastro.

    Esta view pode ser acessada por qualquer usuário.
    """
    return HttpResponse("Acompanhar Cadastro")

@login_required
@permission_required('accounts.tesoureiro_sede')
def listar_cadastros(request):
    """
    View para listar cadastros.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    return HttpResponse("Listar Cadastro")

@login_required
@permission_required('accounts.tesoureiro_sede')
def detalhar_cadastros(request):
    """
    View para detalhar cadastros.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    return HttpResponse("Detalhar Cadastro")

@login_required
@permission_required('accounts.tesoureiro_sede')
def responder_cadastro(request):
    """
    View para responder cadastro.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    return HttpResponse("Responder Cadastro")
