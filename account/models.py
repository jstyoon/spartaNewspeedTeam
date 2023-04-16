from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserModel(AbstractUser):
    username = models.CharField(max_length=20, unique=True) ####
    password1 = models.CharField(max_length=20, default="10")
    password2 = models.CharField(max_length=20, default="10")
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')