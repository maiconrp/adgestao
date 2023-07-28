from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.pagesizes import A4
from functools import partial
import calendar
from datetime import datetime
import io
import qrcode
import os
from accounts.views import obterUsuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from igreja.forms import DizimoForm, OfertaForm, DizimoFormWithUser
from igreja.models import Dizimo, Igreja, OfertaCulto
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from decimal import Decimal

from .forms import SaidaForm, RelatorioGeralForm
from .models import Entradas, RelatorioGeral, RelatorioMensal, Saida

pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))


def atualizar_saldo(request, user):
    igreja = user.igreja

    saidas = Saida.objects.filter(igreja=user.igreja)

    total_saidas = Decimal('0')  # Inicializa como um objeto Decimal

    for saida in saidas:
        total_saidas += saida.valor  # Utiliza a sintaxe de soma para Decimal

    entradas = OfertaCulto.objects.filter(igreja=user.igreja)

    total_entradas = Decimal('0')  # Inicializa como um objeto Decimal

    for entrada in entradas:
        total_entradas += entrada.total  # Utiliza a sintaxe de soma para Decimal

    saldo = total_entradas - total_saidas

    # Atualizando registro de saldo no model de Igreja
    igreja.saldo = saldo
    print('saldo atualizado')
    igreja.save()


def atualizar_registro_model(request, financa, user):
    usuario = obterUsuario(request)
    # Setando objetos
    try:
        relatorio_geral = RelatorioGeral.objects.get(status='Ativo')

    except:
        relatorio_geral = None

    try:
        usuario = obterUsuario(request)
        igreja = usuario.igreja
        relatorio_mensal = RelatorioMensal.objects.get(
            igreja=igreja,
            status='Ativo'
        )

    except:
        relatorio_mensal = None

    # Verifica se um relatório de oferta com o mesmo dia e tipo de culto já foi criado
    if relatorio_geral is not None and relatorio_mensal is not None:

        if financa == 'saida':
            atualizar_saldo(request, usuario)
            # Atualizando registros no model de RealatórioGeral
            relatorio_geral.saidas_sede = relatorio_geral.calc_saidas_sede
            relatorio_geral.saidas_locais = relatorio_geral.calc_saidas_locais
            relatorio_geral.saldo = relatorio_geral.calc_saldo

            relatorio_geral.save()

            # Atualizando registros no model de RealatórioMensal
            relatorio_mensal.total_saidas = relatorio_mensal.calc_saidas
            relatorio_mensal.saldo = relatorio_mensal.calc_saldo
            relatorio_mensal.pagamento_obreiro = relatorio_mensal.calc_pagamento_obreiro
            relatorio_mensal.fundo_convencional = relatorio_mensal.calc_fundo_convencional
            relatorio_mensal.missoes_sede = relatorio_mensal.calc_missoes_sede

            relatorio_mensal.save()

        elif financa == 'entrada e saida':
            # Atualizando registros no model de RealatórioGeral
            # Saídas
            relatorio_geral.saidas_sede = relatorio_geral.calc_saidas_sede
            relatorio_geral.saidas_locais = relatorio_geral.calc_saidas_locais
            relatorio_geral.saldo = relatorio_geral.calc_saldo

            # Entradas
            relatorio_geral.entradas_sede = relatorio_geral.calc_entradas_sede
            relatorio_geral.entradas_locais = relatorio_geral.calc_entradas_locais
            relatorio_geral.saldo = relatorio_geral.calc_saldo

            relatorio_geral.save()

            # Atualizando registros no model de RealatórioMensal
            # Saídas
            relatorio_mensal.pagamento_obreiro = relatorio_mensal.calc_pagamento_obreiro
            relatorio_mensal.fundo_convencional = relatorio_mensal.calc_fundo_convencional
            relatorio_mensal.missoes_sede = relatorio_mensal.calc_missoes_sede
            relatorio_mensal.total_saidas = relatorio_mensal.calc_saidas
            relatorio_mensal.saldo = relatorio_mensal.calc_saldo

            # Entradas
            relatorio_mensal.total_entradas = relatorio_mensal.calc_total_entradas
            relatorio_mensal.pagamento_obreiro = relatorio_mensal.calc_pagamento_obreiro
            relatorio_mensal.fundo_convencional = relatorio_mensal.calc_fundo_convencional
            relatorio_mensal.missoes_sede = relatorio_mensal.calc_missoes_sede
            relatorio_mensal.saldo = relatorio_mensal.calc_saldo


            relatorio_mensal.save()

        else:
            atualizar_saldo(request, usuario)

            # Atualizando registros no model de RealatórioGeral
            relatorio_geral.entradas_sede = relatorio_geral.calc_entradas_sede
            relatorio_geral.entradas_locais = relatorio_geral.calc_entradas_locais
            relatorio_geral.saldo = relatorio_geral.calc_saldo

            relatorio_geral.save()

            # Atualizando registros no model de RealatórioMensal
            relatorio_mensal.total_entradas = relatorio_mensal.calc_total_entradas
            relatorio_mensal.saldo = relatorio_mensal.calc_saldo
            relatorio_mensal.pagamento_obreiro = relatorio_mensal.calc_pagamento_obreiro
            relatorio_mensal.fundo_convencional = relatorio_mensal.calc_fundo_convencional
            relatorio_mensal.missoes_sede = relatorio_mensal.calc_missoes_sede

            relatorio_mensal.save()

    else:

        messages.success(request, 'Crie um relatório mensal e/ou geral!')
        return HttpResponseRedirect(reverse('listar_relatorios_mensais'))


