from django.shortcuts import render
from django.http import HttpResponse
from .models import Car


def car_page(request):
    # cars = Car.objects.all()  # It will get all cars
    # cars2 = Car.objects.get(model='Cerato')
    # return HttpResponse(cars2.color)
    return render(request, 'index.html')
