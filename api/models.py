from django.db import models
from django.contrib.auth.models import User

class Films(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    image_url = models.CharField(max_length=140)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    film = models.ForeignKey(Films,on_delete=models.CASCADE, null=True)
    ranged = models.CharField(max_length=1)
    critic = models.CharField(max_length=140,blank=True,null=True)

class TokensUser(models.Model):
    token = models.CharField(max_length=255)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
