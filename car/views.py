from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CreateCarForm


def car_page(request):
    cars = Car.objects.filter(is_show=True).order_by('created_date')  # It will get all cars
    context = {'cars': cars}
    return render(request, 'car/car_list.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {'car': car}
    return render(request, template_name='car/car_detail.html', context=context)


def car_search(request):
    search_keyword = request.GET.get('Search')
    if search_keyword:
        cars = Car.objects.filter(Q(is_show=True) &
                                  (Q(model__icontains=search_keyword) |
                                   Q(brand__icontains=search_keyword) |
                                   Q(year__icontains=search_keyword)
                                   ))
    else:
        cars = Car.objects.filter(is_show=True).order_by('-id')[:2]
    context = {'cars': cars}
    return render(request, 'car/car_search.html', context)


def car_create(request):
    form = CreateCarForm()
    context = {'form': form}
    return render(request, 'car/car_add.html', context)
