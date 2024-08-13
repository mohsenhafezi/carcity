from django.urls import path
from .views import car_page, car_detail, car_search

# all paths of car app should add here to apply after "/car" path
app_name = 'car'
urlpatterns = [
    path('', car_page, name='car_page'),
    # <int:car_id> used to take args from url
    path('detail/<int:car_id>/', car_detail, name='car_detail'),
    path('car-search/', car_search, name='car_search'),
]
