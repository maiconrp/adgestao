from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/solicitar/', solicitar_cadastro, name='solicitar_cadastro'),
    path('cadastro/acompanhar/', acompanhar_cadastro, name='acompanhar_cadastro'),
    path('cadastro/listar/', listar_cadastros, name='listar_cadastros'),
    path('cadastro/detalhar/', detalhar_cadastros, name='detalhar_cadastros'),
    path('cadastro/responder/', responder_cadastro, name='responder_cadastro'),
]
