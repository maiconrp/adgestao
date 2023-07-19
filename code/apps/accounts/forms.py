from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import Usuario
from adgestao.validators import validate_cpf, validate_telefone


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        
        fields = ["nome", "email", "password1", "password2",
                  "cpf", "telefone", "igreja", "funcao"]
        


class UsuarioFormChangeAdmin(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ["email", "password"]
