from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class GenderChoise(models.Choices):
    MALE = 'Erkak'
    FEMALE = 'Ayol'


class User(AbstractUser):
    gender = models.CharField(
        max_length=255, choices=GenderChoise.choices, default=GenderChoise.FEMALE)

    birth_day = models.DateField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = None

    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

    address = models.CharField(max_length=255)

    instagram = models.CharField(max_length=255)
    imkon_uz = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)

    workplace = models.CharField(max_length=255)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    about = models.TextField()

    USERNAME_FIELD = 'phone_number'

    def __str__(self) -> str:
        return self.get_full_name()
