from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=25)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True) 
    role = models.CharField(max_length=255)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Profile(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

