from django.shortcuts import render
from django.db import transaction
from .forms import IgrejaForm, MembroForm
from .models import Igreja, Membro, Dizimo
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from accounts.views import obterUsuario
from financas.views import criar_relatorio_mensal, criar_relatorio_geral
from financas.models import Entrada, RelatorioGeral



# Create your views here.
@login_required
#@permission_required('accounts.tesoureiro_sede')
def cadastrar_igreja(request):
    numero_igrejas_criadas = Igreja.objects.count()

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
    print(numero_igrejas_criadas)
    if numero_igrejas_criadas == 1:
        #entrada_sede = Entrada.objects.get(igreja=usuario.igreja)
        #print(entrada_sede.igreja)
        criar_relatorio_geral(usuario)
    else:
        print('Mais de uma igreja foi criada, o relatorio geral ja foi criado !')
        
    context = {
        'form' : form,
    }
    
    return render(request, 'igreja/cadastrar.html', context)



@login_required
@permission_required('accounts.tesoureiro')
def listar_igrejas(request):
    igrejas = Igreja.objects.all()
    context = {
        'igrejas': igrejas
    }
    return render(request, 'igreja/listar.html', context)

@login_required
@permission_required('accounts.tesoureiro_sede')
def editar_igreja(request, igreja_id):
    igreja = Igreja.objects.get(id=igreja_id)

    if request.method == "POST":
        form = IgrejaForm(request.POST, instance=igreja)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_igrejas'))
    else:
        form = IgrejaForm(instance=igreja)

    context = {
        'form' : form,
    }
    return render(request, 'igreja/editar.html', context)

@login_required
def cadastrar_membro(request):
    user = obterUsuario(request)
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.instance.igreja = user.igreja
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
        'form' : form,
    }
    
    return render(request, 'igreja/membros/cadastrar.html', context)

@login_required
def listar_membros(request):
    user = obterUsuario(request)
    membros = Membro.objects.filter(igreja=user.igreja)
    context = {
        'membros': membros
    }
    return render(request, 'igreja/membros/listar.html', context)

@login_required
def editar_membro(request, membro_id):
    membro = Membro.objects.get(id=membro_id)
    if request.method == "POST":
        form = MembroForm(request.POST, instance=membro)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_membros'))
    else:
        form = MembroForm(instance=membro)

    context = {
        'form' : form,
    }
    return render(request, 'igreja/membros/editar.html', context)

@login_required
def excluir_membro(request, membro_id):
    membro = Membro.objects.get(id=membro_id)
    membro.delete()

    return HttpResponseRedirect(reverse('listar_membros'))


