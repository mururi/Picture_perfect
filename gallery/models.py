from unicodedata import category, name
from django.db import models
import pyperclip

class Location(models.Model):
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.city

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 255)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add = True)

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls, id):
        '''
        Method to delete an Image object
        '''

        cls.objects.filter(id = id).delete()

    @classmethod
    def update_image(cls, id):
        pass

    @classmethod
    def get_image_by_id(cls, id):
        '''
        Method to get an Image by its ID
        '''

        return cls.objects.filter(id = id)[0]

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(category__name__icontains = search_category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(category__location__icontains = location)
        return images

    @classmethod
    def copy_image_url(cls, id):
        image = cls.objects.get(id = id)
        pyperclip.copy(image.image.url)

    def __str__(self):
        return self.name

