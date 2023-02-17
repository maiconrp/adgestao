from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Usuario(User):
    FUNCAO_CHOICES = (
        ("P", "Pastor"),
        ("T", "Tesoureiro"),
        ("TS", "Tesoureiro Sede"),
    )
    
    cpf = models.CharField(
        max_length=13, 
        unique=True, 
        primary_key=True,
        blank=False, 
        null=False,
    )
    telefone = models.CharField(
        max_length=20,
        blank=False, 
        null=False
    )
    
    funcao = MultiSelectField(
        choices=FUNCAO_CHOICES,
        max_length=20, 
        max_choices=1,
        blank=False, 
        null=False,
    )
    
    def __str__(self):
        return self.username

    def solicitar_cadastro(self, nome, email, cpf, senha, telefone=None, igreja=None):
        """
        Método responsável por permitir que um usuário solicite cadastro no sistema.
        Recebe o nome, email, CPF, senha, telefone e igreja do usuário como parâmetros.
        """
        # Implementação da lógica para solicitar cadastro

    def acompanhar_cadastro(self, cpf):
        """
        Método responsável por permitir que um usuário acompanhe o status de seu cadastro no sistema.
        Recebe o CPF do usuário como parâmetro.
        """
        # Implementação da lógica para acompanhar cadastro

    def atualizar_cadastro(self, nome=None, email=None, cpf=None, senha=None, telefone=None, igreja=None):
        """
        Método responsável por permitir que um usuário atualize seus dados de cadastro no sistema.
        Recebe o nome, email, CPF, senha, telefone e igreja do usuário como parâmetros (opcional).
        """
        # Implementação da lógica para atualizar cadastro

    def realizar_login(self):
        """
        Método responsável por realizar o login de um usuário no sistema.
        Recebe o email e a senha do usuário como parâmetros.
        """
        # Implementação da lógica para realizar o login

    def realizar_logout(self):
        """
        Método responsável por realizar o logout do usuário atual no sistema.
        """
        # Implementação da lógica para realizar o logout

