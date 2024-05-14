from django.db import models

# Create your models here.

class contactsave(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    number=models.IntegerField()
    msg=models.TextField()
