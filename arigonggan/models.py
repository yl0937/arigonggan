from django.db import models

# Create your models here.
class Seat(models.Model):
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=15)