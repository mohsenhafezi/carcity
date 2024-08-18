from django import forms

from car.validators import validate_year


class CreateCarForm(forms.Form):
    brand = forms.CharField(max_length=100, label='برند خودرو')
    model = forms.CharField(max_length=100, label='مدل خودرو')
    image = forms.ImageField(label='تصویر خودرو')
    color = forms.CharField(max_length=50, label='رنگ خودرو')
    year = forms.IntegerField(validators=[validate_year], label='سال ساخت خودرو')
    kilometers = forms.IntegerField(label='میزان کارکرد خودرو')
    price = forms.IntegerField(label='قیمت خودرو')
    city = forms.CharField(max_length=100, label='شهر')
    registered_by = forms.IntegerField()
