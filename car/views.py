from django.shortcuts import render
from django.http import HttpResponse


def car_page(request):
    return HttpResponse("This is the main page of the car apps.")
