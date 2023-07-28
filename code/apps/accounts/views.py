from datetime import date, timedelta
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import UsuarioForm
from .permissions import set_permission
from .models import Usuario, SolicitacaoCadastro
from django.contrib import messages
from financas.models import Saida, Entradas
from igreja.models import Dizimo, OfertaCulto, Membro, Igreja

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


@login_required
def home(request):
    # Filtre os valores dos últimos 5 meses a partir do mês atual da igreja do usuário
    usuario = obterUsuario(request)

    data_atual = date.today()

    data = data_atual - timedelta(days=data_atual.day - 1)

    data_inicio = data - timedelta(days=30 * 4)  # 4 meses atrás
    datas = [data_inicio + timedelta(days=30 * i) for i in range(5)]

    total_dizimos = []
    variacao_dizimos = []
    total_ofertas = []
    variacao_ofertas = []
    total_saidas = []
    variacao_saidas = []
    total = []
    variacao_total = []
    membros = Membro.objects.filter(igreja=usuario.igreja)[:5]
    igrejas = Igreja.objects.all()[:5]

    for i, data in enumerate(datas):
        proximo_mes = data.replace(day=28) + timedelta(days=4)
        dizimos = Dizimo.objects.filter(
            data_culto__gte=data, data_culto__lt=proximo_mes, igreja=usuario.igreja).values_list('valor', flat=True)
        ofertas = OfertaCulto.objects.filter(
            data_culto__gte=data, data_culto__lt=proximo_mes, igreja=usuario.igreja).values_list('valor_oferta', flat=True)
        saidas = Saida.objects.filter(
            data__gte=data, data__lt=proximo_mes, igreja=usuario.igreja).values_list('valor', flat=True)

        total_dizimo = sum(dizimos)
        total_oferta = sum(ofertas)
        total_saida = sum(saidas)
        total_atual = total_dizimo + total_oferta - total_saida

        total_dizimos.append(total_dizimo)
        total_ofertas.append(total_oferta)
        total_saidas.append(total_saida)
        total.append(total_atual)

        if i > 0:
            variacao_dizimo = (
                (total_dizimo - total_dizimos[i-1]) / total_dizimos[i-1] if total_dizimos[i-1] > 0 else 1) * 100
            variacao_oferta = (
                (total_oferta - total_ofertas[i-1]) / total_ofertas[i-1] if total_ofertas[i-1] > 0 else 1) * 100
            variacao_saida = (
                (total_saida - total_saidas[i-1]) / total_saidas[i-1] if total_saidas[i-1] > 0 else 1) * 100
            variacao = (
                (total_atual - total[i-1]) / total[i-1] if total[i-1] > 0 else 1) * 100
        else:
            variacao_dizimo = 0
            variacao_oferta = 0
            variacao_saida = 0
            variacao = 0

        variacao_dizimos.append(variacao_dizimo)
        variacao_ofertas.append(variacao_oferta)
        variacao_saidas.append(variacao_saida)
        variacao_total.append(variacao)
    print(['{:,.2f}'.format(t).replace(',', '.') for t in total])

    context = {
        'igrejas': igrejas,
        'usuario': usuario,
        'igreja': usuario.igreja,
        'usuario_nome': usuario.nome.split()[0],
        # Formatação com duas casas decimais e separador de milhares
        'total_dizimos': '{:,.2f}'.format(total_dizimos[-1]),
        'variacao_dizimos': variacao_dizimos[-1],
        # Formatação com duas casas decimais e separador de milhares
        'total_ofertas': '{:,.2f}'.format(total_ofertas[-1]),
        'variacao_ofertas': variacao_ofertas[-1],
        # Formatação com duas casas decimais e separador de milhares
        'total_saidas': '{:,.2f}'.format(total_saidas[-1]),
        'variacao_saidas': variacao_saidas[-1],
        # Formatação com duas casas decimais e separador de milhares
        'total': '{:,.2f}'.format(total[-1]),
        'variacao_total': variacao_total[-1],
        'membros': membros,
        'mes': [data.strftime('%B %Y') for data in datas],
        'total_meses_data': ['{:,.2f}'.format(t).replace(',', '.') for t in total],
        'total_meses_color': ['green' if t > 0 else 'red' for t in total],
        'variacao_meses': variacao_total,
        'data_atual': data_atual
    }

    return render(request, "home/home.html", context)


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
                usuario=usuario,
            )

            messages.success(
                request, 'Solicitação de cadastro enviada com sucesso! Aguarde a aprovação de um administrador.')

            return HttpResponseRedirect(reverse('acompanhar_cadastro', args=[solicitacao.id]))

    form_solicitacao = UsuarioForm()

    context = {
        
        'form': form_solicitacao
    }
    return render(request, 'solicitacoes/cadastro.html', context)


def acompanhar_cadastro(request, solicitacao_id):
    """
    View para acompanhamento de cadastro.

    Esta view pode ser acessada por qualquer usuário.
    """
    solicitacao = SolicitacaoCadastro.objects.get(id=solicitacao_id)
    context = {
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
    usuario = obterUsuario(request)
    
    pendentes = SolicitacaoCadastro.objects.filter(situacao="Pendente")
    aprovadas = SolicitacaoCadastro.objects.filter(situacao="Aprovada")
    negadas = SolicitacaoCadastro.objects.filter(situacao="Negada")

    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'pendentes': pendentes,
        'aprovadas': aprovadas,
        'negadas': negadas
    }
    return render(request, 'solicitacoes/listar.html', context)


@login_required
@permission_required('accounts.tesoureiro_sede')
def detalhar_cadastro(request, solicitacao_id):
    user = obterUsuario(request)
    """
    View para detalhar cadastros.

    Esta view só pode ser acessada por usuários autenticados e com a permissão 'tesoureiro_sede'.
    """
    solicitacao = SolicitacaoCadastro.objects.get(id=solicitacao_id)
    context = {
        'solicitacao': solicitacao,
        'usuario': user,
        'igreja': user.igreja, 
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
