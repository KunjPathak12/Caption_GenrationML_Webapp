from django.db import models
class uploadImage(models.Model):
    image = models.ImageField(upload_to='images')