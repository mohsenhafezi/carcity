# Generated by Django 5.0.6 on 2024-08-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_car_is_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]