# @login_required
# @permission_required('accounts.tesoureiro')
def adicionar_saida(request):
    user = obterUsuario(request)
    if request.method == 'POST':

        form = SaidaForm(request.POST)
        if form.is_valid():
            form.instance.igreja = user.igreja
            saida = form.save()
            saida.save()

            atualizar_registro_model(request, financa='saida', user=user)

            messages.success(request, 'Saída adicionada com sucesso!')

            context = {
                'form': form,
            }
            return HttpResponseRedirect(reverse('listar_saidas'))
    else:
        form = SaidaForm()

    context = {
        'usuario': user,
        'igreja': user.igreja,
        'form': form,
    }

    return render(request, 'financas/saidas/adicionar.html', context)


# @login_required
# @permission_required('accounts.tesoureiro')
def editar_saida(request, saida_id):

    user = obterUsuario(request)
    saida = Saida.objects.get(id=saida_id)

    if request.method == "POST":
        form = SaidaForm(request.POST, instance=saida)

        if form.is_valid():
            form.save()

            atualizar_registro_model(request, financa='saida', user=user)

            return HttpResponseRedirect(reverse('detalhar_saida', args=[saida.id]))
    else:
        form = SaidaForm(instance=saida)

    context = {
        'usuario': user,
        'igreja': user.igreja,
        'form': form,
    }
    return render(request, 'financas/saidas/editar.html', context)


# @login_required
# @permission_required('accounts.tesoureiro')
def excluir_saida(request, saida_id):
    user = obterUsuario(request)

    saida = Saida.objects.get(id=saida_id)
    saida.delete()

    atualizar_registro_model(request, financa='saida', user=user)

    return HttpResponseRedirect(reverse('listar_saidas'))


# @login_required
# @permission_required('accounts.tesoureiro')
def listar_saidas(request):
    usuario = obterUsuario(request)
    saidas = Saida.objects.filter(igreja=usuario.igreja)
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'saidas': saidas
    }
    return render(request, 'financas/saidas/listar.html', context)


# @login_required
# @permission_required('accounts.tesoureiro')
def detalhar_saida(request, saida_id):

    usuario = obterUsuario(request)
    saida = Saida.objects.get(id=saida_id)
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'saida': saida
    }
    return render(request, 'financas/saidas/detalhar.html', context)

# @login_required
# @permission_required('accounts.tesoureiro')


