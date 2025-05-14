from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField('username', max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
