from django.db import models

# Create your models here.
class Login(models.Model):
    email         = models.CharField(max_length=30)
    password      = models.CharField(max_length=25)
class Newuser(models.Model):
    name          = models.CharField(max_length=30)
    email         = models.CharField(max_length=30)
    password      = models.CharField(max_length=30)
    fk_login      = models.ForeignKey(Login,on_delete=models.CASCADE,default=None)