def adicionar_dizimo(request):
    user = obterUsuario(request)
    print(user.igreja)

    entrada = get_object_or_404(Entradas, igreja=user.igreja)

    if request.method == 'POST':
        form = DizimoFormWithUser(request.POST, usuario=user)

        if form.is_valid():
            form.instance.igreja = user.igreja
            dizimo = form.save()
            dizimo.save()
            messages.success(request, 'Dízimo adicionada com sucesso!')

            entrada.dizimos.add(dizimo)

            try:
                oferta = OfertaCulto.objects.get(
                    Q(data_culto=dizimo.data_culto) & Q(igreja=dizimo.igreja)
                )
            except:
                oferta = None

            # Verifica se um relatório de oferta com o mesmo dia e tipo de culto já foi criado
            if oferta:
                print('oferta existe')
                # Chama a função que calcula a soma dos valores dos dizimos daquele culto
                valor_dizimo = calc_soma_dizimo(oferta)

                # Atribui ao atributo "valor_dizimo" o valor calculado anteriormento pela função
                oferta.valor_dizimo = valor_dizimo

                # Salva os valores dos dízimos criados após o relatório de culto
                oferta.save()

                atualizar_registro_model(request, financa='entrada', user=user)

                context = {
                    'form': form,
                }
                return HttpResponseRedirect(reverse('listar_dizimos'))

            else:
                context = {
                    'form': form,
                }
                return HttpResponseRedirect(reverse('listar_dizimos'))

    else:
        form = DizimoForm()

    context = {
        'usuario': user,
        'igreja': user.igreja,
        'form': form,
    }

    return render(request, 'financas/entradas/dizimos/adicionar.html', context)


# @login_required
# @permission_required('accounts.tesoureiro')
def editar_dizimo(request, dizimo_id):

    user = obterUsuario(request)
    dizimo = Dizimo.objects.get(id=dizimo_id)

    if request.method == "POST":
        form = DizimoForm(request.POST, instance=dizimo)

        if form.is_valid():
            form.save()

            atualizar_registro_model(request, financa='entrada', user=user)

            return HttpResponseRedirect(reverse('detalhar_dizimo', args=[dizimo.id]))
    else:
        form = DizimoForm(instance=dizimo)

    context = {
        'usuario': user,
        'igreja': user.igreja,
        'form': form,
    }
    return render(request, 'financas/entradas/dizimos/editar.html', context)


# @login_required
# @permission_required('accounts.tesoureiro')
def excluir_dizimo(request, dizimo_id):
    user = obterUsuario(request)

    dizimo = Dizimo.objects.get(id=dizimo_id)
    dizimo.delete()

    atualizar_registro_model(request, financa='entrada', user=user)

    return HttpResponseRedirect(reverse('listar_dizimos'))


# @login_required
# @permission_required('accounts.tesoureiro')
def listar_dizimos(request):
    usuario = obterUsuario(request)

    igreja = Igreja.objects.get(nome=usuario.igreja.nome)

    dizimos = igreja.dizimos.all()

    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'dizimos': dizimos
    }
    return render(request, 'financas/entradas/dizimos/listar.html', context)


@login_required
# @permission_required('accounts.tesoureiro')
def detalhar_dizimo(request, dizimo_id):

    usuario = obterUsuario(request)

    dizimo = Dizimo.objects.get(id=dizimo_id)
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'dizimo': dizimo
    }
    return render(request, 'financas/entradas/dizimos/detalhar.html', context)


# Esta função soma os valores dos dízimos de um culto, considerando o dia e tipo de culto do dízimo
def calc_soma_dizimo(oferta):
    # Busca todos os dízimos cuja data é a mesma do relatório de culto
    dizimos = Dizimo.objects.filter(
        Q(data_culto=oferta.data_culto) & Q(igreja=oferta.igreja)
    )

    # Cria a variável "valor_dizimo"
    valor_dizimo = 0

    # Loop que irá percorrer todos os objetos filtrados, contidos em 'dizimos'
    for dizimo in dizimos:

        # verifica se o dizimo em questão possui tanto a mesma data quanto o tipo de culto do relatório criado
        if dizimo.tipo_culto == oferta.tipo_culto and dizimo.data_culto == oferta.data_culto:
            valor_dizimo = valor_dizimo + dizimo.valor

    return valor_dizimo


