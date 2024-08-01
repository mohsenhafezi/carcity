from django.urls import path
from .views import car_page

# all paths of car app should add here to apply after "/car" path
urlpatterns = [
    path('', car_page, name='car'),
]
