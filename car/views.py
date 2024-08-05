from django.http import HttpResponse
from django.shortcuts import render
from .models import Car


def car_page(request):
    cars = Car.objects.filter(is_show=True)  # It will get all cars
    context = {'cars': cars}
    return render(request, 'car/car_list.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {'car': car}
    return render(request, template_name='car/car_detail.html', context=context)