def adicionar_oferta(request):
    user = obterUsuario(request)
    entrada, _ = Entradas.objects.get_or_create(
        igreja=user.igreja)  # (objeto, se ele existe ou não)

    if request.method == 'POST':

        form = OfertaForm(request.POST)
        if form.is_valid():

            # Atribui ao atributo 'igreja' da oferta a igreja do usuario que esta criando o relatório de oferta
            form.instance.igreja = user.igreja
            oferta = form.save()

            # Chama a função que calcula a soma dos valores dos dizimos daquele culto
            valor_dizimo = calc_soma_dizimo(oferta=oferta)

            # Atribui ao atributo "valor_dizimo" o valor calculado anteriormento pela função
            oferta.valor_dizimo = valor_dizimo

            # Salva a nova atribuição
            oferta.save()

            messages.success(request, 'Oferta adicionada com sucesso!')

            entrada.ofertas.add(oferta)

            atualizar_registro_model(request, financa='entrada', user=user)

            context = {
                'form': form,
            }
            return HttpResponseRedirect(reverse('listar_ofertas'))
    else:
        form = OfertaForm()

    context = {
        'usuario': user,
        'igreja': user.igreja,
        'form': form,
    }

    return render(request, 'financas/entradas/ofertas/adicionar.html', context)


def listar_ofertas(request):
    usuario = obterUsuario(request)

    igreja = Igreja.objects.get(nome=usuario.igreja.nome)

    ofertas = igreja.ofertas_culto.all()

    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'ofertas': ofertas
    }
    return render(request, 'financas/entradas/ofertas/listar.html', context)


def excluir_oferta(request, oferta_id):
    user = obterUsuario(request)
    oferta = OfertaCulto.objects.get(id=oferta_id)
    oferta.delete()

    atualizar_registro_model(request, financa='entrada', user=user)

    return HttpResponseRedirect(reverse('listar_ofertas'))


def detalhar_oferta(request, oferta_id):
    usuario = obterUsuario(request)

    oferta = OfertaCulto.objects.get(id=oferta_id)
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'oferta': oferta
    }
    return render(request, 'financas/entradas/ofertas/detalhar.html', context)


def editar_oferta(request, oferta_id):
    user = obterUsuario(request)
    oferta = OfertaCulto.objects.get(id=oferta_id)

    if request.method == "POST":
        form = OfertaForm(request.POST, instance=oferta)

        if form.is_valid():
            form.save()

            atualizar_registro_model(request, financa='entrada', user=user)

            return HttpResponseRedirect(reverse('detalhar_oferta', args=[oferta.id]))
    else:
        form = OfertaForm(instance=oferta)

    context = {
        'usuario': user,
        'igreja': user.igreja,
        'form': form,
    }
    return render(request, 'financas/entradas/ofertas/editar.html', context)


####################### - - - - - - RELATÓRIO MENSAL - - - - - -  ############################

def criar_novo_relatorio_mensal(request):
    user = obterUsuario(request)
    igreja = Igreja.objects.get(nome=user.igreja.nome)

    try:
        relatorios = RelatorioMensal.objects.filter(igreja=ugreja)
    except:
        relatorios = None

    if relatorios is not None:
        for relatorio in relatorios:
            if relatorio.status == 'Ativo':
                messages.error(request, 'Já existe um relatório ativo !')
                return HttpResponseRedirect(reverse('listar_relatorios_gerais'))
            break

        # obtendo a data que contém o último dia do mês
        data_atual = datetime.now()

        # Obtém o último dia do mês
        ultimo_dia = calendar.monthrange(data_atual.year, data_atual.month)[1]

        # Cria a data do último dia do mês
        data_ultimo_dia = datetime(
            data_atual.year, data_atual.month, ultimo_dia)

        # Formata a data no formato "dd/mm/aaaa"
        data_fim = data_ultimo_dia.strftime("%Y-%m-%d")

        data_criacao = datetime.now()
        data_criacao = data_criacao.strftime("%Y-%m-%d")
        relatorio_mensal = RelatorioMensal(
            igreja=igreja, data_inicio=data_criacao, data_fim=data_fim)
        relatorio_mensal.save()

        atualizar_registro_model(request, financa='entrada e saida', user=user)

        messages.success(
            request, 'Um novo Relatório Mensal foi criado com sucesso!')

        return HttpResponseRedirect(reverse('listar_relatorios_mensais'))

    else:
        # obtendo a data que contém o último dia do mês
        data_atual = datetime.now()

        # Obtém o último dia do mês
        ultimo_dia = calendar.monthrange(data_atual.year, data_atual.month)[1]

        # Cria a data do último dia do mês
        data_ultimo_dia = datetime(
            data_atual.year, data_atual.month, ultimo_dia)

        # Formata a data no formato "dd/mm/aaaa"
        data_fim = data_ultimo_dia.strftime("%Y-%m-%d")

        data_criacao = datetime.now()
        data_criacao = data_criacao.strftime("%Y-%m-%d")
        relatorio_mensal = RelatorioMensal(
            igreja=igreja, data_inicio=data_criacao, data_fim=data_fim)
        relatorio_mensal.save()

        atualizar_registro_model(request, financa='entrada e saida', user=user)

        messages.success(
            request, 'Um novo Relatório Mensal foi criado com sucesso!')

        return HttpResponseRedirect(reverse('listar_relatorios_mensais'))


