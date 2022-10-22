from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    role = models.CharField(max_length=25)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

