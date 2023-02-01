#-*- coding: utf-8 -*-

from django.db import models

class Oferta(models.Model):
    class Meta:
        pass

    id = undefined()
    data_culto = undefined()
    valor_dizimo = undefined()
    valor_oferta = undefined()
    tipo_culto = undefined()
    validacao_tesoureiro = undefined()
    validacao_pastor = undefined()


    def gerarRelatorio(self, **keyargs):
        pass

    def adicionar(self, Oferta):
        pass

    def editar(self, id):
        pass

    def visualizar(self, **keyargs?):
        pass

    def excluir(self, id):
        pass

