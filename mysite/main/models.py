from django.db import models

class Carusel(models.Model):
    title = models.CharField(max_length = 200)
    dеscription = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/")