def listar_relatorios_mensais(request):
    usuario = obterUsuario(request)
    print(usuario.funcao)

    relatorios = RelatorioMensal.objects.filter(igreja=usuario.igreja)

    context = {
        'relatorios': relatorios,
        'usuario': usuario,
        'igreja': usuario.igreja,

    }

    return render(request, 'financas/relatorios/mensal/listar.html', context)


def excluir_relatorio_mensal(request, relatorio_id):
    relatorio_mensal = RelatorioMensal.objects.get(id=relatorio_id)
    relatorio_mensal.delete()

    return HttpResponseRedirect(reverse('listar_relatorios_mensais'))


def detalhar_relatorio_mensal(request, relatorio_id):
    usuario = obterUsuario(request)
    relatorio_mensal = RelatorioMensal.objects.get(id=relatorio_id)

    mes_relatorio = relatorio_mensal.data_inicio.month
    ano_relatorio = relatorio_mensal.data_inicio.year

    entradas_relatorio = OfertaCulto.objects.filter(
        data_culto__month=mes_relatorio, data_culto__year=ano_relatorio, igreja=relatorio_mensal.igreja)

    context = {
        'relatorio_mensal': relatorio_mensal,
        'usuario': usuario,
        'igreja': usuario.igreja,
        'entradas_relatorio': entradas_relatorio,
    }

    return render(request, 'financas/relatorios/mensal/detalhar.html', context)


def finalizar_relatorio_mensal(request, relatorio_id):
    relatorio = RelatorioMensal.objects.get(id=relatorio_id)
    relatorio.status = 'Finalizado'
    relatorio.save()
    criar_novo_relatorio_mensal(request)
    return HttpResponseRedirect(reverse('listar_relatorios_mensais'))

####################### - - - RELATÓRIO GERAL - - - ######################


def criar_novo_relatorio_geral(request):
    user = obterUsuario(request)

    try:
        relatorio_ativo = RelatorioGeral.objects.get(status='Ativo')

    except:
        relatorio_ativo = None

    if relatorio_ativo:
        messages.error(request, 'Já existe um relatório ativo !')
        return HttpResponseRedirect(reverse('listar_relatorios_gerais'))
    else:
        # obtendo a data que contém o último dia do mês
        data_atual = datetime.now()

        # Obtém o último dia do mês
        ultimo_dia = calendar.monthrange(data_atual.year, data_atual.month)[1]

        # Cria a data do último dia do mês
        data_ultimo_dia = datetime(
            data_atual.year, data_atual.month, ultimo_dia)

        # Formata a data no formato "dd/mm/aaaa"
        data_fim = data_ultimo_dia.strftime("%Y-%m-%d")

        data_criacao = datetime.now()
        data_criacao = data_criacao.strftime("%Y-%m-%d")
        relatorio_geral = RelatorioGeral(
            tesoureiro_sede=user, data_inicio=data_criacao,  data_fim=data_fim)
        relatorio_geral.save()
        messages.success(
            request, 'Um novo Relatório Geral foi criado com sucesso!')

        return HttpResponseRedirect(reverse('listar_relatorios_gerais'))


