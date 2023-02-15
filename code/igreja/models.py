from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class Igreja(models.Model):
    """
    Classe que representa uma igreja.

    Atributos:
        id: Identificador da igreja.
        nome: Nome da igreja.
        localizacao: Localização da igreja.
        saldo: Saldo financeiro da igreja.
    """
    id = models.CharField(
        max_length=5, 
        unique=True, 
        primary_key=True,
        blank=False, 
        null=False,
    )
    nome = models.CharField(
        max_length=100,
        blank=False, 
        null=False,
    )
    localizacao = models.CharField(
        max_length=200,
        blank=False, 
        null=False,
    )
    saldo = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )


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
        blank=False, 
        null=False,
    )
    data_nasc = models.DateField(      
        blank=False, 
        null=False,
    )
    sexo = MultiSelectField(
        max_length=20, 
        max_choices=1,
        choices=SEXO_CHOICES,
        blank=False, 
        null=False,
    )
    cpf = models.CharField(
        max_length=13, 
        unique=True, 
        primary_key=True,
        blank=False, 
        null=False,
    )


class Financa(models.Model):
    """
    Classe que representa uma finança.

    Attributes:
        id (str): O ID da finança.
        data (DateField): A data da finança.
    """

    id = models.CharField(
        max_length=5, 
        unique=True, 
        primary_key=True,
        blank=False, 
        null=False,
    )
    data = models.DateField(      
        blank=False, 
        null=False,
    )

    def gerarRelatorio(self, **keyargs):
        """
        Gera um relatório de finanças.

        Args:
            **keyargs: Argumentos adicionais.

        Returns:
            str: O relatório gerado.
        """
        pass

    def adicionar(self, ):
        """
        Adiciona uma finança.

        Returns:
            None
        """
        pass

    def editar(self, id):
        """
        Edita uma finança.

        Args:
            id (str): O ID da finança a ser editada.

        Returns:
            None
        """
        pass

    def excluir(self, id):
        """
        Exclui uma finança.

        Args:
            id (str): O ID da finança a ser excluída.

        Returns:
            None
        """
        pass

    def visualizar(self, **keyargs):
        """
        Visualiza uma finança.

        Args:
            **keyargs: Argumentos adicionais.

        Returns:
            None
        """
        pass


class Saida(Financa):
    """
    Classe que representa uma saída de finança.

    Attributes:
        descricao (str): A descrição da saída.
        valor (DecimalField): O valor da saída.
    """

    descricao = models.TextField(
        max_length=200, 
        blank= True,
        null= True,
        default=None
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )

  
class Oferta(Financa):
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
        ("E", "EBD"),
        ("N", "Normal"),
        ("C", "Ceia"),
    )

    valor_dizimo = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    valor_oferta = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    tipo_culto = MultiSelectField(
        max_length=20, 
        max_choices=1,
        choices=CULTO_CHOICE,
        blank=False, 
        null=False,
    )
    validacao_pastor = models.BooleanField(
        default=False
    )     
  
   
class Dizimo(Financa):
    """
    Classe que representa as informações de um Dízimo no sistema de finanças.

    Atributos:
        valor_dizimo (DecimalField): o valor do dízimo doado
    """

    valor_dizimo = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )