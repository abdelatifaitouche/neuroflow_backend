from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Departement(models.Model):
    departement_name = models.CharField(max_length=150 , unique=True)


    def __str__(self):
        return self.departement_name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150 , unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username' , 'first_name' , 'last_name']
    departement = models.ForeignKey('Departement' , on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return self.username


    