def listar_relatorios_gerais(request):
    usuario = obterUsuario(request)
    relatorios_gerais = RelatorioGeral.objects.filter(tesoureiro_sede=usuario)
    context = {
        'relatorios': relatorios_gerais,
        'usuario': usuario,
        'igreja': usuario.igreja,
    }
    return render(request, 'financas/relatorios/geral/listar.html', context)


def excluir_relatorio_geral(request, relatorio_id):
    relatorio_geral = RelatorioGeral.objects.get(id=relatorio_id)
    relatorio_geral.delete()

    return HttpResponseRedirect(reverse('listar_relatorios_gerais'))


def detalhar_relatorio_geral(request, relatorio_id):
    usuario = obterUsuario(request)
    relatorio_geral = RelatorioGeral.objects.get(id=relatorio_id)

    if request.method == "POST":
        form = RelatorioGeralForm(request.POST, instance=relatorio_geral)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalhar_relatorio_geral', args=[relatorio_geral.id]))
    else:
        form = RelatorioGeralForm(instance=relatorio_geral)

    context = {
        'relatorio_geral': relatorio_geral,
        'usuario': usuario,
        'igreja': usuario.igreja,
        'form': form,
    }
    return render(request, 'financas/relatorios/geral/detalhar.html', context)


def finalizar_relatorio_geral(request, relatorio_id):
    relatorio = RelatorioGeral.objects.get(id=relatorio_id)
    relatorio.status = 'Finalizado'
    relatorio.save()

    criar_novo_relatorio_geral(request)
    return HttpResponseRedirect(reverse('listar_relatorios_gerais'))


