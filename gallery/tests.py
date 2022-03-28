from django.test import TestCase
from .models import Location, Category, Image

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
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)