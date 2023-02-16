from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from . models import Pastor, Tesoureiro, TesoureiroSede
from django.contrib.auth.models import User

class UserForm():
    
class PastorForm(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = Pastor
        fields = ["username","email", "password1", "password2", "cpf", "telefone", "igreja"]
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if Pastor.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))
        return e


class TesoureiroSedeForm(UserCreationForm):
    email=forms.EmailField(max_length=30)

    class Meta:
        model = TesoureiroSede
        fields = ["username","email", "password1", "password2", "cpf", "telefone", "igreja"]
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if TesoureiroSede.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))    
        return e


class TesoureiroForm(UserCreationForm):
    email=forms.EmailField(max_length=30)

    class Meta:
        model = Tesoureiro
        fields = ["username","email", "password1", "password2", "cpf", "telefone", "igreja"]
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if Tesoureiro.objects.filter(email=e).exists():
            raise ValidationError('O email {} já está em uso.'.format(e))    
        return e


class PastorFormChangeAdmin(UserChangeForm):
    class Meta:
        model = Pastor
        fields = ["email", "password"]

class TesoureiroFormChangeAdmin(UserChangeForm):
    class Meta:
        model = Tesoureiro
        fields = ["email", "password"]

class TesoureiroSedeFormChangeAdmin(UserChangeForm):
    class Meta:
        model = Tesoureiro
        fields = ["email", "password"]





