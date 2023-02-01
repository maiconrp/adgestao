#-*- coding: utf-8 -*-

from django.db import models

class Dizimo(models.Model):
    class Meta:
        pass

    id = undefined()
    data_pgto = undefined()
    valor = undefined()
    validacao_tesoureiro = undefined()


    def gerarRelatorio(self, **keyargs):
        pass

    def adicionar(self, Dizimo):
        pass

    def editar(self, id):
        pass

    def visualizar(self, **keyargs?):
        pass

    def excluir(self, id):
        pass

