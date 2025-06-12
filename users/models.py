from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = CountryField(blank=True, null=True, blank_label='(Выберите страну)')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username требуется для createsuperuser

    def __str__(self):
        return self.email