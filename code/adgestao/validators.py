import phonenumbers
from django.core.exceptions import ValidationError


def validate_cpf(value):
    # Lógica para validação do CPF
    if not value.isdigit():
        raise ValidationError("O CPF deve conter apenas números.")
    if len(value) != 11:
        raise ValidationError("O CPF deve ter 11 dígitos.")

    # Se o CPF é inválido
    if invalid:
        raise ValidationError("CPF inválido.")


def validate_data(value):
    if value is not None:
        if not isinstance(value, str):
            value = value.strftime("%Y-%m-%d")
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValidationError("Data de nascimento inválida")


def validate_telefone(value):
    try:
        parsed_number = phonenumbers.parse(value, "BR")
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError("Número de telefone inválido.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Número de telefone inválido.")
