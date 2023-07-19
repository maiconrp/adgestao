import uuid

from django.db import models
from django.db.models import F
from multiselectfield import MultiSelectField

from adgestao.validators import validate_cpf, validate_data


class Igreja(models.Model):
    """
    Classe que representa uma igreja.
    Atributos:
        id: Identificador da igreja.
        nome: Nome da igreja.
        localizacao: Localização da igreja.
        saldo: Saldo financeiro da igreja.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    nome = models.CharField(
        max_length=100,
        unique=True
    )

    localizacao = models.CharField(
        max_length=200,
    )

    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=3
    )
    
    REQUIRED_FIELDS = ['nome', 'localização']

    def __str__(self):
        return self.nome


class Membro(models.Model):
    """
    Classe que representa um membro da igreja.
    Herda da classe User do Django, que já possui campos básicos de usuário.
    Atributos:
        nome: Nome do membro.
        data_nasc: Data de nascimento do membro.
        sexo: Sexo do membro.
        cpf: CPF do membro.
    """

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("I", "Indefinido"),
    )
    

    nome = models.CharField(
        max_length=100,
    )

    data_nasc = models.DateField(
        validators=[validate_data]
    )

    sexo = MultiSelectField(
        choices=SEXO_CHOICES,
        max_length=20,
        max_choices=1,
    )

    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        validators=[validate_cpf]
    )

    igreja = models.ForeignKey(
        Igreja,
        related_name='membros',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nome


class Dizimo(models.Model):
    """
    Classe que representa as informações de um Dízimo no sistema de finanças.
    Atributos:
        valor_dizimo (DecimalField): o valor do dízimo doado
    """

    CULTO_CHOICE = (
        ("N", "Normal"),
        ("C", "Ceia"),
        ("M", "Missões"),
    )

    tipo_culto = MultiSelectField(
        max_length=20,
        max_choices=1,
        choices=CULTO_CHOICE,
    )

    data_culto = models.DateField(
        validators=[validate_data]
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    igreja = models.ForeignKey(
        Igreja,
        related_name='dizimos',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=3,
       
    )

    membro = models.ForeignKey(
        Membro,
        on_delete=models.SET_DEFAULT,
        default=None,
        related_name='dizimos'
    )

    def __str__(self):
        return "Dizimo:" + self.membro.nome if self.membro else "Dizimo: Membro Excluido"



class OfertaCulto(models.Model):
    """
    Classe que representa uma oferta de finança.
    Attributes:
        CULTO_CHOICE (tuple): As opções de culto.
        valor_dizimo (DecimalField): O valor do dízimo.
        valor_oferta (DecimalField): O valor da oferta.
        tipo_culto (MultiSelectField): O tipo de culto.
        validacao_pastor (BooleanField): A validação do pastor.
    """

    CULTO_CHOICE = (
        ("N", "Normal"),
        ("C", "Ceia"),
        ("M", "Missões"),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    igreja = models.ForeignKey(
        Igreja,
        related_name='ofertas_culto',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    data_culto = models.DateField(
        validators=[validate_data]
    )

    valor_dizimo = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )

    valor_oferta = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )


    total = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        null=True
    )

    tipo_culto = MultiSelectField(
        max_length=20,
        max_choices=1,
        choices=CULTO_CHOICE,
    )

    def save(self, *args, **kwargs):
        self.total = self.valor_oferta + self.valor_dizimo
        super().save(*args, **kwargs)

    def __str__(self):
        return "Oferta -" + self.data_culto.strftime('%d/%m/%Y')