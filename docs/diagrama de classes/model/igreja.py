#-*- coding: utf-8 -*-

from django.db import models

class Igreja(models.Model):
    class Meta:
        pass

    id = undefined()
    localização = undefined()
    saldo = undefined()
    nome = undefined()


    def gerarRelatorio(self, **keyargs):
        pass

