from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    cpf = models.CharField(max_length=13, unique=True, primarykey=True)
    telefone = models.CharField(max_length=20)
    igreja = models.ForeignKey(
        Igreja,
        on_delete=models.D0_NOTHING,
        related_name='Usuario'
    )
    
    def __str__(self):
        return self.username

class TesoureiroLocal(Usuario):


    def queijo(self):
        pass
    

class TesoureiroSede(Usuario):


    def ela(self):
        pass


class Pastor(Usuario):


    def muie_dos_outro(self):
        pass
    



