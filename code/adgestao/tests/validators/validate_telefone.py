from django.test import TestCase
from adgestao.validators import validate_telefone
from django.core.exceptions import ValidationError

class TestValidateTelefone(TestCase):
    def test_validate_telefone_valido(self):
        telefone = "+5511987654321"
        validate_telefone(telefone)

    def test_validate_telefone_nao_numerico(self):
        telefone = "abcd"
        with self.assertRaisesMessage(ValidationError, "Número de telefone inválido."):
            validate_telefone(telefone)

    def test_validate_telefone_incompleto(self):
        telefone = "+5511"
        with self.assertRaisesMessage(ValidationError, "Número de telefone inválido."):
            validate_telefone(telefone)

    def test_validate_telefone_tamanho_maximo(self):
        telefone = "+5511987654321123456"
        with self.assertRaisesMessage(ValidationError, "Número de telefone inválido."):
            validate_telefone(telefone)

    def test_validate_telefone_prefixo_invalido(self):
        telefone = "+550011987654321"
        with self.assertRaisesMessage(ValidationError, "Número de telefone inválido."):
            validate_telefone(telefone)
