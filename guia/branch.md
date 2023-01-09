# Branches

:information_source: **`Branches` (ramos)** são versões paralelas do código de um projeto em um ponto específico do tempo, permitindo alterações sem **afetar a versão principal** ("branch master" ou "branch principal"). Assim, é possível **adicionar novas funcionalidades** ou **corrigir bugs** sem interromper o trabalho em andamento da equipe. 

<hr>

## Por que usar branches?
Existem várias razões pelas quais é importante usar branches em um projeto:

:diamond_shape_with_a_dot_inside: Permitir que vários desenvolvedores trabalhem em diferentes funcionalidades ao mesmo tempo sem interferir uns nos outros.

:diamond_shape_with_a_dot_inside: Permitir que as alterações sejam realizadas de forma segura, sem afetar o código principal do projeto.

:diamond_shape_with_a_dot_inside: Facilitar o processo de testes e validação de alterações antes de integrá-las ao código principal.

<hr>

## Como manipular branches

:one: **Criar uma nova branch:**
```
git branch <nome da branch>
```
<hr>

:two: **Mudar para uma branch existente:**
```
git checkout <nome da branch>
```

<hr>

:three: **Criar uma nova branch e já mudar para ela:**
```
git checkout -b <nome da branch>
```

<hr>

:four: **Ver todas as branches existentes:**
```
git branch
```

<hr>

:five: **Ver a branch atualmente selecionada:**
```
git branch -l
```

<hr>

:six: **Mesclar um branch em outra:**
```
git git merge <nome da branch>
```

<hr>

## Padrões para branches
:information_source: Existem alguns padrões recomendados para nomear branches, de forma a facilitar a identificação das alterações realizadas. Alguns desses padrões incluem:

:white_check_mark: Branches de novas funcionalidades: Prefixo **`feature/`** + ***funcionalidade***:
```
feature/tela-de-login
feature/filtro-saídas
feature/validacao-de-form
```
<br>

:white_check_mark: Branches de correções de bugs: Prefixo **`fix/`** + ***bug***:
```
fix/bug-de-login
fix/bug-filtro-de-saidas
fix/bug-form-validacao
```
<br>

:white_check_mark: Branches de correções de bugs urgentes: Prefixo **`hotfix/`** + ***bug***:
```
hotfix/credenciais-expostas
hotfix/hash-de-senhas
hotfix/vulnerabilidade-front
```
<br>
