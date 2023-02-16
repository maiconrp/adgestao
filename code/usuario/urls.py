from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView

from .views import *

urlpatterns = [
    path('',                                    renderLP, name="renderLP"),
    path('mudar_senha/',                        PasswordChangeView.as_view(template_name='usuario/mudarSenha.html')),
    path('solicitacoes/',                       listar_solicitacoes,    name='listar_solicitacoes'),
    path('solicitacao/autorizar/<str:cpf>/',    autorizar_solicitacao,  name='autorizar_solicitacao'),
    path('solicitacao/negar/<str:cpf>/',        negar_solicitacao,      name='negar_solicitacao'),
    path('cadastro/solicitar/',                 solicitar_cadastro,     name='solicitar_cadastro'),
    path('solicitacao/acompanhar/',             acompanhar_cadastro,    name='acompanhar_cadastro'),
]
