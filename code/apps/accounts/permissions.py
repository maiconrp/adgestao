from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Usuario

# Obtém o content_type para o model Usuario


def set_permission(usuario):
    """
    Função que define as permissões e grupo de usuário com base na função.

    Args:
        usuario (Usuario): objeto do modelo Usuario.

    Returns:
        Usuario: objeto do modelo Usuario atualizado com as permissões e grupo definidos.
    """
    content_type = ContentType.objects.get_for_model(Usuario)

    # Define o nome do grupo a partir da função do usuário
    permissoes = {
        'TS': 'tesoureiro_sede',
        'T': 'tesoureiro',
        'P': 'pastor',
    }
    permissao_codenome = permissoes.get(''.join(usuario.funcao), 'default')


    # Define o nome da permissão a partir da função do usuário
    permissao_nome = permissao_codenome.replace("_", " ").title()

    # Cria ou recupera a permissão
    try:
        permission, _ = Permission.objects.get_or_create(
            codename=permissao_codenome,
            name=permissao_nome,
            content_type=content_type
        )
    except Exception as e:
        raise Exception(f"Erro ao criar/recuperar permissão {permissao_nome}: {e}")

    # Adiciona a permissão ao usuario
    try:
        usuario.user_permissions.add(permission)
    except Exception as e:
        raise Exception(f"Erro ao adicionar permissão {permissao_nome} ao usuário {usuario.nome}: {e}")

    return usuario
