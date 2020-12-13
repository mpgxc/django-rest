### Crianfo um ambiente de desenvolvimento
 - python3 -m venv env
 - source env/bin/activate

### Instalando as depedências
- pip3 install -r requirements.txt

### Criando um app
- django-admin startapp name

### Linkando o database
- python manage.py migrate

### Criando um usuário admin
- python manage.py createsuperuser --email admin@example.com --username admin

### Executando o server
- python3 manage.py runserver
