from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Saida
from .forms import SaidaForm
from accounts.models import Usuario


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
