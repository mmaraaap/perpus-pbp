from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    category = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
