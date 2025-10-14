from django.shortcuts import render
from taxi.models import Driver, Car, Manufacturer
from django.http import HttpResponse, HttpRequest

def index(request):
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    context = {"num_drivers": num_drivers,
               "num_manufacturers": num_manufacturers,
               "num_cars": num_cars}

    return render(request, "taxi/index.html", context=context)
