from django.db import models
from .validators import validate_year


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[validate_year])
    kilometers = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
