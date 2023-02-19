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

### Comandos Basicos

<br>

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
git merge <nome da branch>
```

<hr>

:seven: **Deletar uma branch**
```
git branch -d <nome da branch>
```

*  É importante lembrar que você só conseguirá deletar uma branch que não possua commits que não foram incorporados em outras branches. 
Para forçar a deleção de uma branch, mesmo que ela possua commits não incorporados em outras branches, utilize o seguinte comando:

```
git branch - D <nome da branch>
```

:warning: Este comando **deletará** a branch mesmo que ela esteja associada à outras branchs, tenha certeza do que está fazendo ao utilizá-la

<hr>

:eight: **Renomear uma branch**

```
git branch -m <novo-nome>
```

<hr>

:nine: **Enviar uma branch ao repositório remoto**:

Depois de criar uma nova branch no seu repositório local, você precisará fazer o **"push"** dessa branch para o repositório remoto no GitHub para que ela possa ser vista e colaborada por outras pessoas. Aqui está um exemplo de como você pode fazer isso usando o Git:

1. *Verifique se você está na branch que deseja enviar:*
```
git branch -l
```

2. Faça o push da branch para o repositório remoto:
```
git push -u origin <nome-da-branch>
```

* Esse comando vai enviar a branch para o repositório remoto no GitHub, criando uma cópia dela lá. O parâmetro `-u` serve para estabelecer uma ligação entre a branch local e a remota, de forma que, a partir de então, você pode usar apenas _git push_ e _git pull_ para sincronizar as branches.
* Depois disso, a branch nova deverá aparecer no repositório remoto e outros colaboradores poderão visualizá-la e fazer pull requests.

<hr>

### Comandos Avançados

<br>

:one: **Criar uma nova branch a partir de um commit específico**

```
git branch <nome-da-branch> <hash-do-commit>
```

* Este comando cria uma nova branch a partir de um commit específico, sendo útil para criar uma branch a partir de um ponto específico na história do projeto.

<hr>

:two: **Visualizar o histórico de uma branch**
```
git log <nome-da-branch>
```
* Este comando permite visualizar o histórico de commits de uma branch específica.

<hr>

:three: **Comparar o conteúdo de duas branche**

```
git diff <nome-da-branch-1> <nome-da-branch-2>
```
* Este comando permite visualizar as diferenças entre duas branches específicas.

<hr>

:four: **Criar uma branch a partir de outra e mudar para ela**
```
git checkout -b <nome-da-branch-nova> <nome-da-branch-existente>
```
* Este comando cria uma nova branch a partir de uma branch existente e muda para a nova branch criada.

<hr>

:five: **Desfazer as mudanças feitas em uma branch**
```
git reset --hard HEAD
```
:warning: Este comando **desfaz todas as mudanças feitas** na branch atualmente selecionada desde o último commit feito. É importante lembrar que este comando pode **deletar mudanças permanentemente** e, por isso, deve ser utilizado com cuidado.

<hr>

:six: **Criar uma branch a partir de um commit específico em outra branch**
```
git cherry-pick <hash-do-commit>
```
* Este comando permite aplicar um commit específico de uma branch em outra branch.

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

:white_check_mark: Branches testes: Prefixo **`teste/`** + ***assunto***:
```
teste/gitHub-actions
teste/api-reamde
teste/painel-issue
```
<br>
