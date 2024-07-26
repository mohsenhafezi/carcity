from django.core.exceptions import ValidationError


def validate_year(value):
    if not (1300 <= value <= 1499):
        raise ValidationError(f'{value} is not a valid year')
