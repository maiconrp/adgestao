from django.urls import path
from .views import *

urlpatterns = [
    path('saidas/adicionar/', adicionar_saida, name='adicionar_saida'),
    path('saidas/excluir/<uuid:saida_id>/', excluir_saida, name='excluir_saida'),
    path('saidas/listar/', listar_saidas, name='listar_saidas'),
    path('saidas/detalhar/<uuid:saida_id>/', detalhar_saida, name='detalhar_saida'),
    path('saidas/editar/<uuid:saida_id>/', editar_saida, name='editar_saida'),
    path('saidas/filtrar/', filtrar_saidas, name='filtrar_saidas'),
    path('dizimos/adicionar/', adicionar_dizimo, name='adicionar_dizimo'),
    path('dizimos/excluir/<uuid:dizimo_id>/', excluir_dizimo, name='excluir_dizimo'),
    path('dizimos/listar/', listar_dizimos, name='listar_dizimos'),
    path('dizimos/detalhar/<uuid:dizimo_id>/', detalhar_dizimo, name='detalhar_dizimo'),
    path('dizimos/editar/<uuid:dizimo_id>/', editar_dizimo, name='editar_dizimo'),
    path('entradas/dizimos/filtrar/', filtrar_dizimos, name='filtrar_dizimos'),
    path('ofertas/adicionar/', adicionar_oferta, name='adicionar_oferta'),
    path('ofertas/excluir/<uuid:oferta_id>/', excluir_oferta, name='excluir_oferta'),
    path('ofertas/listar/', listar_ofertas, name='listar_ofertas'),
    path('ofertas/detalhar/<uuid:oferta_id>/', detalhar_oferta, name='detalhar_oferta'),
    path('ofertas/editar/<uuid:oferta_id>/', editar_oferta, name='editar_oferta'),
    path('ofertas/filtrar/', filtrar_ofertas, name='filtrar_ofertas'),
    path('relatorios/mensal/excluir/<uuid:relatorio_id>/', excluir_relatorio_mensal, name='excluir_relatorio_mensal'),
    path('relatorios/mensal/listar/', listar_relatorios_mensais, name='listar_relatorios_mensais'),
    path('relatorios/mensal/detalhar/<uuid:relatorio_id>/', detalhar_relatorio_mensal, name='detalhar_relatorio_mensal'),
    path('relatorios/mensal/finalizar/<uuid:relatorio_id>/', finalizar_relatorio_mensal, name='finalizar_relatorio_mensal'),
    path('relatorios/mensal/criar/', criar_novo_relatorio_mensal, name='criar_novo_relatorio_mensal'),
    path('relatorios/mensal/gerar-relatorio/<uuid:relatorio_id>/', gerar_relatorio_mensal, name='gerar_relatorio_mensal'),
    path('relatorios/geral/listar/', listar_relatorios_gerais, name='listar_relatorios_gerais'),
    path('relatorios/geral/detalhar/<uuid:relatorio_id>/', detalhar_relatorio_geral, name='detalhar_relatorio_geral'),
    path('relatorios/geral/finalizar/<uuid:relatorio_id>/', finalizar_relatorio_geral, name='finalizar_relatorio_geral'),
    path('relatorios/geral/criar/', criar_novo_relatorio_geral, name='criar_novo_relatorio_geral'),
    path('relatorios/geral/atualizar-saldo/', atualizar_saldo, name='atualizar_saldo'),
    path('relatorios/geral/gerar-relatorio/<uuid:relatorio_id>/', gerar_relatorio_geral, name='gerar_relatorio_geral'),


]
