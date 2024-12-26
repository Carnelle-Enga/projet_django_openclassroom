# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello():
    bands=Band.objects.all()
    # return render(request, 'listings/hello.html',{'bands': bands})
    return HttpResponse("<h1>HELLO WORLD</h1>")


def listings(request):
    listings=Listing.objects.all()

    return render(request, 'listings/listings.html',{'listings':listings})

def about(request):
    return render(request,'listings/about.html')



def contact(request):
    return render(request,'listings/contact.html')