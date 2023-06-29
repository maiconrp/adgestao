from django.contrib import admin
from .models import *
from django import forms

class DizimoAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.igreja:
            self.fields['membro'].queryset = self.fields['membro'].queryset.filter(igreja=self.instance.igreja)

class DizimoAdmin(admin.ModelAdmin):
    form = DizimoAdminForm


admin.site.register(Dizimo, DizimoAdmin)
admin.site.register(OfertaCulto)
admin.site.register(Membro)
admin.site.register(Igreja)