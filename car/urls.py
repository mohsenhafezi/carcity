from django.urls import path
from .views import car_page

urlpatterns = [
    path('', car_page, name='car_page'),
]