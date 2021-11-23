import typing
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET, SET_NULL
from django.db.models.fields import AutoField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class topic(models.Model):
    topic = models.CharField(max_length=300)
    
    def __str__(self):
        return self.topic

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    post = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, related_name='likes', default=None, blank=True)
    def __str__(self):
        return f'{self.post}'
    
    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

class comments(models.Model):
    created = models.DateTimeField(auto_now=True)
    posts = models.ForeignKey(post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    comment = models.TextField(max_length= 500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment)