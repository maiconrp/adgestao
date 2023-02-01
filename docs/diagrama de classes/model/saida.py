#-*- coding: utf-8 -*-

from django.db import models

class Saida(models.Model):
    class Meta:
        pass

    id = undefined()
    data = undefined()
    descricao = undefined()
    valor = undefined()
    tipo = undefined()
    validacao_tesoureiro = undefined()


    def gerarRelatorio(self, **keyargs):
        pass

    def adicionar(self, ):
        pass

    def editar(self, id):
        pass

    def excluir(self, id):
        pass

    def visualizar(self, **keyargs?):
        pass

