python3 -m venv env
source env/bin/activate

### Criando um app
- django-admin startapp name

### Linkando o database
- python manage.py migrate

### Criando um usuário admin
- python manage.py createsuperuser --email admin@example.com --username admin
