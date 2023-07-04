from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q

from .models import Saida, Entrada, RelatorioMensal
from igreja.models import OfertaCulto, Dizimo, Igreja
from igreja.forms import OfertaForm, DizimoForm
from .forms import SaidaForm
from accounts.views import obterUsuario


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
from datetime import datetime



@login_required
@permission_required('accounts.tesoureiro')
def adicionar_saida(request):
    user = obterUsuario(request)
    if request.method == 'POST':
        
        form = SaidaForm(request.POST)
        if form.is_valid():
            form.instance.igreja = user.igreja
            saida = form.save()
            saida.save()            
            messages.success(request, 'Saída adicionada com sucesso!')
            context = {
                    'form': form,
                }
            return HttpResponseRedirect(reverse('listar_saida'))
    else:
        form = SaidaForm()
        
    context = {
        'form' : form,
    }
    
    return render(request, 'financas/saidas/adicionar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def editar_saida(request, saida_id):

    saida = Saida.objects.get(id=saida_id)

    if request.method == "POST":
        form = SaidaForm(request.POST, instance=saida)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalhar_saida', args=[saida.id]))
    else:
        form = SaidaForm(instance=saida)

    context = {
        'form' : form,
    }
    return render(request, 'financas/saidas/editar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def excluir_saida(request, saida_id):
    saida = Saida.objects.get(id=saida_id)
    saida.delete()

    return HttpResponseRedirect(reverse('listar_saida'))


@login_required
@permission_required('accounts.tesoureiro')
def listar_saida(request):
    user = obterUsuario(request)
    saidas = Saida.objects.filter(igreja=user.igreja)
    context = {
        'saidas': saidas
    }
    return render(request, 'financas/saidas/listar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def detalhar_saida(request, saida_id):

    saida = Saida.objects.get(id=saida_id)
    context = {
        'saida': saida
    }
    return render(request, 'financas/saidas/detalhar.html', context)

@login_required
@permission_required('accounts.tesoureiro')
def adicionar_dizimo(request):
    user = obterUsuario(request)
    print(user.igreja)
    entrada = Entrada.objects.get(igreja=user.igreja)
    if request.method == 'POST':
        
        form = DizimoForm(request.POST)
        if form.is_valid():
            form.instance.igreja = user.igreja
            dizimo = form.save()
            dizimo.save()            
            messages.success(request, 'Dízimo adicionada com sucesso!')

            entrada.dizimos.add(dizimo)
            context = {
                    'form': form,
                }
            return HttpResponseRedirect(reverse('listar_dizimos'))
    else:
        form = DizimoForm()
        
    context = {
        'form' : form,
    }
    
    return render(request, 'financas/entradas/dizimos/adicionar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def editar_dizimo(request, dizimo_id):

    dizimo = Dizimo.objects.get(id=dizimo_id)

    if request.method == "POST":
        form = DizimoForm(request.POST, instance=dizimo)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalhar_dizimo', args=[dizimo.id]))
    else:
        form = DizimoForm(instance=dizimo)

    context = {
        'form' : form,
    }
    return render(request, 'financas/entradas/dizimos/editar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def excluir_dizimo(request, dizimo_id):
    dizimo = Dizimo.objects.get(id=dizimo_id)
    dizimo.delete()

    return HttpResponseRedirect(reverse('listar_dizimos'))


@login_required
@permission_required('accounts.tesoureiro')
def listar_dizimos(request):
    usuario = obterUsuario(request)

    igreja = Igreja.objects.get(nome=usuario.igreja.nome)
  
    dizimos = igreja.dizimos.all()
    
    context = {
        'dizimos': dizimos
    }
    return render(request, 'financas/entradas/dizimos/listar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def detalhar_dizimo(request, dizimo_id):

    dizimo = Dizimo.objects.get(id=dizimo_id)
    context = {
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

        #verifica se o dizimo em questão possui tanto a mesma data quanto o tipo de culto do relatório criado
        if dizimo.tipo_culto == oferta.tipo_culto and dizimo.data_culto == oferta.data_culto:
            valor_dizimo = valor_dizimo + dizimo.valor

    return valor_dizimo

def adicionar_oferta(request):
    user = obterUsuario(request)
    entrada = Entrada.objects.get(igreja=user.igreja)
    if request.method == 'POST':
        
        form = OfertaForm(request.POST)
        if form.is_valid():
            
            # Atribui ao atributo 'igreja' da oferta a igreja do usuario que esta criando o relatório de oferta
            form.instance.igreja = user.igreja

            oferta = form.save()
            oferta.save()     

            # Chama a função que calcula a soma dos valores dos dizimos daquele culto
            valor_dizimo = calc_soma_dizimo(oferta=oferta)

            # Atribui ao atributo "valor_dizimo" o valor calculado anteriormento pela função
            oferta.valor_dizimo = valor_dizimo

            # Salva a nova atribuição
            oferta.save()

            messages.success(request, 'Oferta adicionada com sucesso!')

            entrada.ofertas.add(oferta)

            context = {
                    'form': form,
                }
            return HttpResponseRedirect(reverse('listar_ofertas'))
    else:
        form = OfertaForm()
        
    context = {
        'form' : form,
    }
    
    return render(request, 'financas/entradas/ofertas/adicionar.html', context)

def listar_ofertas(request):
    usuario = obterUsuario(request)

    igreja = Igreja.objects.get(nome=usuario.igreja.nome)
  
    ofertas = igreja.ofertas_culto.all()

    context = {
        'ofertas': ofertas
    }
    return render(request, 'financas/entradas/ofertas/listar.html', context)


def excluir_oferta(request, oferta_id):
    oferta = OfertaCulto.objects.get(id=oferta_id)
    oferta.delete()

    return HttpResponseRedirect(reverse('listar_ofertas'))


def detalhar_oferta(request, oferta_id):
   
    oferta = OfertaCulto.objects.get(id=oferta_id)
    context = {
        'oferta': oferta
    }
    return render(request, 'financas/entradas/ofertas/detalhar.html', context)


def editar_oferta(request, oferta_id):
    oferta = OfertaCulto.objects.get(id=oferta_id)

    if request.method == "POST":
        form = OfertaForm(request.POST, instance=oferta)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalhar_oferta', args=[oferta.id]))
    else:
        form = OfertaForm(instance=oferta)

    context = {
        'form' : form,
    }
    return render(request, 'financas/entradas/dizimos/editar.html', context)



###################### - - - - - - RELATÓRIO MENSAL - - - - - -  ############################

def criar_relatorio_mensal(igreja, entrada):
    data_criacao = datetime.now()
    data_criacao = data_criacao.strftime("%Y-%m-%d")
    relatorio_mensal = RelatorioMensal(igreja=igreja, entradas=entrada, data_inicio=data_criacao)
    relatorio_mensal.save()

def listar_relatorios_mensais(request):
    usuario = obterUsuario(request)
    relatorios_mensais = RelatorioMensal.objects.filter(igreja=usuario.igreja)
    context = {
        'relatorios': relatorios_mensais
    }
    return render(request, 'financas/relatorios/mensal/listar.html', context)


def excluir_relatorio_mensal(request, relatorio_id):
    relatorio_mensal = RelatorioMensal.objects.get(id=relatorio_id)
    relatorio_mensal.delete()

    return HttpResponseRedirect(reverse('listar_relatorios_mensais'))


def detalhar_relatorio_mensal(request, relatorio_id):
   
    relatorio_mensal = RelatorioMensal.objects.get(id=relatorio_id)
    context = {
        'relatorio_mensal': relatorio_mensal
    }
    return render(request, 'financas/relatorios/mensal/detalhar.html', context)



@login_required
@permission_required('accounts.tesoureiro')
def gerar_relatorio(request):
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%d/%m/%Y às %H:%M")
    tesoureiro = obterUsuario(request)
    print(tesoureiro.igreja)
    naoBaixar = 0
    buf = io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Arial", 14)
    
    saidas = Saida.objects.all()

    lines = []
    lines.append(str(tesoureiro.igreja))
    lines.append(" ")
    lines.append("Relatório de Saídas - Mês e ano")
    lines.append(" ")
    lines.append(" ")
    lines.append(" ")
    lines.append("       Data                         Valor(R$)                        Descrição")
    lines.append(" ")

  
       
    if saidas:
        total = 0
        for saida in saidas:
                lines.append(str(saida.data) + '                      ' + str(f'{saida.valor:,.2f}') + '                     ' + str(saida.descricao))
                lines.append("______________________________________________________________")
                lines.append(" ")
                total = total + saida.valor
        naoBaixar = naoBaixar+1

    lines.append(" ")
    lines.append(f'Total: R${total:,.2f}')
    lines.append(" ")
    lines.append(" ")
    lines.append("Emitido em: " + str(data_atual))

    

           
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename= 'lista.pdf')