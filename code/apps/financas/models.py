import uuid

import accounts.models
import igreja.models
from django.db import models
from django.db.models import F

from adgestao.validators import validate_cpf, validate_data


class Saida(models.Model):
    """
    Classe que representa uma saída de finança.
    Attributes:
        descricao (str): A descrição da saída.
        valor (DecimalField): O valor da saída.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    data = models.DateField(
        # validators=[validate_data]
    )

    descricao = models.TextField(
        max_length=200,
    )

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=3
    )

    igreja = models.ForeignKey(
        igreja.models.Igreja,
        related_name='saidas',
        on_delete=models.CASCADE,
    )

    REQUIRED_FIELDS = ['descricao', 'data', 'valor', 'igreja']

    def __str__(self):
        return "Saída -" + self.data.strftime('%d/%m/%Y')

    def gerar_relatorio(self, **kargs):
        return "Gerar Relatorio"


class Entrada(models.Model):
    ofertas = models.ManyToManyField(
        igreja.models.OfertaCulto,
        related_name="entradas_ofertas",
        blank=True
    )

    dizimos = models.ManyToManyField(
        igreja.models.Dizimo,
        related_name="entradas_dizimos",
        blank=True
    )

    igreja = models.ForeignKey(
        igreja.models.Igreja,
        related_name='entradas',
        on_delete=models.CASCADE,
    )

  
    def save(self, *args, **kwargs):
            is_new_instance = not self.pk
            super().save(*args, **kwargs)
            if is_new_instance:
                self.ofertas.set([])
                self.dizimos.set([])       

    def __str__(self):
        return f"Entrada - {self.igreja.nome} - {self.igreja.pk}" 
    # + self.data.strftime('%d/%m/%Y')

    def gerar_relatorio(self, **kargs):
        return "Gerar Relatorio"


class RelatorioGeral(models.Model):
    """
    Modelo para relatório geral de entrada e saída de caixa.
    """

    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Saldo',
    )

    data_inicio = models.DateField(
        validators=[validate_data]
    )

    data_fim = models.DateField(
        validators=[validate_data]
    )

    entradas_sede = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Entradas Sede',
    )

    entradas_locais = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Entradas Locais',
    )

    entradas_missoes = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Entradas Missões',
    )

    saidas_sede = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='Saídas Sede',
    )

    saidas_locais = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='Saídas Locais',
    )

    pgto_obreiros = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='Pagamento de Obreiros',
    )

    inss = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='INSS',
    )

    aluguel_obreiros = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='Aluguel de Obreiros',
    )

    construcoes = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='Construções',
    )

    assis_social = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True,
        verbose_name='Assistência Social',
    )

    tesoureiro_sede = models.ForeignKey(
        accounts.models.Usuario,
        related_name='relatorio_geral',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        """
        Retorna a representação do objeto em forma de string.
        """
        return f"Relatório: {self.data_inicio} - {self.data_fim}"

    def baixar(self):
        return "Baixar Relatório"

    def enviar(self):
        return "Enviar Relatório"


class RelatorioMensal(models.Model):

    data_inicio = models.DateField(
        validators=[validate_data]
    )

    data_fim = models.CharField(
        max_length=10,
        default='2023-00-00'
    )

    entradas = models.ForeignKey(
        Entrada,
        related_name='relatorio_mensal_entradas',
        on_delete=models.CASCADE,
    )


    pagamento_obreiro = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )

    missoes_sede = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )

    fundo_convencional = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0

    )

    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
        
    )

    igreja = models.ForeignKey(
        igreja.models.Igreja,
        related_name='relatorio_mensal',
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return "Relatório Mensal - " + self.igreja.nome + " " + self.data_inicio.strftime('%d/%m/%Y')

    def baixar(self):
        return "Baixar Relatório"

    def enviar(self):
        return "Enviar Relatório"
