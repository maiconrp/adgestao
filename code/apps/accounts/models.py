from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from igreja.models import Igreja
from adgestao.validators import validate_telefone, validate_cpf
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator


class Usuario(User):
    FUNCAO_CHOICES = (
        ("P", "Pastor"),
        ("T", "Tesoureiro"),
        ("TS", "Tesoureiro Sede"),
    )
    
    nome = models.CharField(
        max_length=100, 
    )
    
    cpf = models.CharField(
        max_length=13, 
        primary_key=True,
        validators=[validate_cpf]     
    )
    
    telefone = models.CharField(
        max_length=20,  
        validators=[validate_telefone]    
    )
    
    funcao = MultiSelectField(
        choices=FUNCAO_CHOICES,
        max_length=20, 
        max_choices=1,   
    )
    
    igreja = models.ForeignKey(
        Igreja, 
        related_name='usuario', 
        on_delete=models.DO_NOTHING,
    )
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['cpf', 'nome', 'email', 'funcao', 'igreja']
    
    def __str__(self):
        return self.nome


class SolicitacaoCadastro(models.Model):
    
    usuario = models.ForeignKey(
        Usuario, 
        related_name='usuario_solicitacao_cadastro', 
        on_delete=models.CASCADE 
    )
    
    tesoureiro_sede_responsavel = models.ForeignKey(
        Usuario, 
        related_name='tesoureiro_solicitacao_cadastro', 
        on_delete=models.CASCADE 
    )
    
    situacao = models.CharField(
        max_length=20, 
        default="Pendente"
    )
    
    mensagem = models.TextField(
        max_length=200,
        blank=True, 
        null=True,
        validators=[
            MaxLengthValidator(200),
            MinLengthValidator(5)
        ]
    )
    
    horario = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return "Solicitação de" + self.nome
