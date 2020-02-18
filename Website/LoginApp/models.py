from django.db import models

class SignUpModel(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(primary_key=True)
    Password = models.CharField(max_length=200)
