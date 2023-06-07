from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Saida, Entrada
from igreja.models import Oferta, Dizimo
from igreja.forms import OfertaForm, DizimoForm
from .forms import SaidaForm
from accounts.models import Usuario
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
    # usuario = Usuario.objects.get(pk=request.user.pk)
    # saidas = Saida.objects.filter(igreja=usuario.igreja)
    dizimos = Dizimo.objects.all()
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