from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class GenderChoise(models.Choices):
    MALE = 'Erkak'
    FEMALE = 'Ayol'


class User(AbstractUser):
    gender = models.CharField(
        max_length=255, choices=GenderChoise.choices, default=GenderChoise.FEMALE)

    birth_day = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = None

    USERNAME_FIELD = 'phone_number'
