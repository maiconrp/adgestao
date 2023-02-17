import uuid
from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Usuario
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db.models import F

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('O CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('O CPF deve ter 11 dígitos.')
    
    # Lógica para validação do CPF
    
    # Se o CPF é inválido
    if invalid:
        raise ValidationError('CPF inválido.')

def validate_data(value):
    if value is not None:
        if not isinstance(value, str):
            value = value.strftime('%Y-%m-%d')
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValidationError('Data de nascimento inválida')


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
    )
    
    localizacao = models.CharField(
        max_length=200,    
    )
    
    saldo = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    
    pastor = models.ForeignKey(
        Usuario, 
        related_name='igreja_pastor', 
        on_delete=models.DO_NOTHING, 
    )
    
    tesoureiro = models.ForeignKey(
        Usuario, 
        related_name='igreja_tesoureiro', 
        on_delete=models.DO_NOTHING, 
    )
    
    tesoureiro_sede = models.ForeignKey(
        Usuario, 
        related_name='igreja_tesoureiro_sede', 
        on_delete=models.DO_NOTHING, 
    )
    
    
    def __str__(self):
        return self.nome

   
class Membro(User):
    """
    Classe que representa um membro da igreja.
    Herda da classe User do Django, que já possui campos básicos de usuário.
    Atributos:
        nome: Nome do membro.
        data_nasc: Data de nascimento do membro.
        sexo: Sexo do membro.
        cpf: CPF do membro.
    """
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
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['username', 'nome', 'data_nasc', 'sexo']

    def __str__(self):
        return self.nome


class Oferta(models.Model):
    """
    Classe que representa uma oferta de finança.
    Attributes:
        CULTO_CHOICE (tuple): As opções de culto.
        valor_dizimo (DecimalField): O valor do dízimo.
        valor_oferta (DecimalField): O valor da oferta.
        tipo_culto (MultiSelectField): O tipo de culto.
        validacao_pastor (BooleanField): A validação do pastor.
    """

    CULTO_CHOICE =  (
        ("N", "Normal"),
        ("C", "Ceia"),
    )
    
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    
    data_culto = models.DateField(
        validators=[validate_data]
    )
    
    valor_dizimo = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    
    valor_oferta = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    
    # função F para referenciar os campos valor_culto e valor_dizimo
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default=F('valor_culto') + F('valor_dizimo')
    )
    
    tipo_culto = MultiSelectField(
        max_length=20, 
        max_choices=1,
        choices=CULTO_CHOICE,
        
    )  
    def __str__(self):
        return "Oferta -" + self.data_culto


class Dizimo(models.Model):
    """
    Classe que representa as informações de um Dízimo no sistema de finanças.
    Atributos:
        valor_dizimo (DecimalField): o valor do dízimo doado
    """
    
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    
    data = models.DateField(
        validators=[validate_data]
    )
    
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    
    membro = models.ForeignKey(
        Membro, 
        on_delete=models.SET_DEFAULT, 
        default=None, 
        related_name='dizimos'
    )

    def __str__(self):
        return "Dizimo:" + self.membro.nome if self.membro else "Dizimo: Membro Excluido"