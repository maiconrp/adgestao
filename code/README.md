# Repositório Django

Esta pasta contém os arquivos de código Django para o projeto AD Gestão

# Conteúdo da pasta
- Arquivos do projeto Django
- Pastas de aplicativos Django

# Estrutura
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    |
    ├───adgestao
    |   └── tests
    └───apps
        ├───accounts
        ├───financas
        └───igreja
        
# Instalação
## Requisitos
- Git
- Pip
- Python 3.x
- Django 2.x ou superior

## Passos

1. Instale o [Git](https://git-scm.com/downloads)
2. Abra o terminal ou Git Bash e digite o seguinte comando:

    ```
    git clone https://github.com/maiconrp/adgestao.git
    ```

3. Acesse a pasta code

    ```
   cd adgestao\code
    ```
4. Instale as dependências
    
    ```
   pip install -r requirements.txt
    ```
5. Execute as migrações:
    
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Rode a aplicação
    
    ```
    python manage.py runserver
    ```
7. Acesse a aplicação digitando <http://127.0.0.1:8000/> no navegador.

# Observações
- Certifique-se de estar usando a versão correta do Python e do Django
- Mantenha seus arquivos de configuração seguros, especialmente informações sensíveis como senhas e chaves API.
- Se precisar de mais informações ou tiver dúvidas, consulte a [documentação oficial do Django][django].

[django]: https://docs.djangoproject.com/pt-br/4.1/
