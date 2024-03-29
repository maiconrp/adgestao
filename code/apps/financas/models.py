import uuid

from decimal import Decimal
import accounts.models
import igreja.models
from igreja.models import OfertaCulto
from django.db import models
from django.db.models import F, Q


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


    @property
    def calc_saldo(user):
        saidas = Saida.objects.filter(igreja = user.igreja)

        total_saidas = Decimal('0')  # Inicializa como um objeto Decimal

        for saida in saidas:
            total_saidas += saida.valor  # Utiliza a sintaxe de soma para Decimal

        entradas = OfertaCulto.objects.filter(igreja = user.igreja)

        total_entradas = Decimal('0')  # Inicializa como um objeto Decimal

        for entrada in entradas:
            total_entradas += entrada.total  # Utiliza a sintaxe de soma para Decimal

        saldo = total_entradas - total_saidas

        return saldo
        

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

    def __str__(self):
        return "Saída -" + self.data.strftime('%d/%m/%Y')

    def gerar_relatorio(self, **kargs):
        return "Gerar Relatorio"


class Entradas(models.Model):
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
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    status = models.CharField(
        max_length=10,
        default='Ativo'
    )

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
        default=0,
        verbose_name='Saídas Sede',
    )

    saidas_locais = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Saídas Locais',
    )

    pgto_obreiros = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Pagamento de Obreiros',
    )

    inss = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='INSS',
    )

    aluguel_obreiros = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Aluguel de Obreiros',
    )

    construcoes = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Construções',
    )

    assis_social = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Assistência Social',
    )

    tesoureiro_sede = models.ForeignKey(
        accounts.models.Usuario,
        related_name='relatorio_geral',
        on_delete=models.DO_NOTHING,
    )


    @property
    def calc_entradas_sede(self):
        mes_relatorio = self.data_inicio.month
        ano_relatorio = self.data_inicio.year
        
        entradas_mes = OfertaCulto.objects.filter(data_culto__month=mes_relatorio, data_culto__year=ano_relatorio, igreja=self.tesoureiro_sede.igreja)
        
        total_entradas = Decimal('0')

        for entradas in entradas_mes:
            total_entradas += entradas.total

        return total_entradas

    @property
    def calc_total_entradas(self):
        
        total_entradas = self.entradas_locais + self.entradas_sede

        return total_entradas

    @property
    def calc_total_saidas(self):
        
        total_saidas = self.saidas_locais + self.saidas_sede

        return total_saidas

        
    @property
    def calc_entradas_locais(self):
        mes_relatorio = self.data_inicio.month
        ano_relatorio = self.data_inicio.year
        
        entradas_mes = OfertaCulto.objects.filter(data_culto__month=mes_relatorio, data_culto__year=ano_relatorio).exclude(igreja=self.tesoureiro_sede.igreja)
        
        total_entradas = Decimal('0')

        for entradas in entradas_mes:
            total_entradas += entradas.total
        

        return total_entradas


    @property
    def calc_saidas_sede(self):
        mes_relatorio = self.data_inicio.month
        ano_relatorio = self.data_inicio.year

        saidas = Saida.objects.filter(data__month=mes_relatorio, data__year=ano_relatorio, igreja=self.tesoureiro_sede.igreja)

        total_saidas = Decimal('0')  # Inicializa como um objeto Decimal

        for saida in saidas:
            total_saidas += saida.valor  # Utiliza a sintaxe de soma para Decimal

        return total_saidas


    @property
    def calc_saidas_locais(self):
        mes_relatorio = self.data_inicio.month
        ano_relatorio = self.data_inicio.year

        saidas = Saida.objects.filter(data__month=mes_relatorio, data__year=ano_relatorio).exclude(igreja=self.tesoureiro_sede.igreja)

        total_saidas = Decimal('0')  # Inicializa como um objeto Decimal

        for saida in saidas:
            total_saidas += saida.valor  # Utiliza a sintaxe de soma para Decimal

        return total_saidas

    @property
    def calc_saldo(self):
        total_saidas = self.saidas_locais + self.saidas_sede
        total_entradas = self.entradas_locais + self.entradas_sede

        despesas = self.pgto_obreiros + self.construcoes + self.inss + self.aluguel_obreiros + self.assis_social + total_saidas


        saldo = total_entradas - despesas
        return saldo

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)


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
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    status = models.CharField(
        max_length=10,
        default='Ativo'
    )

    data_inicio = models.DateField(
        validators=[validate_data]
    )

    data_fim = models.DateField(
        validators=[validate_data]
    )


    total_entradas = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Entradas',
    )

    total_saidas = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0,
        verbose_name='Saídas',
    )

    missoes_sede = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )

    pagamento_obreiro = models.DecimalField(
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
        default=0,
        verbose_name='Saldo',
    )

    igreja = models.ForeignKey(
        igreja.models.Igreja,
        related_name='relatorio_mensal',
        on_delete=models.CASCADE,
    )


    @property
    def calc_total_entradas(self):
        mes_relatorio = self.data_inicio.month
        ano_relatorio = self.data_inicio.year
        
        ofertas_mes = OfertaCulto.objects.filter(Q(data_culto__month=mes_relatorio) & Q(data_culto__year=ano_relatorio) 
        &Q(igreja=self.igreja))
        
        total_entradas = 0

        for oferta in ofertas_mes:
            total_entradas = total_entradas + oferta.total

        return total_entradas

    @property
    def calc_saidas(self):
        mes_relatorio = self.data_inicio.month
        ano_relatorio = self.data_inicio.year

        saidas = Saida.objects.filter(data__month=mes_relatorio, data__year=ano_relatorio, igreja=self.igreja)

        total_saidas = Decimal('0')  # Inicializa como um objeto Decimal

        for saida in saidas:
            total_saidas += saida.valor  # Utiliza a sintaxe de soma para Decimal

        total_saidas = total_saidas + self.pagamento_obreiro + self.fundo_convencional + self.missoes_sede    

        return total_saidas

    @property
    def calc_saldo(self):
        saldo = self.total_entradas - self.total_saidas

        return saldo

  
    @property
    def calc_pagamento_obreiro(self):
        total_entradas = self.total_entradas
        pagamento_obreiro = Decimal(total_entradas) * Decimal('0.1')
        pagamento_obreiro = format(pagamento_obreiro, '.2f')
        return pagamento_obreiro


    @property
    def calc_missoes_sede(self):
        total_entradas = self.total_entradas
        missoes_sede = Decimal(total_entradas) * Decimal('0.1')
        missoes_sede = format(missoes_sede, '.2f')
        return missoes_sede

    
    @property
    def calc_fundo_convencional(self):
        total_entradas = self.total_entradas
        fundo_convencional = Decimal(total_entradas) * Decimal('0.05')
        fundo_convencional = format(fundo_convencional, '.2f')
        return  fundo_convencional
        

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return "Relatório Mensal - " + self.igreja.nome + " " + self.data_inicio.strftime('%d/%m/%Y')

    def baixar(self):
        return "Baixar Relatório"

    def enviar(self):
        return "Enviar Relatório"
