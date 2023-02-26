# Pylint Report
**Total**: 

| Arquivo | Código do erro | Erro | Tipo | Local |
| ------- | ------------- | ---- | ---- | ----- |
| 1 |  E0401 |  Unable to import 'django.core.asgi' |  | [1:12](asgi.py:12) |
| 1 |  C0303 |  Trailing whitespace |  | [1:41](settings.py:41) |
| 1 |  C0303 |  Trailing whitespace |  | [1:46](settings.py:46) |
| 1 |  C0304 |  Final newline missing |  | [1:137](settings.py:137) |
| 1 |  C0410 |  Multiple imports on one line |  | [1:14](settings.py:14) |
| 1 |  C0303 |  Trailing whitespace |  | [1:24](permissions.py:24) |
| 1 |  C0303 |  Trailing whitespace |  | [1:33](permissions.py:33) |
| 1 |  C0303 |  Trailing whitespace |  | [1:42](permissions.py:42) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](permissions.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](permissions.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib.auth.models' |  | [1:2](permissions.py:2) |
| 1 |  E0401 |  Unable to import 'django.contrib.contenttypes.models' |  | [1:3](permissions.py:3) |
| 1 |  C0103 |  Method name "setUp" doesn't conform to snake_case naming style |  | [1:14](permissions.py:14) |
| 1 |  W0612 |  Unused variable 'content_type' |  | [1:56](permissions.py:56) |
| 1 |  C0412 |  Imports from package accounts are not grouped |  | [1:6](permissions.py:6) |
| 1 |  W0611 |  Unused Permission imported from django.contrib.auth.models |  | [1:2](permissions.py:2) |
| 1 |  C0303 |  Trailing whitespace |  | [1:19](validate_cpf.py:19) |
| 1 |  C0303 |  Trailing whitespace |  | [1:39](validate_cpf.py:39) |
| 1 |  C0303 |  Trailing whitespace |  | [1:46](validate_cpf.py:46) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](validate_cpf.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](validate_cpf.py:1) |
| 1 |  E0401 |  Unable to import 'django.core.exceptions' |  | [1:3](validate_cpf.py:3) |
| 1 |  C0115 |  Missing class docstring |  | [1:5](validate_cpf.py:5) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:7](validate_cpf.py:7) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:14](validate_cpf.py:14) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:21](validate_cpf.py:21) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:27](validate_cpf.py:27) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:35](validate_cpf.py:35) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:41](validate_cpf.py:41) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:47](validate_cpf.py:47) |
| 1 |  C0411 |  third party import "from django.core.exceptions import ValidationError" should be placed before "from adgestao.validators import validate_cpf" |  | [1:3](validate_cpf.py:3) |
| 1 |  C0412 |  Imports from package django are not grouped |  | [1:3](validate_cpf.py:3) |
| 1 |  C0303 |  Trailing whitespace |  | [1:7](validate_data.py:7) |
| 1 |  C0303 |  Trailing whitespace |  | [1:11](validate_data.py:11) |
| 1 |  C0301 |  Line too long |  | [1:14](validate_data.py:14) |
| 1 |  C0303 |  Trailing whitespace |  | [1:16](validate_data.py:16) |
| 1 |  C0301 |  Line too long |  | [1:19](validate_data.py:19) |
| 1 |  C0303 |  Trailing whitespace |  | [1:21](validate_data.py:21) |
| 1 |  C0301 |  Line too long |  | [1:24](validate_data.py:24) |
| 1 |  C0303 |  Trailing whitespace |  | [1:26](validate_data.py:26) |
| 1 |  C0303 |  Trailing whitespace |  | [1:27](validate_data.py:27) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](validate_data.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](validate_data.py:1) |
| 1 |  E0401 |  Unable to import 'django.core.exceptions' |  | [1:3](validate_data.py:3) |
| 1 |  C0115 |  Missing class docstring |  | [1:6](validate_data.py:6) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:8](validate_data.py:8) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:12](validate_data.py:12) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:17](validate_data.py:17) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:22](validate_data.py:22) |
| 1 |  C0411 |  third party import "from django.core.exceptions import ValidationError" should be placed before "from adgestao.validators import validate_data" |  | [1:3](validate_data.py:3) |
| 1 |  C0411 |  standard import "import datetime" should be placed before "from django.test import TestCase" |  | [1:4](validate_data.py:4) |
| 1 |  C0412 |  Imports from package django are not grouped |  | [1:3](validate_data.py:3) |
| 1 |  W0611 |  Unused import datetime |  | [1:4](validate_data.py:4) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](validate_telefone.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](validate_telefone.py:1) |
| 1 |  E0401 |  Unable to import 'django.core.exceptions' |  | [1:3](validate_telefone.py:3) |
| 1 |  C0115 |  Missing class docstring |  | [1:5](validate_telefone.py:5) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:6](validate_telefone.py:6) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:10](validate_telefone.py:10) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:15](validate_telefone.py:15) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:20](validate_telefone.py:20) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:25](validate_telefone.py:25) |
| 1 |  C0411 |  third party import "from django.core.exceptions import ValidationError" should be placed before "from adgestao.validators import validate_telefone" |  | [1:3](validate_telefone.py:3) |
| 1 |  C0412 |  Imports from package django are not grouped |  | [1:3](validate_telefone.py:3) |
| 1 |  E0401 |  Unable to import 'django.contrib' |  | [1:16](urls.py:16) |
| 1 |  E0401 |  Unable to import 'django.urls' |  | [1:17](urls.py:17) |
| 1 |  C0301 |  Line too long |  | [1:36](validators.py:36) |
| 1 |  C0301 |  Line too long |  | [1:46](validators.py:46) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](validators.py:1) |
| 1 |  E0401 |  Unable to import 'phonenumbers' |  | [1:1](validators.py:1) |
| 1 |  E0401 |  Unable to import 'django.core.exceptions' |  | [1:2](validators.py:2) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:5](validators.py:5) |
| 1 |  R1728 |  Consider using a generator instead 'sum(cpf[i] * |  | [1:18](validators.py:18) |
| 1 |  R1728 |  Consider using a generator instead 'sum(cpf[i] * |  | [1:26](validators.py:26) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:34](validators.py:34) |
| 1 |  W0707 |  Consider explicitly re-raising using 'except ValueError as exc' and 'raise ValidationError("Data inválida. Utilize o formato 'dia/mês/ano'") from exc' |  | [1:42](validators.py:42) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:48](validators.py:48) |
| 1 |  W0707 |  Consider explicitly re-raising using 'except Exception as exc' and 'raise ValidationError('Número de telefone inválido.') from exc' |  | [1:54](validators.py:54) |
| 1 |  C0411 |  standard import "import datetime" should be placed before "import phonenumbers" |  | [1:3](validators.py:3) |
| 1 |  E0401 |  Unable to import 'django.core.wsgi' |  | [1:12](wsgi.py:12) |
| 1 |  C0303 |  Trailing whitespace |  | [1:1](__init__.py:1) |
| 1 |  C0304 |  Final newline missing |  | [1:5](admin.py:5) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](admin.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib' |  | [1:1](admin.py:1) |
| 1 |  W0401 |  Wildcard import models |  | [1:2](admin.py:2) |
| 1 |  W0614 |  Unused import(s) User, EmailValidator, MaxLengthValidator, MinLengthValidator, models, Igreja, MultiSelectField, validate_cpf and validate_telefone from wildcard import of models |  | [1:2](admin.py:2) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](apps.py:1) |
| 1 |  E0401 |  Unable to import 'django.apps' |  | [1:1](apps.py:1) |
| 1 |  C0115 |  Missing class docstring |  | [1:4](apps.py:4) |
| 1 |  R0903 |  Too few public methods |  | [1:4](apps.py:4) |
| 1 |  C0303 |  Trailing whitespace |  | [1:13](forms.py:13) |
| 1 |  C0304 |  Final newline missing |  | [1:23](forms.py:23) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](forms.py:1) |
| 1 |  E0401 |  Unable to import 'django' |  | [1:1](forms.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib.auth.forms' |  | [1:2](forms.py:2) |
| 1 |  E0401 |  Unable to import 'django.core.exceptions' |  | [1:3](forms.py:3) |
| 1 |  E0401 |  Unable to import 'django.contrib.auth.models' |  | [1:5](forms.py:5) |
| 1 |  C0115 |  Missing class docstring |  | [1:7](forms.py:7) |
| 1 |  C0115 |  Missing class docstring |  | [1:10](forms.py:10) |
| 1 |  R0903 |  Too few public methods |  | [1:10](forms.py:10) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:14](forms.py:14) |
| 1 |  C0103 |  Variable name "e" doesn't conform to snake_case naming style |  | [1:15](forms.py:15) |
| 1 |  C0209 |  Formatting a regular string which could be a f-string |  | [1:17](forms.py:17) |
| 1 |  R0903 |  Too few public methods |  | [1:7](forms.py:7) |
| 1 |  C0115 |  Missing class docstring |  | [1:20](forms.py:20) |
| 1 |  C0115 |  Missing class docstring |  | [1:21](forms.py:21) |
| 1 |  R0903 |  Too few public methods |  | [1:21](forms.py:21) |
| 1 |  R0903 |  Too few public methods |  | [1:20](forms.py:20) |
| 1 |  C0411 |  third party import "from django.contrib.auth.models import User" should be placed before "from .models import Usuario" |  | [1:5](forms.py:5) |
| 1 |  W0611 |  Unused User imported from django.contrib.auth.models |  | [1:5](forms.py:5) |
| 1 |  C0303 |  Trailing whitespace |  | [1:47](models.py:47) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](models.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib.auth.models' |  | [1:1](models.py:1) |
| 1 |  E0401 |  Unable to import 'django.core.validators' |  | [1:2](models.py:2) |
| 1 |  E0401 |  Unable to import 'django.db' |  | [1:4](models.py:4) |
| 1 |  E0401 |  Unable to import 'multiselectfield' |  | [1:6](models.py:6) |
| 1 |  C0115 |  Missing class docstring |  | [1:11](models.py:11) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:48](models.py:48) |
| 1 |  R1725 |  Consider using Python 3 style super() without arguments |  | [1:50](models.py:50) |
| 1 |  W0201 |  Attribute 'username' defined outside __init__ |  | [1:49](models.py:49) |
| 1 |  C0115 |  Missing class docstring |  | [1:53](models.py:53) |
| 1 |  R0903 |  Too few public methods |  | [1:53](models.py:53) |
| 1 |  W0611 |  Unused EmailValidator imported from django.core.validators |  | [1:2](models.py:2) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](permissions.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib.auth.models' |  | [1:1](permissions.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib.contenttypes.models' |  | [1:2](permissions.py:2) |
| 1 |  C0103 |  Variable name "e" doesn't conform to snake_case naming style |  | [1:30](permissions.py:30) |
| 1 |  W0707 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao criar/recuperar grupo {grupo_nome} |  {e}' from e' raise-missing-from | [1:31](permissions.py:31) |
| 1 |  W0719 |  Raising too general exception |  Exception broad-exception-raised | [1:31](permissions.py:31) |
| 1 |  C0103 |  Variable name "e" doesn't conform to snake_case naming style |  | [1:43](permissions.py:43) |
| 1 |  W0707 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao criar/recuperar permissão {permissao_nome} |  {e}' from e' raise-missing-from | [1:44](permissions.py:44) |
| 1 |  W0719 |  Raising too general exception |  Exception broad-exception-raised | [1:44](permissions.py:44) |
| 1 |  C0103 |  Variable name "e" doesn't conform to snake_case naming style |  | [1:49](permissions.py:49) |
| 1 |  W0707 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao adicionar permissão {permissao_nome} ao grupo {grupo_nome} |  {e}' from e' raise-missing-from | [1:50](permissions.py:50) |
| 1 |  W0719 |  Raising too general exception |  Exception broad-exception-raised | [1:50](permissions.py:50) |
| 1 |  C0103 |  Variable name "e" doesn't conform to snake_case naming style |  | [1:55](permissions.py:55) |
| 1 |  W0707 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao adicionar usuário {usuario.nome} ao grupo {grupo_nome} |  {e}' from e' raise-missing-from | [1:56](permissions.py:56) |
| 1 |  W0719 |  Raising too general exception |  Exception broad-exception-raised | [1:56](permissions.py:56) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](tests.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](tests.py:1) |
| 1 |  W0611 |  Unused TestCase imported from django.test |  | [1:1](tests.py:1) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](urls.py:1) |
| 1 |  E0401 |  Unable to import 'django.urls' |  | [1:1](urls.py:1) |
| 1 |  W0401 |  Wildcard import views |  | [1:2](urls.py:2) |
| 1 |  W0614 |  Unused import(s) login_required, permission_required, HttpResponse, HttpResponseRedirect, render, reverse, UsuarioForm, set_permission, Usuario, SolicitacaoCadastro and messages from wildcard import of views |  | [1:2](urls.py:2) |
| 1 |  C0303 |  Trailing whitespace |  | [1:2](views.py:2) |
| 1 |  C0303 |  Trailing whitespace |  | [1:14](views.py:14) |
| 1 |  C0303 |  Trailing whitespace |  | [1:17](views.py:17) |
| 1 |  C0303 |  Trailing whitespace |  | [1:20](views.py:20) |
| 1 |  C0303 |  Trailing whitespace |  | [1:23](views.py:23) |
| 1 |  C0303 |  Trailing whitespace |  | [1:25](views.py:25) |
| 1 |  C0303 |  Trailing whitespace |  | [1:29](views.py:29) |
| 1 |  C0301 |  Line too long |  | [1:30](views.py:30) |
| 1 |  C0303 |  Trailing whitespace |  | [1:31](views.py:31) |
| 1 |  C0303 |  Trailing whitespace |  | [1:35](views.py:35) |
| 1 |  C0303 |  Trailing whitespace |  | [1:37](views.py:37) |
| 1 |  C0303 |  Trailing whitespace |  | [1:39](views.py:39) |
| 1 |  C0303 |  Trailing whitespace |  | [1:43](views.py:43) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](views.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib.auth.decorators' |  | [1:1](views.py:1) |
| 1 |  E0401 |  Unable to import 'django.http' |  | [1:2](views.py:2) |
| 1 |  E0401 |  Unable to import 'django.shortcuts' |  | [1:3](views.py:3) |
| 1 |  E0401 |  Unable to import 'django.contrib' |  | [1:7](views.py:7) |
| 1 |  W0612 |  Unused variable 'solicitacao' |  | [1:26](views.py:26) |
| 1 |  W0613 |  Unused argument 'request' |  | [1:46](views.py:46) |
| 1 |  W0613 |  Unused argument 'request' |  | [1:56](views.py:56) |
| 1 |  W0613 |  Unused argument 'request' |  | [1:66](views.py:66) |
| 1 |  W0613 |  Unused argument 'request' |  | [1:76](views.py:76) |
| 1 |  C0411 |  third party import "from django.contrib import messages" should be placed before "from .forms import UsuarioForm" |  | [1:7](views.py:7) |
| 1 |  W0611 |  Unused Usuario imported from models |  | [1:6](views.py:6) |
| 1 |  C0303 |  Trailing whitespace |  | [1:1](__init__.py:1) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](admin.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib' |  | [1:1](admin.py:1) |
| 1 |  W0401 |  Wildcard import models |  | [1:2](admin.py:2) |
| 1 |  W0614 |  Unused import(s) uuid, accounts, igreja, models, F, validate_cpf and validate_data from wildcard import of models |  | [1:2](admin.py:2) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](apps.py:1) |
| 1 |  E0401 |  Unable to import 'django.apps' |  | [1:1](apps.py:1) |
| 1 |  C0115 |  Missing class docstring |  | [1:4](apps.py:4) |
| 1 |  R0903 |  Too few public methods |  | [1:4](apps.py:4) |
| 1 |  C0303 |  Trailing whitespace |  | [1:80](models.py:80) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](models.py:1) |
| 1 |  E0401 |  Unable to import 'django.db' |  | [1:5](models.py:5) |
| 1 |  E0401 |  Unable to import 'django.db.models' |  | [1:6](models.py:6) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:48](models.py:48) |
| 1 |  W0613 |  Unused argument 'kargs' |  | [1:48](models.py:48) |
| 1 |  C0115 |  Missing class docstring |  | [1:52](models.py:52) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:83](models.py:83) |
| 1 |  W0613 |  Unused argument 'kargs' |  | [1:83](models.py:83) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:196](models.py:196) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:199](models.py:199) |
| 1 |  C0115 |  Missing class docstring |  | [1:203](models.py:203) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:261](models.py:261) |
| 1 |  C0116 |  Missing function or method docstring |  | [1:264](models.py:264) |
| 1 |  W0611 |  Unused validate_cpf imported from adgestao.validators |  | [1:8](models.py:8) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](tests.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](tests.py:1) |
| 1 |  W0611 |  Unused TestCase imported from django.test |  | [1:1](tests.py:1) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](views.py:1) |
| 1 |  E0401 |  Unable to import 'django.shortcuts' |  | [1:1](views.py:1) |
| 1 |  W0611 |  Unused render imported from django.shortcuts |  | [1:1](views.py:1) |
| 1 |  C0303 |  Trailing whitespace |  | [1:1](__init__.py:1) |
| 1 |  C0304 |  Final newline missing |  | [1:7](admin.py:7) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](admin.py:1) |
| 1 |  E0401 |  Unable to import 'django.contrib' |  | [1:1](admin.py:1) |
| 1 |  W0401 |  Wildcard import models |  | [1:2](admin.py:2) |
| 1 |  W0614 |  Unused import(s) uuid, models, F, MultiSelectField, validate_cpf and validate_data from wildcard import of models |  | [1:2](admin.py:2) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](apps.py:1) |
| 1 |  E0401 |  Unable to import 'django.apps' |  | [1:1](apps.py:1) |
| 1 |  C0115 |  Missing class docstring |  | [1:4](apps.py:4) |
| 1 |  R0903 |  Too few public methods |  | [1:4](apps.py:4) |
| 1 |  C0303 |  Trailing whitespace |  | [1:37](models.py:37) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](models.py:1) |
| 1 |  E0401 |  Unable to import 'django.db' |  | [1:3](models.py:3) |
| 1 |  E0401 |  Unable to import 'django.db.models' |  | [1:4](models.py:4) |
| 1 |  E0401 |  Unable to import 'multiselectfield' |  | [1:5](models.py:5) |
| 1 |  R0903 |  Too few public methods |  | [1:10](models.py:10) |
| 1 |  R0903 |  Too few public methods |  | [1:44](models.py:44) |
| 1 |  R0903 |  Too few public methods |  | [1:90](models.py:90) |
| 1 |  R0903 |  Too few public methods |  | [1:144](models.py:144) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](tests.py:1) |
| 1 |  E0401 |  Unable to import 'django.test' |  | [1:1](tests.py:1) |
| 1 |  W0611 |  Unused TestCase imported from django.test |  | [1:1](tests.py:1) |
| 1 |  C0114 |  Missing module docstring |  | [1:1](views.py:1) |
| 1 |  E0401 |  Unable to import 'django.shortcuts' |  | [1:1](views.py:1) |
| 1 |  W0611 |  Unused render imported from django.shortcuts |  | [1:1](views.py:1) |
| 1 |  C0415 |  Import outside toplevel |  | [1:11](manage.py:11) |

**Total**: 226
