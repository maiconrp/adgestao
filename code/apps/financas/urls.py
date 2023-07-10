from django.urls import path
from .views import *

urlpatterns = [
    path('saidas/adicionar/', adicionar_saida, name='adicionar_saida'),
    path('saidas/gerar_relatorio/', gerar_relatorio, name='gerar_relatorio'),
    path('saidas/excluir/<uuid:saida_id>/', excluir_saida, name='excluir_saida'),
    path('saidas/listar/', listar_saida, name='listar_saida'),
    path('saidas/detalhar/<uuid:saida_id>/', detalhar_saida, name='detalhar_saida'),
    path('saidas/editar/<uuid:saida_id>/', editar_saida, name='editar_saida'),
    path('saidas/filtrar/', filtrar_saidas, name='filtrar_saidas'),
    path('dizimos/adicionar/', adicionar_dizimo, name='adicionar_dizimo'),
    path('entradas/gerar_relatorio/', gerar_relatorio, name='gerar_relatorio'),
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
]
