from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TesoureiroSede)
admin.site.register(Tesoureiro)
admin.site.register(Pastor)
admin.site.register(SolicitacaoCadastro)