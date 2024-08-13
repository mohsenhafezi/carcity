from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Car


def car_page(request):
    cars = Car.objects.filter(is_show=True).order_by('created_date')  # It will get all cars
    # search_keyword = request.GET.get('Search')
    # if search_keyword:
    #     cars = cars.filter(model__icontains=search_keyword).order_by('created_date')
    context = {'cars': cars}
    return render(request, 'car/car_list.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {'car': car}
    return render(request, template_name='car/car_detail.html', context=context)


def car_search(request):
    # cars = Car.objects.filter(is_show=True).order_by('-id')[:2]  # It will get all cars
    search_keyword = request.GET.get('Search')
    if search_keyword:
        cars = Car.objects.filter(is_show=True, model__icontains=search_keyword)
    else:
        # در صورت عدم وجود جستجو، دو مورد آخر را برگردانید
        cars = Car.objects.filter(is_show=True).order_by('-id')[:2]
    # if search_keyword:
    #     cars = cars.filter(model__icontains=search_keyword)
    context = {'cars': cars}
    return render(request, 'car/car_search.html', context)
