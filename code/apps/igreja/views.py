from django.shortcuts import render
from django.db import transaction
from .forms import IgrejaForm, MembroForm
from .models import Igreja, Membro, Dizimo
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from accounts.views import obterUsuario
from financas.views import criar_relatorio_mensal
from financas.models import Entrada


# Create your views here.
@login_required
@permission_required('accounts.tesoureiro_sede')
def cadastrar_igreja(request):

    usuario = obterUsuario(request)

    if request.method == 'POST':
    
        form = IgrejaForm(request.POST)
        if form.is_valid():
            igreja_cad = form.save()
            igreja_cad.save()

            #   Ao cadastrar uma nova igreja, uma instância do objeto Entrada é criado. Este objeto é vinculado a uma igreja
            # e contém o registro de todos os dízimos e ofertas da mesma
            entrada_criada = Entrada(igreja=igreja_cad)
            entrada_criada.save()

            criar_relatorio_mensal(igreja_cad, entrada_criada)
           
            messages.success(request, 'Igreja cadastrada com sucesso !')
            context = {
                    'form': form,
                }
            return HttpResponseRedirect(reverse('listar_igrejas'))
    else:
        form = IgrejaForm()
        
    context = {
        'form' : form,
    }
 
    return render(request, 'igreja/cadastrar.html', context)

@login_required
@permission_required('accounts.tesoureiro_sede')
def listar_igrejas(request):
    usuario = obterUsuario(request)
    
    igrejas = Igreja.objects.all()
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'igrejas': igrejas
    }
    return render(request, 'igreja/listar.html', context)

@login_required
@permission_required('accounts.tesoureiro_sede')
def editar_igreja(request, igreja_id = ''):
    usuario = obterUsuario(request)
    if igreja_id != '':
        igreja = Igreja.objects.get(id=igreja_id)
    else:
        igreja = Igreja.objects.get(id=request.user.igreja)

    if request.method == "POST":
        form = IgrejaForm(request.POST, instance=igreja)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_igrejas'))
    else:
        form = IgrejaForm(instance=igreja)

    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'form' : form,
        'igreja':igreja
    }
    return render(request, 'igreja/editar.html', context)

@login_required
def cadastrar_membro(request):
    usuario = obterUsuario(request)
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.instance.igreja = usuario.igreja
            membro = form.save()
            membro.save()            
            messages.success(request, 'membro cadastrado com sucesso !')
            context = {
                    'form': form,
                }
            return HttpResponseRedirect(reverse('listar_membros'))
    else:
        form = MembroForm()
        
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'form' : form,
    }
    
    return render(request, 'igreja/membros/cadastrar.html', context)

@login_required
def listar_membros(request):
    usuario = obterUsuario(request)
    membros = Membro.objects.filter(igreja=usuario.igreja)
    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'membros': membros
    }
    return render(request, 'igreja/membros/listar.html', context)

@login_required
def editar_membro(request, membro_id):
    usuario = obterUsuario(request)
    membro = Membro.objects.get(id=membro_id)
    if request.method == "POST":
        form = MembroForm(request.POST, instance=membro)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_membros'))
    else:
        form = MembroForm(instance=membro)

    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'form' : form,
    }
    return render(request, 'igreja/membros/editar.html', context)

@login_required
def excluir_membro(request, membro_id):
    membro = Membro.objects.get(id=membro_id)
    membro.delete()

    return HttpResponseRedirect(reverse('listar_membros'))


