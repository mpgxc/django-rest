#### Crianfo um ambiente de desenvolvimento
 - python3 -m venv env
 - source env/bin/activate

#### Instalando as depedências
- pip3 install -r requirements.txt

#### Criando um app
- django-admin startapp name

#### Linkando o database
- python manage.py migrate

#### Criando um usuário admin
- python manage.py createsuperuser --email admin@example.com --username admin

#### Executando o server
- python3 manage.py runserver


## 🤔 Como como executar ?
    
#### Clonando o repositório
```console
mpgxc@mpgxc:~$ git clone https://github.com/mpgxc/micro-django-api.git
mpgxc@mpgxc:~$ cd micro-django-api/
mpgxc@mpgxc:~$ code .
```
#### Ambiente Virtual
```console
mpgxc@mpgxc:~$ python3 -m venv myenv
mpgxc@mpgxc:~$ source myvenv/bin/activate
mpgxc@mpgxc:~$ pip install -r requiremets.txt
```
#### Configurando banco de dados
```
Para facilitar todo o processo de instalação e configuração do postgres utilizaremos um container
docker para agilizar todo o processo
```
 
#### Instalando Docker
```console
mpgxc@mpgxc:~$ sudo apt install docker.io
```
#### Utilizando o comando docker sem sudo
```console 
mpgxc@mpgxc:~$ sudo usermod -aG docker ${USER}
mpgxc@mpgxc:~$ su - ${USER}
mpgxc@mpgxc:~$ id -nG
``` 
#### Testando docker
```console
mpgxc@mpgxc:~$ docker run hello-world
```
#### Instalando Postgres via DockerHub
```
Caso os passos anteriores tenham ocorrido sem problemas o seguinte passo é baixar a imagem do 
postgres do dockerhub
```

```console
mpgxc@mpgxc:~$ docker run --name nome_do_banco -e POSTGRES_PASSWORD=senha  -p 5432:5432 -d postgres
```
#### Instalando complementos
```console
mpgxc@mpgxc:~$ sudo apt-get update
mpgxc@mpgxc:~$ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
mpgxc@mpgxc:~$ pip install psycopg2
```
#### Conectando o projeto Dajngo com Postgres
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "nome_do_banco",
        "USER": "postgres",
        "PASSWORD": "senha",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
#### Criando as tabelas e executando o projeto

```console
mpgxc@mpgxc:~$ python manage.py makemigrations
mpgxc@mpgxc:~$ python manage.py migrate
mpgxc@mpgxc:~$ python manage.py runserver
```
## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

