from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
# Create your models here.



class TestM(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=200)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    

class Goods(models.Model):
    title = models.CharField(max_length=100)
    content = JSONField()
    
    

