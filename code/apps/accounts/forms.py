from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from . models import Usuario
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = Usuario
        fields = ["username","email", "password1", "password2", "cpf", "telefone", "igreja", "funcao"]
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if Usuario.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))
        return e

class UsuarioFormChangeAdmin(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ["email", "password"]