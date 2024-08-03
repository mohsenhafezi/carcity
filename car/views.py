from django.shortcuts import render
from .models import Car


def car_page(request):
    cars = Car.objects.filter(is_show=True)  # It will get all cars
    context = {'cars': cars}
    return render(request, 'car/car_list.html', context)
