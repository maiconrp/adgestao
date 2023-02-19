from django.test import TestCase
from adgestao.validators import validate_data
from django.core.exceptions import ValidationError
import datetime

class TestValidatorData(TestCase):
    
    def test_data_valida(self):
        data = "24/02/2005"
        validate_data(data)
    
    def test_data_incompleta(self):
        data = "24/02/200"
        with self.assertRaisesMessage(ValidationError, "Data inválida. Utilize o formato 'dia/mês/ano'"):
            validate_data(data)
    
    def test_data_ordem_errada(self):
        data = "2005/02/24"
        with self.assertRaisesMessage(ValidationError, "Data inválida. Utilize o formato 'dia/mês/ano'"):
            validate_data(data)
        
    def test_data_caracteres_errados(self):
        data = "2005-02-24"
        with self.assertRaisesMessage(ValidationError, "Data inválida. Utilize o formato 'dia/mês/ano'"):
            validate_data(data)
    
    
