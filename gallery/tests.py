from django.test import TestCase
from .models import Location, Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile

class LocationTestClass(TestCase):
    '''
    Test class to test the behavior of the location class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''

        self.new_location = Location(city = "Nairobi", country = "Kenya")

    def test_instance(self):
        '''
        test_instance method to test if the new_loction object is an instance of the Location model
        '''

        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_method(self):
        '''
        test_save_method method to test if new_location object is saved successfully
        '''
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    '''
    Test class to test the behavior of the category class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''

        self.new_category = Category(name = "Lifestyle")

    def test_instance(self):
        '''
        test_instance method to test if the new_category object is an instance of the Category model
        '''

        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_method(self):
        '''
        test_save_method method to test if new_category object is saved successfully
        '''
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

class ImageTestClass(TestCase):
    '''
    Test class to test the behavior of the Image model class
    '''

    def setUp(self):
        '''
        set up method to run before each test case
        '''

        # Creating a new location and saving it
        self.new_location = Location(city = "Nairobi", country = "Kenya")
        self.new_location.save()

        # Creating a new category and saving it
        self.new_category = Category(name = "Lifestyle")
        self.new_category.save()

        self.new_image = Image(name = 'test_image', description = "sample descritpion", location = self.new_location, category = self.new_category)

        # self.new_image.image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')

    def test_instance(self):
        '''
        test_instance method to test if the new_image object is an instance of the Image model
        '''

        self.assertTrue(isinstance(self.new_image, Image))

    def test_delete_method(self):
        Image.delete_image(self.new_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)