# Generated by Django 3.2 on 2021-04-23 05:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')]),
        ),
    ]
