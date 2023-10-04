from django.db import models
from django.utils import timezone

# Create your models here.
# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

# Aqui, você cria uma classe para os campos serem preenchidos para a
# base de dados. O Django cria o id automaticamente.
# A parte de Field, define o que será cada categoria.
# CharField = String, EmailField = Email, DateField = Data, TextField = Texto
# DateTimeField = Data e Hora, BooleanField = Booleano (True/False)
# para tornar opcional, você precisa colocar blank=True
# Para criar a base de dados, você precisa rodar o comando:
# python manage.py makemigrations


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)  # pegar a data
    description = models.TextField(blank=True)

    # Apresentar no admin o nome completo
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
