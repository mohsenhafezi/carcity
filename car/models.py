from django.db import models
from .validators import validate_year


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[validate_year])
    kilometers = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"