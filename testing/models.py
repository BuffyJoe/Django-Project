import typing
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import AutoField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class roles(models.Model):
    Seller = models.BooleanField(default=False)
    Buyer = models.BooleanField(default=True)
    def __str__(self):
        return f'{str(roles)}'


class people(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    about = models.TextField(max_length=500, null=True)
    def __str__(self):
        return f'@{self.username}'

class topic(models.Model):
    topic = models.CharField(max_length=300)
    def __str__(self):
        return self.topic

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    post = models.TextField(max_length=500)
    created = models.DateField(auto_now=True)
    def __str__(self):
        return f'{self.Topic}'

class finance(models.Model):
    owner = models.ForeignKey(people, on_delete=models.CASCADE)
    gold = models.BooleanField(default=False)
    silver = models.BooleanField(default=False)
    bronze = models.BooleanField(default=True)
    amount = models.IntegerField()
    def __str__(self):
        return f'{self.owner} - {self.amount}'

class comments(models.Model):
    created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    comment = models.TextField(max_length= 500)

    def __str__(self):
        return str(self.owner)