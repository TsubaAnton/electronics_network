from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
