from django.contrib import admin
from .models import *

class EntradaAdmin(admin.ModelAdmin):
    list_display = ('id', 'igreja')

class RMAdmin(admin.ModelAdmin):
    list_display = ('id', 'igreja', 'data_inicio')

admin.site.register(RelatorioMensal, RMAdmin)
admin.site.register(RelatorioGeral)
admin.site.register(Entradas, EntradaAdmin)
admin.site.register(Saida)
