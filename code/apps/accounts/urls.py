from django.urls import path
from .views import *

urlpatterns = [
    path('home/',  home, name='home'),
    path('cadastro/solicitar/', solicitar_cadastro, name='solicitar_cadastro'),
    path('cadastro/acompanhar/<uuid:solicitacao_id>/', acompanhar_cadastro, name='acompanhar_cadastro'),
    path('cadastro/listar/', listar_cadastros, name='listar_cadastros'),
    path('cadastro/detalhar/<uuid:solicitacao_id>/', detalhar_cadastro, name='detalhar_cadastro'),
    path('cadastro/responder/<uuid:solicitacao_id>/<str:acao>/', responder_cadastro, name='responder_cadastro'),
]
