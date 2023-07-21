from django.shortcuts import render
from django.db import transaction
from .forms import IgrejaForm, MembroForm
from .models import Igreja, Membro, Dizimo
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from accounts.views import obterUsuario
from financas.views import criar_primeiro_relatorio_mensal, criar_primeiro_relatorio_geral
from financas.models import Entrada, RelatorioGeral
import calendar
from datetime import datetime


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

            criar_primeiro_relatorio_mensal(igreja_cad)

            messages.success(request, 'Igreja cadastrada com sucesso !')
            context = {
                'form': form,
                'usuario': usuario,
                'igreja': usuario.igreja,
            }
            return HttpResponseRedirect(reverse('listar_igrejas'))
    else:
        form = IgrejaForm()


    context = {
        'form': form,
        'usuario': usuario,
        'igreja': usuario.igreja,
    }

    return render(request, 'igreja/cadastrar.html', context)


@login_required
@permission_required('accounts.tesoureiro_sede')
def listar_igrejas(request):
    usuario = obterUsuario(request)

    igrejas = Igreja.objects.all()

    context = {
        'igrejas': igrejas,
        'usuario': usuario,
        'igreja': usuario.igreja,
    }
    return render(request, 'igreja/listar.html', context)


@login_required
@permission_required('accounts.tesoureiro_sede')
def editar_igreja(request, igreja_id):
    usuario = obterUsuario(request)

    igreja = Igreja.objects.get(id=igreja_id)

    if request.method == "POST":
        form = IgrejaForm(request.POST, instance=igreja)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_igrejas'))
    else:
        form = IgrejaForm(instance=igreja)

    membros = Membro.objects.filter(igreja=igreja)
    print(igreja.membros.count())

    context = {
        'usuario': usuario,
        'igreja': usuario.igreja,
        'form': form,
        'igreja': igreja,
        'membros': membros
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
        'form': form,
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
@permission_required('accounts.tesoureiro')
def editar_membro(request, membro_id):
    usuario = obterUsuario(request)
    membro = Membro.objects.get(id=membro_id)
    dizimos = Dizimo.objects.filter(membro=membro)
    if request.method == "POST":
        form = MembroForm(request.POST, instance=membro)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listar_membros'))
    else:
        form = MembroForm(instance=membro)

    context = {
        'membro': membro,
        'usuario': usuario,
        'igreja': usuario.igreja,
        'form': form,
        'dizimos': dizimos,
    }
    return render(request, 'igreja/membros/editar.html', context)


@login_required
@permission_required('accounts.tesoureiro')
def excluir_membro(request, membro_id):
    membro = Membro.objects.get(id=membro_id)
    membro.delete()

    return HttpResponseRedirect(reverse('listar_membros'))


#####################           FILTROS             ########################################

@login_required
def filtrar_membro(request):
    if request.method == 'POST':
        # Obtém o nome do membro do formulário
        nome = request.POST.get('nome', '')
        # Filtra os membros com base no nome
        membros = Membro.objects.filter(nome__icontains=nome)

        context = {
            'membros_filtrados': membros
        }
        return render(request, 'igreja/membros/listar.html', context)
    else:
        return render(request, 'igreja/membros/listar.html')


@login_required
def filtrar_igreja(request):
    if request.method == 'POST':
        # Obtém a parte do nome fornecida no formulário
        nome = request.POST.get('nome', '')
        # Filtra as igrejas cujos nomes contenham a parte fornecida
        igrejas = Igreja.objects.filter(nome__icontains=nome)

        context = {
            'igrejas_filtradas': igrejas
        }
        return render(request, 'igreja/listar.html', context)
    else:
        return render(request, 'igreja/listar.html')
