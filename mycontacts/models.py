from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    relation = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

