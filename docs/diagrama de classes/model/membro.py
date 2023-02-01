#-*- coding: utf-8 -*-

from django.db import models

class Membro(models.Model):
    class Meta:
        pass

    nome = undefined()
    data_nasc = undefined()
    sexo = undefined()
    cpf = undefined()


    def gerarRelatorio(self, **keyargs):
        pass

    def adicionar(self, Membro):
        pass

    def editar(self, cpf):
        pass

    def visualizar(self, **keyargs?):
        pass

    def excluir(self, cpf):
        pass

    def detalhar(self, cpf):
        pass

