from django import forms
from django.core.exceptions import ValidationError

from .models import Igreja, Membro, Dizimo, OfertaCulto

class IgrejaForm(forms.ModelForm):

    class Meta:
        model = Igreja
        fields = ['nome', 'localizacao', 'saldo']


class MembroForm(forms.ModelForm):

    class Meta:
        model = Membro
        fields = ['nome', 'data_nasc', 'sexo', 'cpf']


class DizimoForm(forms.ModelForm):

    class Meta:
        model = Dizimo
        fields = ['data', 'valor', 'membro', 'tipo_culto', 'data_culto']


class OfertaForm(forms.ModelForm):

    class Meta:
        model = OfertaCulto
        fields = ['data_culto', 'valor_oferta', 'tipo_culto']