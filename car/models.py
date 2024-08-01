from django.db import models
from .validators import validate_year


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# these classes are related to the Car app in this Website


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carcity/images/',blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # this auto now adds feature will add date time automatically to the field
    # if we have an update record, it should have an "auto_now = True"
    color = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[validate_year])
    kilometers = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    city = models.CharField(max_length=100)
    registered_by = models.ForeignKey(Person, on_delete=models.CASCADE)

    # if Person class defined after the car model, then we can introduce Person as string to avoid an error:
    # registered_by = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
