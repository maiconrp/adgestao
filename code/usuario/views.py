from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_permission
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SolicitacaoCadastroForm
from .models import Pastor, Tesoureiro, TesoureiroSede, SolicitacaoCadastro

def solicitar_cadastro(request):
    if request.method == "POST":
        form_solicitacao = SolicitacaoCadastroForm(request.POST)
        
        if form_solicitacao.is_valid():
            form_solicitacao.save(commit=False)
            form_solicitacao.situacao = "Pendente"
            form_solicitacao.save()
            
            context={'form_solicitacao': form_solicitacao}
            
            return HttpResponseRedirect("acompanhar/cadastro")
    else:
        form_solicitacao = SolicitacaoCadastroForm()
        
    return render(request, 'solicitacoes/solicitar.html', {'form_solicitacao': form_solicitacao})


def acompanhar_cadastro(request):
    
    solicitacao = None
    
    if request.method == "POST":
        
        cpf = request.POST.get("cpf")
        
        try:
            solicitacao = SolicitacaoCadastro.objects.get(cpf=cpf)
            situacao = solicitacao.situacao
            
            if situacao == 'Aprovado':
                return HttpResponseRedirect('accounts/login')
            
            else:
                mensagem = 'Seu cadastro ainda está em análise. Aguarde a aprovação do Tesoureiro Sede.'
            
        except SolicitacaoCadastro.DoesNotExist:
            mensagem = 'Não foi encontrada nenhuma solicitação de cadastro com o CPF informado.'

        context = {
            'mensagem': mensagem,
            'solicitacao': solicitacao
        }
        
        return render(request, 'solicitacao/acompanhar.html', context)
        
        
    else:
        return render(request, 'solicitacao/acompanhar.html', {})


def autorizar_solicitacao(request, cpf):
    solicitacao = get_object_or_404(SolicitacaoCadastro, cpf=cpf)
    solicitacao.situacao = 'Autorizado' # Define a situação como autorizado
    solicitacao.save()

    # Cria um objeto do usuário correspondente e salva-o no banco de dados
    if solicitacao.funcao == 'P':
        pastor = Pastor.objects.create_user(
            username=solicitacao.username,
            email=solicitacao.email,
            password=solicitacao.password,
            cpf=solicitacao.cpf,
            telefone=solicitacao.telefone,
            igreja=solicitacao.igreja
        )
        pastor.save()
    elif solicitacao.funcao == 'T':
        tesoureiro = Tesoureiro.objects.create_user(
            username=solicitacao.username,
            email=solicitacao.email,
            password=solicitacao.password,
            cpf=solicitacao.cpf,
            telefone=solicitacao.telefone,
            igreja=solicitacao.igreja
        )
        tesoureiro.save()
    else:
        tesoureiro_sede = TesoureiroSede.objects.create_user(
            username=solicitacao.username,
            email=solicitacao.email,
            password=solicitacao.password,
            cpf=solicitacao.cpf,
            telefone=solicitacao.telefone,
            igreja=solicitacao.igreja
        )
        tesoureiro_sede.save()
        assign_role(tesoureiro_sede, TesoureiroSede)

    return HttpResponseRedirect('solicitacoes/')


def negar_solicitacao(request, cpf):
    solicitacao = get_object_or_404(SolicitacaoCadastro, cpf=cpf)
    solicitacao.situacao = 'Negado' # Define a situação como negado
    solicitacao.save()

    return HttpResponseRedirect('solicitacoes/')


