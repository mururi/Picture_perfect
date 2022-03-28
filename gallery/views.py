from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    images = Image.get_all_images()
    return render(request, 'index.html', {"images": images})