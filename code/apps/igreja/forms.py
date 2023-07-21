from django import forms
from django.core.exceptions import ValidationError

from .models import Igreja, Membro, Dizimo, OfertaCulto

class IgrejaForm(forms.ModelForm):

    class Meta:
        model = Igreja
        fields = ['nome', 'localizacao']


class MembroForm(forms.ModelForm):

    class Meta:
        model = Membro
        fields = ['nome', 'data_nasc', 'sexo', 'cpf']

class DizimoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(DizimoForm, self).__init__(*args, **kwargs)
        if usuario:
            self.fields['membro'].queryset = usuario.igreja.membros.all()

    class Meta:
            model = Dizimo
            fields = ['valor', 'membro', 'tipo_culto', 'data_culto']


class DizimoFormWithUser(DizimoForm):
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(DizimoFormWithUser, self).__init__(*args, **kwargs)
        if usuario:
            self.fields['membro'].queryset = usuario.igreja.membros.all()

    class Meta:
            model = Dizimo
            fields = ['valor', 'membro', 'tipo_culto', 'data_culto']
   


class OfertaForm(forms.ModelForm):

    class Meta:
        model = OfertaCulto
        fields = ['data_culto', 'valor_oferta', 'tipo_culto']