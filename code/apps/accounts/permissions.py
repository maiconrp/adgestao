from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import Usuario

# Obtém o content_type para o model Usuario
content_type = ContentType.objects.get_for_model(Usuario)


def set_permission(usuario):
    """
    Função que define as permissões e grupo de usuário com base na função.

    Args:
        usuario (Usuario): objeto do modelo Usuario.

    Returns:
        Usuario: objeto do modelo Usuario atualizado com as permissões e grupo definidos.
    """
    # Define o nome do grupo a partir da função do usuário
    funcao_para_grupo = {
        'TS': 'tesoureiro_sede',
        'T': 'tesoureiro',
        'P': 'pastor',
    }
    grupo_nome = funcao_para_grupo.get(usuario.funcao, 'default')

    # Cria ou recupera o grupo
    try:
        grupo, _ = Group.objects.get_or_create(name=grupo_nome)
    except Exception as e:
        raise Exception(f"Erro ao criar/recuperar grupo {grupo_nome}: {e}")

    # Define o nome da permissão a partir da função do usuário
    permissao_nome = grupo_nome.replace("_", " ").title()

    # Cria ou recupera a permissão
    try:
        permission, _ = Permission.objects.get_or_create(
            codename=grupo_nome,
            name=permissao_nome,
            content_type=content_type,
        )
    except Exception as e:
        raise Exception(f"Erro ao criar/recuperar permissão {permissao_nome}: {e}")

    # Adiciona a permissão ao grupo
    try:
        grupo.permissions.add(permission)
    except Exception as e:
        raise Exception(f"Erro ao adicionar permissão {permissao_nome} ao grupo {grupo_nome}: {e}")

    # Adiciona o usuário ao grupo
    try:
        usuario.groups.add(grupo)
    except Exception as e:
        raise Exception(f"Erro ao adicionar usuário {usuario.nome} ao grupo {grupo_nome}: {e}")

    return usuario
