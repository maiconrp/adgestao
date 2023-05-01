from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/home/',  home, name='home'),
    path('cadastro/solicitar/', solicitar_cadastro, name='solicitar_cadastro'),
    path('cadastro/acompanhar/<int:solicitacao_id>/', acompanhar_cadastro, name='acompanhar_cadastro'),
    path('cadastro/listar/', listar_cadastros, name='listar_cadastros'),
    path('cadastro/detalhar/<int:solicitacao_id>/', detalhar_cadastro, name='detalhar_cadastro'),
    path('cadastro/responder/<int:solicitacao_id>/<str:acao>/', responder_cadastro, name='responder_cadastro'),
]
