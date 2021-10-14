from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255)
    post_cat = models.CharField(max_length=255)