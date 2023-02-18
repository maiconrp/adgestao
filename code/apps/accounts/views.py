from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render

def solicitar_cadastro(request):
    """
    View para solicitação de cadastro.

    Esta view pode ser acessada por qualquer usuário.
    """
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
