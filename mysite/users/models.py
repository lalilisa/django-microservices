from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)