# Generated by Django 3.2 on 2021-04-25 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emi', '0003_auto_20210423_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emimodel',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 25), verbose_name='DATE'),
        ),
    ]
