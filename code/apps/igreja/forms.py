from django import forms
from django.core.exceptions import ValidationError

from .models import Igreja, Membro

class IgrejaForm(forms.ModelForm):

    class Meta:
        model = Igreja
        fields = ['nome', 'localizacao', 'saldo']

class MembroForm(forms.ModelForm):

    class Meta:
        model = Membro
        fields = ['nome', 'data_nasc', 'sexo', 'cpf']