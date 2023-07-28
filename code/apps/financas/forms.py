from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import Saida, Entradas, RelatorioGeral

class SaidaForm(forms.ModelForm):

    class Meta:
        model = Saida
        fields = ['descricao', 'data', 'valor']


class EntradaForm(forms.ModelForm):

    class Meta:
        model = Entradas
        fields = ['igreja']

class RelatorioGeralForm(forms.ModelForm):

    class Meta:
        model = RelatorioGeral
        fields = ['inss', 'aluguel_obreiros', 'assis_social', 'construcoes', 'pgto_obreiros']
