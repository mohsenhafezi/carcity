from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Car, Person
from .forms import CreateCarForm


def car_page(request):
    cars = Car.objects.filter(is_show=True).order_by('-created_date')  # It will get all cars
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
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # this following code will create a new car in the database
            car_brand = form.cleaned_data.get('brand')
            car_model = form.cleaned_data.get('model')
            car_year = form.cleaned_data.get('year')
            car_price = form.cleaned_data.get('price')
            car_image = form.cleaned_data.get('image')
            car_created_date = form.cleaned_data.get('created_date')
            car_color = form.cleaned_data.get('color')
            car_kilometers = form.cleaned_data.get('kilometers')
            car_city = form.cleaned_data.get('city')
            car_registered_by = form.cleaned_data.get('registered_by')
            # person = get_object_or_404(Person, id=car_registered_by)
            Car.objects.create(brand=car_brand, model=car_model, year=car_year, price=car_price, image=car_image,
                               created_date=car_created_date, color=car_color, kilometers=car_kilometers, city=car_city,
                               registered_by_id=car_registered_by)
            print('car is created')
    context = {'form': form}
    return render(request, 'car/car_add.html', context)
