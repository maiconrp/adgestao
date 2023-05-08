from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Saida
from .forms import SaidaForm
from accounts.models import Usuario

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
@permission_required('accounts.tesoureiro')
def adicionar_saida(request):
    
    if request.method == 'POST':
        
        form = SaidaForm(request.POST)
        if form.is_valid():
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
    # usuario = Usuario.objects.get(pk=request.user.pk)
    # saidas = Saida.objects.filter(igreja=usuario.igreja)
    saidas = Saida.objects.all()
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