from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView
 
urlpatterns = [
    path('', views.renderLP, name="renderLP"),
    path('registrar_tesoureiro_sede/', views.criarTesoureiroSede, name="criarTesoureiroSede"),
    path('registrar_pastor/', views.criarPastor, name="addTeacher"),
    path('registrar_tesoureiro/', views.criarTesoureiro, name="criarTesoureiro"),
    path('mudar_senha/', PasswordChangeView.as_view(template_name='usuario/mudarSenha.html')),
    path('mudar_senha/done/', PasswordChangeView.as_view(template_name='home.html')),
 ]