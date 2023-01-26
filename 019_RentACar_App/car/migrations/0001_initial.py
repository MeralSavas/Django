# Generated by Django 4.1.5 on 2023-01-26 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=15, unique=True)),
                ('brand', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=20)),
                ('year', models.SmallIntegerField()),
                ('gear', models.CharField(choices=[('a', 'automatic'), ('m', 'manuel')], max_length=1)),
                ('rent_per_day', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1)])),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
    ]