############################ Gerar PDF  #######################
@login_required
@permission_required('accounts.tesoureiro')
def gerar_relatorio_geral(request, relatorio_id):
    relatorio_geral = RelatorioGeral.objects.get(id=relatorio_id)
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y às %H:%M")
    tesoureiro = obterUsuario(request)

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4)
    elements = []

    # Gerar o QR code
    qr_code_link = "http://127.0.0.1:8000/financas/relatorios/geral/detalhar/" + \
        str(relatorio_id)
    qr_code = qrcode.make(qr_code_link)

    # Adicionar o QR code ao PDF
    buf_qr = io.BytesIO()
    qr_code.save(buf_qr, format="PNG")
    qr_code_img = buf_qr.getvalue()
    buf_qr.close()
    igreja = "Igreja Evangélica Assembléia de Deus<br/>"
    endereco = "Rua 01, Nº 408 - Bairro Brindes<br/>"
    departamento = "Departamento Administrativo - Guanambi - BA<br/>"

    # Adicionar a imagem do QR code aos elementos do PDF
    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))
    qr_img = io.BytesIO(qr_code_img)
    
    elements.append(Paragraph("<br/>", getSampleStyleSheet()['Normal']))
    image_path = os.path.abspath('static/assets/images/profile-picture.png')
    # Título e informações da igreja
    header_data = [
        [
            Image(image_path, width=35, height=35),
            Paragraph(igreja+endereco+departamento, getSampleStyleSheet()['Normal']), 
            Image(qr_img, width=50, height=50)]
    ]
    header_table = Table(header_data, colWidths=[50, 380, 50], rowHeights=[30])
    title_data = [
        ["Relatório Financeiro: Mês de " +
            str(datetime.today().strftime("%b %Y"))],

    ]
    elements.append(header_table)

    table_title = Table(title_data, colWidths=[400], rowHeights=[30])
    table_title.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    
    elements.append(table_title)
    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))

    # Tabela de entradas
    data_entradas = [
        ["ENTRADAS"],
        ["SEDE:", 'R$ ' + str(relatorio_geral.calc_entradas_sede)],
        ["CONGREGAÇÕES", 'R$ ' + str(relatorio_geral.calc_entradas_locais)],
        ["TOTAL:", 'R$ ' + str(relatorio_geral.calc_total_entradas)],
    ]

    table_entradas = Table(data_entradas, colWidths=[300, 100])
    table_entradas.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Header background color
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(Paragraph("<br/>", getSampleStyleSheet()['Normal']))
    elements.append(table_entradas)

    # Tabela de saídas
    data_saidas = [
        ["SAÍDAS", ""],
        ["SEDE:", 'R$ ' + str(relatorio_geral.calc_saidas_sede)],
        ["CONGREGAÇÕES", 'R$ ' + str(relatorio_geral.calc_saidas_locais)],
        ["PGTO OBREIROS", 'R$ ' + str(relatorio_geral.pgto_obreiros)],
        ["INSS", 'R$ ' + str(relatorio_geral.inss)],
        ["ALUGUEL DE OBREIROS", 'R$ ' + str(relatorio_geral.aluguel_obreiros)],
        ["REPS/REFMAS/CONST", 'R$ ' + str(relatorio_geral.construcoes)],
        ["ASSIS. SOCIAL", 'R$ ' + str(relatorio_geral.assis_social)],
        ["TOTAL:", 'R$ ' + str(relatorio_geral.calc_total_saidas)],
    ]

    table_saidas = Table(data_saidas, colWidths=[300, 100])
    table_saidas.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Header background color
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))
    elements.append(table_saidas)

    # Saldo Atual (using a table)
    saldo_atual_data = [
        ["SALDO ATUAL", ""],
        ["TOTAL:", 'R$ ' + str(relatorio_geral.calc_saldo)],
    ]

    table_saldo_atual = Table(saldo_atual_data, colWidths=[300, 100])
    table_saldo_atual.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # Header background color
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
    ]))

    elements.append(Paragraph("<br/><br/>",
                    getSampleStyleSheet()['Normal']))
    elements.append(table_saldo_atual)

    elements.append(Paragraph("<br/><br/><br/><br/>",
                    getSampleStyleSheet()['Normal']))
    elements.append(Paragraph("Gerado em " + data_atual, getSampleStyleSheet()['Normal'])) 

    signature_data = [
        ["_"*40],
        [tesoureiro.nome.upper()],
        ["Tesoureiro"]
    ]

    table_signature = Table(signature_data, colWidths=[
        400], rowHeights=[15, 15, 15])
    table_signature.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elements.append(Paragraph("<br/><br/><br/>",
                    getSampleStyleSheet()['Normal']))
    elements.append(table_signature)

    doc.build(elements)

    buf.seek(0)

    arquivo = f'Relatorio Geral - {str(datetime.today().strftime("%b %Y"))}.pdf'
    return FileResponse(buf, as_attachment=True, filename=arquivo)


