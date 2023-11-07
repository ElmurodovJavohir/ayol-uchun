from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class GenderChoise(models.Choices):
    MALE = 'Erkak'
    FEMALE = 'Ayol'


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("User must have a phone number")
        if not password:
            raise ValueError("User must have a Password")

        user = self.model(
            phone_number=phone_number
        )

        user.set_password(password)  # change password to hash
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    gender = models.CharField(
        max_length=255, choices=GenderChoise.choices, default=GenderChoise.FEMALE, blank=True, null=True)

    birth_day = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(null=True, blank=True)

    country = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)

    instagram = models.CharField(max_length=255, blank=True, null=True)
    imkon_uz = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    workplace = models.CharField(max_length=255, blank=True, null=True)
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def __str__(self) -> str:
        return self.get_full_name()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self) -> str:
        return self.phone_number

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
