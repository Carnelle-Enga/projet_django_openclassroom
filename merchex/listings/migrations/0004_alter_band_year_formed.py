# Generated by Django 5.1 on 2024-12-01 05:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_bibliography_band_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2024)]),
        ),
    ]
