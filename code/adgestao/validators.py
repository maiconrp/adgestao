import phonenumbers
from django.core.exceptions import ValidationError
import datetime

def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError("O CPF deve conter apenas números.")
    if len(value) != 11:
        raise ValidationError("O CPF deve ter 11 dígitos.")

    cpf = [int(d) for d in value]

    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        raise ValidationError("CPF inválido.")

    # Verifica o primeiro dígito verificador
    soma = sum([cpf[i] * (10 - i) for i in range(9)])
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != cpf[9]:
        raise ValidationError("CPF inválido.")

    # Verifica o segundo dígito verificador
    soma = sum([cpf[i] * (11 - i) for i in range(10)])
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != cpf[10]:
        raise ValidationError("CPF inválido.")


import datetime

def validate_data(date):
    if isinstance(date, str):
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            raise ValidationError("Data inválida. Utilize o formato 'dia/mês/ano'")

        # Verificar se o ano está entre 1900 e o ano atual
        day, month, year = map(int, date.split('/'))
        if year < 1900 or year > datetime.datetime.now().year:
            raise ValidationError(f"Data inválida. Insira um ano entre 1900 e {datetime.datetime.now().year}")

    if isinstance(date, datetime.datetime):
        if date.year < 1900 or date.year > datetime.datetime.now().year:
            raise ValidationError(f"Data inválida. Insira um ano entre 1900 e {datetime.datetime.now().year}")


def validate_telefone(value):
    try:
        parsed_number = phonenumbers.parse(value, "BR")
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError("Número de telefone inválido.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Número de telefone inválido.")
