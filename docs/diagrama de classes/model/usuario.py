#-*- coding: utf-8 -*-

from django.db import models

class Usuario(models.Model):
    class Meta:
        pass

    nome = undefined()
    email = undefined()
    cpf = undefined()
    senha = undefined()
    telefone = undefined()


    def solicitarCadastro(self, nome, e-mail, cpf):
        pass

    def acompanharCadastro(self, cpf):
        pass

    def atualizarCadastro(self, nome?, e-mail?, cpf, senha):
        pass

    def realizarLogin(self, email, senha):
        pass

    def realizarLogout(self, ):
        pass

