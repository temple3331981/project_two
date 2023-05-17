from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    REQUIRED_FIELDS=['password']
    USERNAME_FIELD='EMAIL'
    objects=UserManager()
    
# Create your models here.
