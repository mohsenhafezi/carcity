from django.core.exceptions import ValidationError


# this code is used to validate entered number for created years of cars
def validate_year(value):
    if not (1300 <= value <= 1499):
        raise ValidationError(f'{value} is not a valid year')
