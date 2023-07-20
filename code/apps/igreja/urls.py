from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar/', cadastrar_igreja, name='cadastrar_igreja'),
    path('listar/', listar_igrejas, name='listar_igrejas'),  
    path('editar/<uuid:igreja_id>/', editar_igreja, name='editar_igreja'), 
    path('membros/cadastrar/', cadastrar_membro, name='cadastrar_membro'),
    path('membros/listar/', listar_membros, name='listar_membros'),  
    path('membros/editar/<uuid:membro_id>/', editar_membro, name='editar_membro'), 
    path('membros/excluir/<uuid:membro_id>/', excluir_membro, name='excluir_membro'), 
    path('filtrar-membro/', filtrar_membro, name='filtrar_membro'),
    path('filtrar-igreja/', filtrar_igreja, name='filtrar_igreja'),
]