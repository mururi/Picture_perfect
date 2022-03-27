from unicodedata import category
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length = 50)

class Category(models.Model):
    name = models.CharField(max_length = 30)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 255)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

