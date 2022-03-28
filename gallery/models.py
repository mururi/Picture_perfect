from unicodedata import category
from django.db import models

class Location(models.Model):
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.city

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 255)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

