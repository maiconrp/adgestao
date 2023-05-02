from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import Saida

class SaidaForm(forms.ModelForm):

    class Meta:
        model = Saida
        fields = ['descricao', 'data', 'valor', 'igreja']