from django.test import TestCase
from adgestao.validators import validate_cpf
from django.core.exceptions import ValidationError

class TestValidatorCpf(TestCase):

    def test_validate_cpf_cpf_valido(self):
        # Arrange
        cpf = "12345678901"
        with self.assertRaisesMessage(ValidationError, "CPF inválido."):
            validate_cpf(cpf)


    def test_validate_cpf_cpf_com_menos_de_11_digitos(self):
        # Arrange
        cpf = "1234567890"
        with self.assertRaisesMessage(ValidationError, "O CPF deve ter 11 dígitos."):
            validate_cpf(cpf)
        

    def test_validate_cpf_cpf_com_mais_de_11_digitos(self):
        # Arrange
        cpf = "1234567890123"
        with self.assertRaisesMessage(ValidationError, "O CPF deve ter 11 dígitos."):
            validate_cpf(cpf)

    def test_validate_cpf_cpf_com_digitos_iguais(self):
        # Arrange
        cpf = "11111111111"

        # Act and Assert
        with self.assertRaisesMessage(ValidationError, "CPF inválido."):
            validate_cpf(cpf)

    def test_validate_cpf_cpf_com_primeiro_digito_verificador_incorreto(self):
        # Arrange
        cpf = "12345678900"
        with self.assertRaisesMessage(ValidationError, "CPF inválido."):
            validate_cpf(cpf)   

    def test_validate_cpf_cpf_com_segundo_digito_verificador_incorreto(self):
        # Arrange
        cpf = "12345678903"
        with self.assertRaisesMessage(ValidationError, "CPF inválido."):
            validate_cpf(cpf)
            
    def test_validate_cpf_cpf_com_digitos_nao_numericos(self):
        # Arrange
        cpf = "a2345678901"
        with self.assertRaisesMessage(ValidationError, "O CPF deve conter apenas números."):
            validate_cpf(cpf)
