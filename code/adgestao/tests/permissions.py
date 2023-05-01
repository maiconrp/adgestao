from django.test import TestCase
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Usuario
from igreja.models import Igreja
from accounts.permissions import set_permission


class SetPermissionTestCase(TestCase):
    """
    Teste para a função de permissões `set_permission`.
    """

    def setUp(self):
        """
        Configura os dados iniciais do teste.
        """
        # Cria uma Igreja para os usuários
        self.igreja, self._ = Igreja.objects.get_or_create(
            nome="Igreja Teste",
            localizacao="Local de teste",
            saldo=0
        )
        
        # Cria um usuário Tesoureiro Sede
        self.usuario_ts, self._ = Usuario.objects.get_or_create(
            nome='Tesoureiro Sede',
            cpf='12345678901',
            telefone='00000000000',
            funcao='TS',
            igreja=self.igreja,
        )
        
        # Cria um usuário Tesoureiro
        self.usuario_t, self._  = Usuario.objects.get_or_create(
            nome='Tesoureiro',
            cpf='23456789012',
            telefone='00000000000',
            funcao='T',
            igreja=self.igreja,
        )
        
        # Cria um usuário Pastor
        self.usuario_p, self._  = Usuario.objects.get_or_create(
            nome='Pastor',
            cpf='34567890123',
            telefone='00000000000',
            funcao='P',
            igreja=self.igreja,
        )

    def test_set_permission(self):
        """
        Testa a função de permissões `set_permission`.
        """

        # Define as permissões do usuário Tesoureiro Sede
        usuario_ts = set_permission(self.usuario_ts)
        self.assertTrue(usuario_ts.has_perm('accounts.tesoureiro_sede'))
        self.assertFalse(usuario_ts.has_perm('accounts.tesoureiro'))
        self.assertFalse(usuario_ts.has_perm('accounts.pastor'))

        # Define as permissões do usuário Tesoureiro
        usuario_t = set_permission(self.usuario_t)
        self.assertTrue(usuario_t.has_perm('accounts.tesoureiro'))
        self.assertFalse(usuario_t.has_perm('accounts.tesoureiro_sede'))
        self.assertFalse(usuario_t.has_perm('accounts.pastor'))

        # Define as permissões do usuário Pastor
        usuario_p = set_permission(self.usuario_p)
        self.assertTrue(usuario_p.has_perm('accounts.pastor'))
        self.assertFalse(usuario_t.has_perm('accounts.tesoureiro_sede'))
        self.assertFalse(usuario_p.has_perm('accounts.tesoureiro'))
