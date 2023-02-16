from django.db import models


class Relatorio(models.Model):
    """
    Modelo base para relatórios.
    """
    def __str__(self):
        """
        Retorna a representação do objeto em forma de string.
        """
        return f"Relatório {self}"

    def baixar(self):
        """
        Baixa o relatório.
        """
        return self

    def enviar(self):
        """
        Envia o relatório por e-mail.
        """
        return self

    def filtrar(self):
        """
        Filtra o relatório por período.
        """
        return self
    
    
class RelatorioGeral(Relatorio):
    """
    Modelo para relatório geral de entrada e saída de caixa.
    """
    
    # relação de composição com a classe Entradas
    
    data_inicio = models.DateField(
        blank=False,
        null=False
    )

    data_fim = models.DateField(
        blank=False,
        null=False
    )

    entradas_sede = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )

    entradas_locais = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )

    entradas_missoes = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )
    
    saidas_sede = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    saidas_locais = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    pgto_obreiros = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    inss = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    aluguel_obreiros = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    construcoes = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    assis_social = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    
    saldo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False
    )


    def __str__(self):
        """
        Retorna a representação do objeto em forma de string.
        """
        return f"Relatório: {self.data_inicio} - {self.data_fim}"