def gerar_relatorio_mensal(request, relatorio_id):
    relatorio_mensal= RelatorioMensal.objects.get(id=relatorio_id)
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y às %H:%M")
    tesoureiro = obterUsuario(request)
    igreja = tesoureiro.igreja
    nome_igreja = igreja.nome

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4)
    elements = []

    # Gerar o QR code
    qr_code_link = "http://127.0.0.1:8000/financas/relatorios/mensal/detalhar/" + \
        str(relatorio_id)
    qr_code = qrcode.make(qr_code_link)

    # Adicionar o QR code ao PDF
    buf_qr = io.BytesIO()
    qr_code.save(buf_qr, format="PNG")
    qr_code_img = buf_qr.getvalue()
    buf_qr.close()
    endereco = igreja.localizacao
    departamento = "Departamento Administrativo - Guanambi - BA<br/>"

    # Adicionar a imagem do QR code aos elementos do PDF
    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))
    qr_img = io.BytesIO(qr_code_img)

    elements.append(Paragraph("<br/>", getSampleStyleSheet()['Normal']))
    image_path = os.path.abspath('static/assets/images/profile-picture.png')
    # Título e informações da igreja
    header_data = [
        [
            Image(image_path, width=35, height=35),
            Paragraph(nome_igreja+endereco+departamento, getSampleStyleSheet()['Normal']), 
            Image(qr_img, width=50, height=50)]
    ]
    header_table = Table(header_data, colWidths=[50, 380, 50], rowHeights=[30])
    title_data = [
        ["Relatório Financeiro Mensal: Mês de " +
            str(datetime.today().strftime("%b %Y"))],

    ]
    elements.append(header_table)

    table_title = Table(title_data, colWidths=[400], rowHeights=[30])
    table_title.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))


    elements.append(table_title)
    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))

    # Tabela de entradas
    data_entradas = [
        ["ENTRADAS"],
        ["TOTAL:", 'R$ ' + str(relatorio_mensal.calc_total_entradas)],
    ]

    table_entradas = Table(data_entradas, colWidths=[300, 100])
    table_entradas.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Header background color
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(Paragraph("<br/>", getSampleStyleSheet()['Normal']))
    elements.append(table_entradas)

    # Tabela de saídas
    data_saidas = [
        ["SAÍDAS", ""],
        ["PGTO OBREIROS", 'R$ ' + str(relatorio_mensal.pagamento_obreiro)],
        ["MISSÕES SEDE", 'R$ ' + str(relatorio_mensal.missoes_sede)],
        ["FUNDO CONVENCIONAL", 'R$ ' + str(relatorio_mensal.fundo_convencional)],
        ["TOTAL:", 'R$ ' + str(relatorio_mensal.calc_saidas)],
    ]

    table_saidas = Table(data_saidas, colWidths=[300, 100])
    table_saidas.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Header background color
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['Normal']))
    elements.append(table_saidas)

    # Saldo Atual (using a table)
    saldo_atual_data = [
        ["SALDO ATUAL", ""],
        ["TOTAL:", 'R$ ' + str(relatorio_mensal.calc_saldo)],
    ]

    table_saldo_atual = Table(saldo_atual_data, colWidths=[300, 100])
    table_saldo_atual.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        # Header background color
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
    ]))

    elements.append(Paragraph("<br/><br/>",
                    getSampleStyleSheet()['Normal']))
    elements.append(table_saldo_atual)

    elements.append(Paragraph("<br/><br/><br/><br/>",
                    getSampleStyleSheet()['Normal']))
    elements.append(Paragraph("Gerado em " + data_atual, getSampleStyleSheet()['Normal'])) 

    signature_data = [
        ["_"*40],
        [tesoureiro.nome.upper()],
        ["Tesoureiro"]
    ]

    table_signature = Table(signature_data, colWidths=[
        400], rowHeights=[15, 15, 15])
    table_signature.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elements.append(Paragraph("<br/><br/><br/>",
                    getSampleStyleSheet()['Normal']))
    elements.append(table_signature)

    doc.build(elements)

    buf.seek(0)

    arquivo = f'Relatorio Mensal - {str(datetime.today().strftime("%b %Y"))}.pdf'
    return FileResponse(buf, as_attachment=True, filename=arquivo)



###############################################  FILTROS  ##################################################################


def filtrar_ofertas(request):
    if request.method == 'POST':
        # Obtém o valor do input do template
        date_input = request.POST.get('date_input')
        ofertas_filtradas = OfertaCulto.objects.filter(
            data_culto=date_input)  # Realiza a filtragem do modelo

        return render(request, 'financas/entradas/ofertas/listar.html', {'ofertas_filtradas': ofertas_filtradas})

    return render(request, 'financas/entradas/ofertas/listar.html')


def filtrar_saidas(request):
    if request.method == 'POST':
        # Obtém o valor do input do template
        date_input = request.POST.get('date_input')
        saidas_filtradas = Saida.objects.filter(
            data=date_input)  # Realiza a filtragem do modelo

        return render(request, 'financas/saidas/listar.html', {'saidas_filtradas': saidas_filtradas})

    return render(request, 'financas/saidas/listar.html')


def filtrar_dizimos(request):
    if request.method == 'POST':
        # Obtém o nome do membro do formulário
        membro = request.POST.get('membro', '')
        # Filtra os dizimos com base no nome do membro
        dizimos = Dizimo.objects.filter(membro__nome__icontains=membro)
        context = {
            'dizimos_filtrados': dizimos
        }
        return render(request, 'financas/entradas/dizimos/listar.html', context)
    else:
        return render(request, 'financas/entradas/dizimos/listar.html')
