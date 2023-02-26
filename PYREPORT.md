# Pylint Report

**Total**: 274
| ID | Arquivo | Linha | Erro | Cod | Tipo |
| -- | ------- | ----- | ---- | --- | ---- |
| 0 | [asgi.py](code/adgestao/asgi.py#L12) | 12 |  Unable to import 'django.core.asgi' (import-error) |  E0401 | import-error |
| 1 | [settings.py](code/adgestao/settings.py#L41) | 41 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 2 | [settings.py](code/adgestao/settings.py#L46) | 46 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 3 | [settings.py](code/adgestao/settings.py#L137) | 137 |  Final newline missing (missing-final-newline) |  C0304 | missing-final-newline |
| 4 | [settings.py](code/adgestao/settings.py#L14) | 14 |  Multiple imports on one line (os, sys) (multiple-imports) |  C0410 | multiple-imports |
| 5 | [permissions.py](code/adgestao/tests/permissions.py#L24) | 24 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 6 | [permissions.py](code/adgestao/tests/permissions.py#L33) | 33 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 7 | [permissions.py](code/adgestao/tests/permissions.py#L42) | 42 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 8 | [permissions.py](code/adgestao/tests/permissions.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 9 | [permissions.py](code/adgestao/tests/permissions.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 10 | [permissions.py](code/adgestao/tests/permissions.py#L2) | 2 |  Unable to import 'django.contrib.auth.models' (import-error) |  E0401 | import-error |
| 11 | [permissions.py](code/adgestao/tests/permissions.py#L3) | 3 |  Unable to import 'django.contrib.contenttypes.models' (import-error) |  E0401 | import-error |
| 12 | [permissions.py](code/adgestao/tests/permissions.py#L14) | 14 |  Method name "setUp" doesn't conform to snake_case naming style (invalid-name) |  C0103 | invalid-name |
| 13 | [permissions.py](code/adgestao/tests/permissions.py#L56) | 56 |  Unused variable 'content_type' (unused-variable) |  W0612 | unused-variable |
| 14 | [permissions.py](code/adgestao/tests/permissions.py#L6) | 6 |  Imports from package accounts are not grouped (ungrouped-imports) |  C0412 | ungrouped-imports |
| 15 | [permissions.py](code/adgestao/tests/permissions.py#L2) | 2 |  Unused Permission imported from django.contrib.auth.models (unused-import) |  W0611 | unused-import |
| 16 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L19) | 19 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 17 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L39) | 39 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 18 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L46) | 46 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 19 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 20 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 21 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L3) | 3 |  Unable to import 'django.core.exceptions' (import-error) |  E0401 | import-error |
| 22 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L5) | 5 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 23 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L7) | 7 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 24 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L14) | 14 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 25 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L21) | 21 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 26 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L27) | 27 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 27 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L35) | 35 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 28 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L41) | 41 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 29 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L47) | 47 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 30 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L3) | 3 |  third party import "from django.core.exceptions import ValidationError" should be placed before "from adgestao.validators import validate_cpf" (wrong-import-order) |  C0411 | wrong-import-order |
| 31 | [validate_cpf.py](code/adgestao/tests/validators/validate_cpf.py#L3) | 3 |  Imports from package django are not grouped (ungrouped-imports) |  C0412 | ungrouped-imports |
| 32 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L7) | 7 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 33 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L11) | 11 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 34 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L14) | 14 |  Line too long (105/100) (line-too-long) |  C0301 | line-too-long |
| 35 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L16) | 16 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 36 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L19) | 19 |  Line too long (105/100) (line-too-long) |  C0301 | line-too-long |
| 37 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L21) | 21 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 38 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L24) | 24 |  Line too long (105/100) (line-too-long) |  C0301 | line-too-long |
| 39 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L26) | 26 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 40 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L27) | 27 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 41 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 42 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 43 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L3) | 3 |  Unable to import 'django.core.exceptions' (import-error) |  E0401 | import-error |
| 44 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L6) | 6 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 45 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L8) | 8 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 46 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L12) | 12 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 47 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L17) | 17 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 48 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L22) | 22 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 49 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L3) | 3 |  third party import "from django.core.exceptions import ValidationError" should be placed before "from adgestao.validators import validate_data" (wrong-import-order) |  C0411 | wrong-import-order |
| 50 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L4) | 4 |  standard import "import datetime" should be placed before "from django.test import TestCase" (wrong-import-order) |  C0411 | wrong-import-order |
| 51 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L3) | 3 |  Imports from package django are not grouped (ungrouped-imports) |  C0412 | ungrouped-imports |
| 52 | [validate_data.py](code/adgestao/tests/validators/validate_data.py#L4) | 4 |  Unused import datetime (unused-import) |  W0611 | unused-import |
| 53 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 54 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 55 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L3) | 3 |  Unable to import 'django.core.exceptions' (import-error) |  E0401 | import-error |
| 56 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L5) | 5 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 57 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L6) | 6 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 58 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L10) | 10 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 59 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L15) | 15 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 60 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L20) | 20 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 61 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L25) | 25 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 62 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L3) | 3 |  third party import "from django.core.exceptions import ValidationError" should be placed before "from adgestao.validators import validate_telefone" (wrong-import-order) |  C0411 | wrong-import-order |
| 63 | [validate_telefone.py](code/adgestao/tests/validators/validate_telefone.py#L3) | 3 |  Imports from package django are not grouped (ungrouped-imports) |  C0412 | ungrouped-imports |
| 64 | [urls.py](code/adgestao/urls.py#L16) | 16 |  Unable to import 'django.contrib' (import-error) |  E0401 | import-error |
| 65 | [urls.py](code/adgestao/urls.py#L17) | 17 |  Unable to import 'django.urls' (import-error) |  E0401 | import-error |
| 66 | [validators.py](code/adgestao/validators.py#L36) | 36 |  Line too long (115/100) (line-too-long) |  C0301 | line-too-long |
| 67 | [validators.py](code/adgestao/validators.py#L46) | 46 |  Line too long (109/100) (line-too-long) |  C0301 | line-too-long |
| 68 | [validators.py](code/adgestao/validators.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 69 | [validators.py](code/adgestao/validators.py#L1) | 1 |  Unable to import 'phonenumbers' (import-error) |  E0401 | import-error |
| 70 | [validators.py](code/adgestao/validators.py#L2) | 2 |  Unable to import 'django.core.exceptions' (import-error) |  E0401 | import-error |
| 71 | [validators.py](code/adgestao/validators.py#L5) | 5 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 72 | [validators.py](code/adgestao/validators.py#L18) | 18 |  Consider using a generator instead 'sum(cpf[i] * (10 - i) for i in range(9))' (consider-using-generator) |  R1728 | consider-using-generator |
| 73 | [validators.py](code/adgestao/validators.py#L26) | 26 |  Consider using a generator instead 'sum(cpf[i] * (11 - i) for i in range(10))' (consider-using-generator) |  R1728 | consider-using-generator |
| 74 | [validators.py](code/adgestao/validators.py#L34) | 34 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 75 | [validators.py](code/adgestao/validators.py#L42) | 42 |  Consider explicitly re-raising using 'except ValueError as exc' and 'raise ValidationError("Data inválida. Utilize o formato 'dia/mês/ano'") from exc' (raise-missing-from) |  W0707 | raise-missing-from |
| 76 | [validators.py](code/adgestao/validators.py#L48) | 48 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 77 | [validators.py](code/adgestao/validators.py#L54) | 54 |  Consider explicitly re-raising using 'except Exception as exc' and 'raise ValidationError('Número de telefone inválido.') from exc' (raise-missing-from) |  W0707 | raise-missing-from |
| 78 | [validators.py](code/adgestao/validators.py#L3) | 3 |  standard import "import datetime" should be placed before "import phonenumbers" (wrong-import-order) |  C0411 | wrong-import-order |
| 79 | [wsgi.py](code/adgestao/wsgi.py#L12) | 12 |  Unable to import 'django.core.wsgi' (import-error) |  E0401 | import-error |
| 80 | [__init__.py](code/apps/accounts/__init__.py#L1) | 1 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 81 | [admin.py](code/apps/accounts/admin.py#L5) | 5 |  Final newline missing (missing-final-newline) |  C0304 | missing-final-newline |
| 82 | [admin.py](code/apps/accounts/admin.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 83 | [admin.py](code/apps/accounts/admin.py#L1) | 1 |  Unable to import 'django.contrib' (import-error) |  E0401 | import-error |
| 84 | [admin.py](code/apps/accounts/admin.py#L2) | 2 |  Wildcard import models (wildcard-import) |  W0401 | wildcard-import |
| 85 | [admin.py](code/apps/accounts/admin.py#L2) | 2 |  Unused import(s) User, EmailValidator, MaxLengthValidator, MinLengthValidator, models, Igreja, MultiSelectField, validate_cpf and validate_telefone from wildcard import of models (unused-wildcard-import) |  W0614 | unused-wildcard-import |
| 86 | [apps.py](code/apps/accounts/apps.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 87 | [apps.py](code/apps/accounts/apps.py#L1) | 1 |  Unable to import 'django.apps' (import-error) |  E0401 | import-error |
| 88 | [apps.py](code/apps/accounts/apps.py#L4) | 4 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 89 | [apps.py](code/apps/accounts/apps.py#L4) | 4 |  Too few public methods (0/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 90 | [forms.py](code/apps/accounts/forms.py#L13) | 13 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 91 | [forms.py](code/apps/accounts/forms.py#L23) | 23 |  Final newline missing (missing-final-newline) |  C0304 | missing-final-newline |
| 92 | [forms.py](code/apps/accounts/forms.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 93 | [forms.py](code/apps/accounts/forms.py#L1) | 1 |  Unable to import 'django' (import-error) |  E0401 | import-error |
| 94 | [forms.py](code/apps/accounts/forms.py#L2) | 2 |  Unable to import 'django.contrib.auth.forms' (import-error) |  E0401 | import-error |
| 95 | [forms.py](code/apps/accounts/forms.py#L3) | 3 |  Unable to import 'django.core.exceptions' (import-error) |  E0401 | import-error |
| 96 | [forms.py](code/apps/accounts/forms.py#L5) | 5 |  Unable to import 'django.contrib.auth.models' (import-error) |  E0401 | import-error |
| 97 | [forms.py](code/apps/accounts/forms.py#L7) | 7 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 98 | [forms.py](code/apps/accounts/forms.py#L10) | 10 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 99 | [forms.py](code/apps/accounts/forms.py#L10) | 10 |  Too few public methods (0/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 100 | [forms.py](code/apps/accounts/forms.py#L14) | 14 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 101 | [forms.py](code/apps/accounts/forms.py#L15) | 15 |  Variable name "e" doesn't conform to snake_case naming style (invalid-name) |  C0103 | invalid-name |
| 102 | [forms.py](code/apps/accounts/forms.py#L17) | 17 |  Formatting a regular string which could be a f-string (consider-using-f-string) |  C0209 | consider-using-f-string |
| 103 | [forms.py](code/apps/accounts/forms.py#L7) | 7 |  Too few public methods (1/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 104 | [forms.py](code/apps/accounts/forms.py#L20) | 20 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 105 | [forms.py](code/apps/accounts/forms.py#L21) | 21 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 106 | [forms.py](code/apps/accounts/forms.py#L21) | 21 |  Too few public methods (0/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 107 | [forms.py](code/apps/accounts/forms.py#L20) | 20 |  Too few public methods (0/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 108 | [forms.py](code/apps/accounts/forms.py#L5) | 5 |  third party import "from django.contrib.auth.models import User" should be placed before "from .models import Usuario" (wrong-import-order) |  C0411 | wrong-import-order |
| 109 | [forms.py](code/apps/accounts/forms.py#L5) | 5 |  Unused User imported from django.contrib.auth.models (unused-import) |  W0611 | unused-import |
| 110 | [models.py](code/apps/accounts/models.py#L47) | 47 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 111 | [models.py](code/apps/accounts/models.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 112 | [models.py](code/apps/accounts/models.py#L1) | 1 |  Unable to import 'django.contrib.auth.models' (import-error) |  E0401 | import-error |
| 113 | [models.py](code/apps/accounts/models.py#L2) | 2 |  Unable to import 'django.core.validators' (import-error) |  E0401 | import-error |
| 114 | [models.py](code/apps/accounts/models.py#L4) | 4 |  Unable to import 'django.db' (import-error) |  E0401 | import-error |
| 115 | [models.py](code/apps/accounts/models.py#L6) | 6 |  Unable to import 'multiselectfield' (import-error) |  E0401 | import-error |
| 116 | [models.py](code/apps/accounts/models.py#L11) | 11 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 117 | [models.py](code/apps/accounts/models.py#L48) | 48 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 118 | [models.py](code/apps/accounts/models.py#L50) | 50 |  Consider using Python 3 style super() without arguments (super-with-arguments) |  R1725 | super-with-arguments |
| 119 | [models.py](code/apps/accounts/models.py#L49) | 49 |  Attribute 'username' defined outside __init__ (attribute-defined-outside-init) |  W0201 | attribute-defined-outside-init |
| 120 | [models.py](code/apps/accounts/models.py#L53) | 53 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 121 | [models.py](code/apps/accounts/models.py#L53) | 53 |  Too few public methods (1/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 122 | [models.py](code/apps/accounts/models.py#L2) | 2 |  Unused EmailValidator imported from django.core.validators (unused-import) |  W0611 | unused-import |
| 123 | [permissions.py](code/apps/accounts/permissions.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 124 | [permissions.py](code/apps/accounts/permissions.py#L1) | 1 |  Unable to import 'django.contrib.auth.models' (import-error) |  E0401 | import-error |
| 125 | [permissions.py](code/apps/accounts/permissions.py#L2) | 2 |  Unable to import 'django.contrib.contenttypes.models' (import-error) |  E0401 | import-error |
| 126 | [permissions.py](code/apps/accounts/permissions.py#L30) | 30 |  Variable name "e" doesn't conform to snake_case naming style (invalid-name) |  C0103 | invalid-name |
| 127 | [permissions.py](code/apps/accounts/permissions.py#L31) | 31 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao criar/recuperar grupo {grupo_nome} |  W0707 | raise-missing-from |
| 128 | [permissions.py](code/apps/accounts/permissions.py#L31) | 31 |  Raising too general exception |  W0719 | broad-exception-raised |
| 129 | [permissions.py](code/apps/accounts/permissions.py#L43) | 43 |  Variable name "e" doesn't conform to snake_case naming style (invalid-name) |  C0103 | invalid-name |
| 130 | [permissions.py](code/apps/accounts/permissions.py#L44) | 44 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao criar/recuperar permissão {permissao_nome} |  W0707 | raise-missing-from |
| 131 | [permissions.py](code/apps/accounts/permissions.py#L44) | 44 |  Raising too general exception |  W0719 | broad-exception-raised |
| 132 | [permissions.py](code/apps/accounts/permissions.py#L49) | 49 |  Variable name "e" doesn't conform to snake_case naming style (invalid-name) |  C0103 | invalid-name |
| 133 | [permissions.py](code/apps/accounts/permissions.py#L50) | 50 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao adicionar permissão {permissao_nome} ao grupo {grupo_nome} |  W0707 | raise-missing-from |
| 134 | [permissions.py](code/apps/accounts/permissions.py#L50) | 50 |  Raising too general exception |  W0719 | broad-exception-raised |
| 135 | [permissions.py](code/apps/accounts/permissions.py#L55) | 55 |  Variable name "e" doesn't conform to snake_case naming style (invalid-name) |  C0103 | invalid-name |
| 136 | [permissions.py](code/apps/accounts/permissions.py#L56) | 56 |  Consider explicitly re-raising using 'raise Exception(f'Erro ao adicionar usuário {usuario.nome} ao grupo {grupo_nome} |  W0707 | raise-missing-from |
| 137 | [permissions.py](code/apps/accounts/permissions.py#L56) | 56 |  Raising too general exception |  W0719 | broad-exception-raised |
| 138 | [tests.py](code/apps/accounts/tests.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 139 | [tests.py](code/apps/accounts/tests.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 140 | [tests.py](code/apps/accounts/tests.py#L1) | 1 |  Unused TestCase imported from django.test (unused-import) |  W0611 | unused-import |
| 141 | [urls.py](code/apps/accounts/urls.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 142 | [urls.py](code/apps/accounts/urls.py#L1) | 1 |  Unable to import 'django.urls' (import-error) |  E0401 | import-error |
| 143 | [urls.py](code/apps/accounts/urls.py#L2) | 2 |  Wildcard import views (wildcard-import) |  W0401 | wildcard-import |
| 144 | [urls.py](code/apps/accounts/urls.py#L2) | 2 |  Unused import(s) login_required, permission_required, HttpResponse, HttpResponseRedirect, render, reverse, UsuarioForm, set_permission, Usuario, SolicitacaoCadastro and messages from wildcard import of views (unused-wildcard-import) |  W0614 | unused-wildcard-import |
| 145 | [views.py](code/apps/accounts/views.py#L2) | 2 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 146 | [views.py](code/apps/accounts/views.py#L14) | 14 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 147 | [views.py](code/apps/accounts/views.py#L17) | 17 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 148 | [views.py](code/apps/accounts/views.py#L20) | 20 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 149 | [views.py](code/apps/accounts/views.py#L23) | 23 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 150 | [views.py](code/apps/accounts/views.py#L25) | 25 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 151 | [views.py](code/apps/accounts/views.py#L29) | 29 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 152 | [views.py](code/apps/accounts/views.py#L30) | 30 |  Line too long (126/100) (line-too-long) |  C0301 | line-too-long |
| 153 | [views.py](code/apps/accounts/views.py#L31) | 31 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 154 | [views.py](code/apps/accounts/views.py#L35) | 35 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 155 | [views.py](code/apps/accounts/views.py#L37) | 37 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 156 | [views.py](code/apps/accounts/views.py#L39) | 39 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 157 | [views.py](code/apps/accounts/views.py#L43) | 43 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 158 | [views.py](code/apps/accounts/views.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 159 | [views.py](code/apps/accounts/views.py#L1) | 1 |  Unable to import 'django.contrib.auth.decorators' (import-error) |  E0401 | import-error |
| 160 | [views.py](code/apps/accounts/views.py#L2) | 2 |  Unable to import 'django.http' (import-error) |  E0401 | import-error |
| 161 | [views.py](code/apps/accounts/views.py#L3) | 3 |  Unable to import 'django.shortcuts' (import-error) |  E0401 | import-error |
| 162 | [views.py](code/apps/accounts/views.py#L7) | 7 |  Unable to import 'django.contrib' (import-error) |  E0401 | import-error |
| 163 | [views.py](code/apps/accounts/views.py#L26) | 26 |  Unused variable 'solicitacao' (unused-variable) |  W0612 | unused-variable |
| 164 | [views.py](code/apps/accounts/views.py#L46) | 46 |  Unused argument 'request' (unused-argument) |  W0613 | unused-argument |
| 165 | [views.py](code/apps/accounts/views.py#L56) | 56 |  Unused argument 'request' (unused-argument) |  W0613 | unused-argument |
| 166 | [views.py](code/apps/accounts/views.py#L66) | 66 |  Unused argument 'request' (unused-argument) |  W0613 | unused-argument |
| 167 | [views.py](code/apps/accounts/views.py#L76) | 76 |  Unused argument 'request' (unused-argument) |  W0613 | unused-argument |
| 168 | [views.py](code/apps/accounts/views.py#L7) | 7 |  third party import "from django.contrib import messages" should be placed before "from .forms import UsuarioForm" (wrong-import-order) |  C0411 | wrong-import-order |
| 169 | [views.py](code/apps/accounts/views.py#L6) | 6 |  Unused Usuario imported from models (unused-import) |  W0611 | unused-import |
| 170 | [__init__.py](code/apps/financas/__init__.py#L1) | 1 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 171 | [admin.py](code/apps/financas/admin.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 172 | [admin.py](code/apps/financas/admin.py#L1) | 1 |  Unable to import 'django.contrib' (import-error) |  E0401 | import-error |
| 173 | [admin.py](code/apps/financas/admin.py#L2) | 2 |  Wildcard import models (wildcard-import) |  W0401 | wildcard-import |
| 174 | [admin.py](code/apps/financas/admin.py#L2) | 2 |  Unused import(s) uuid, accounts, igreja, models, F, validate_cpf and validate_data from wildcard import of models (unused-wildcard-import) |  W0614 | unused-wildcard-import |
| 175 | [apps.py](code/apps/financas/apps.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 176 | [apps.py](code/apps/financas/apps.py#L1) | 1 |  Unable to import 'django.apps' (import-error) |  E0401 | import-error |
| 177 | [apps.py](code/apps/financas/apps.py#L4) | 4 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 178 | [apps.py](code/apps/financas/apps.py#L4) | 4 |  Too few public methods (0/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 179 | [models.py](code/apps/financas/models.py#L80) | 80 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 180 | [models.py](code/apps/financas/models.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 181 | [models.py](code/apps/financas/models.py#L5) | 5 |  Unable to import 'django.db' (import-error) |  E0401 | import-error |
| 182 | [models.py](code/apps/financas/models.py#L6) | 6 |  Unable to import 'django.db.models' (import-error) |  E0401 | import-error |
| 183 | [models.py](code/apps/financas/models.py#L48) | 48 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 184 | [models.py](code/apps/financas/models.py#L48) | 48 |  Unused argument 'kargs' (unused-argument) |  W0613 | unused-argument |
| 185 | [models.py](code/apps/financas/models.py#L52) | 52 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 186 | [models.py](code/apps/financas/models.py#L83) | 83 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 187 | [models.py](code/apps/financas/models.py#L83) | 83 |  Unused argument 'kargs' (unused-argument) |  W0613 | unused-argument |
| 188 | [models.py](code/apps/financas/models.py#L196) | 196 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 189 | [models.py](code/apps/financas/models.py#L199) | 199 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 190 | [models.py](code/apps/financas/models.py#L203) | 203 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 191 | [models.py](code/apps/financas/models.py#L261) | 261 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 192 | [models.py](code/apps/financas/models.py#L264) | 264 |  Missing function or method docstring (missing-function-docstring) |  C0116 | missing-function-docstring |
| 193 | [models.py](code/apps/financas/models.py#L8) | 8 |  Unused validate_cpf imported from adgestao.validators (unused-import) |  W0611 | unused-import |
| 194 | [tests.py](code/apps/financas/tests.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 195 | [tests.py](code/apps/financas/tests.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 196 | [tests.py](code/apps/financas/tests.py#L1) | 1 |  Unused TestCase imported from django.test (unused-import) |  W0611 | unused-import |
| 197 | [views.py](code/apps/financas/views.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 198 | [views.py](code/apps/financas/views.py#L1) | 1 |  Unable to import 'django.shortcuts' (import-error) |  E0401 | import-error |
| 199 | [views.py](code/apps/financas/views.py#L1) | 1 |  Unused render imported from django.shortcuts (unused-import) |  W0611 | unused-import |
| 200 | [__init__.py](code/apps/igreja/__init__.py#L1) | 1 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 201 | [admin.py](code/apps/igreja/admin.py#L7) | 7 |  Final newline missing (missing-final-newline) |  C0304 | missing-final-newline |
| 202 | [admin.py](code/apps/igreja/admin.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 203 | [admin.py](code/apps/igreja/admin.py#L1) | 1 |  Unable to import 'django.contrib' (import-error) |  E0401 | import-error |
| 204 | [admin.py](code/apps/igreja/admin.py#L2) | 2 |  Wildcard import models (wildcard-import) |  W0401 | wildcard-import |
| 205 | [admin.py](code/apps/igreja/admin.py#L2) | 2 |  Unused import(s) uuid, models, F, MultiSelectField, validate_cpf and validate_data from wildcard import of models (unused-wildcard-import) |  W0614 | unused-wildcard-import |
| 206 | [apps.py](code/apps/igreja/apps.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 207 | [apps.py](code/apps/igreja/apps.py#L1) | 1 |  Unable to import 'django.apps' (import-error) |  E0401 | import-error |
| 208 | [apps.py](code/apps/igreja/apps.py#L4) | 4 |  Missing class docstring (missing-class-docstring) |  C0115 | missing-class-docstring |
| 209 | [apps.py](code/apps/igreja/apps.py#L4) | 4 |  Too few public methods (0/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 210 | [models.py](code/apps/igreja/models.py#L37) | 37 |  Trailing whitespace (trailing-whitespace) |  C0303 | trailing-whitespace |
| 211 | [models.py](code/apps/igreja/models.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 212 | [models.py](code/apps/igreja/models.py#L3) | 3 |  Unable to import 'django.db' (import-error) |  E0401 | import-error |
| 213 | [models.py](code/apps/igreja/models.py#L4) | 4 |  Unable to import 'django.db.models' (import-error) |  E0401 | import-error |
| 214 | [models.py](code/apps/igreja/models.py#L5) | 5 |  Unable to import 'multiselectfield' (import-error) |  E0401 | import-error |
| 215 | [models.py](code/apps/igreja/models.py#L10) | 10 |  Too few public methods (1/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 216 | [models.py](code/apps/igreja/models.py#L44) | 44 |  Too few public methods (1/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 217 | [models.py](code/apps/igreja/models.py#L90) | 90 |  Too few public methods (1/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 218 | [models.py](code/apps/igreja/models.py#L144) | 144 |  Too few public methods (1/2) (too-few-public-methods) |  R0903 | too-few-public-methods |
| 219 | [tests.py](code/apps/igreja/tests.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 220 | [tests.py](code/apps/igreja/tests.py#L1) | 1 |  Unable to import 'django.test' (import-error) |  E0401 | import-error |
| 221 | [tests.py](code/apps/igreja/tests.py#L1) | 1 |  Unused TestCase imported from django.test (unused-import) |  W0611 | unused-import |
| 222 | [views.py](code/apps/igreja/views.py#L1) | 1 |  Missing module docstring (missing-module-docstring) |  C0114 | missing-module-docstring |
| 223 | [views.py](code/apps/igreja/views.py#L1) | 1 |  Unable to import 'django.shortcuts' (import-error) |  E0401 | import-error |
| 224 | [views.py](code/apps/igreja/views.py#L1) | 1 |  Unused render imported from django.shortcuts (unused-import) |  W0611 | unused-import |
| 225 | [manage.py](code/manage.py#L11) | 11 |  Import outside toplevel (django.core.management.execute_from_command_line) (import-outside-toplevel) |  C0415 | import-outside-toplevel |
| 226 | [manage.py](code/manage.py#L1) | 1 |  Similar lines in 2 files |  R0801 |  |
