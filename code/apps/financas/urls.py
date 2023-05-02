from django.urls import path
from .views import *

urlpatterns = [
    path('saidas/adicionar/', adicionar_saida, name='adicionar_saida'),
    path('saidas/excluir/<uuid:saida_id>/', excluir_saida, name='excluir_saida'),
    path('saidas/listar/', listar_saida, name='listar_saida'),
    path('saidas/detalhar/<uuid:saida_id>/', detalhar_saida, name='detalhar_saida'),
    path('saidas/editar/<uuid:saida_id>/', editar_saida, name='editar_saida'),
]
