from rolepermissions.roles import AbstractUserRole

class TesoureiroSedeRole(AbstractUserRole):
    available_permissions = {
        'autorizar_solicitacao': True,
        'negar_solicitacao': True,
    }
