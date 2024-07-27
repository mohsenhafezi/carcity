from django.contrib import admin
from .models import Car, Person

# Models should be registered here to show in admin panel.
admin.site.register(Car)
admin.site.register(Person)
