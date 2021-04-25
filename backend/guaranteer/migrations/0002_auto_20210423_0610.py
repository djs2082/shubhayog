# Generated by Django 3.2 on 2021-04-23 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guaranteer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guaranteermodel',
            options={'verbose_name': 'GUARANTEER', 'verbose_name_plural': 'GUARANTEERS'},
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='address',
            field=models.CharField(max_length=200, verbose_name='ADDRESS'),
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='EMAIL'),
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='fname',
            field=models.CharField(max_length=50, verbose_name='FIRST NAME'),
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='lname',
            field=models.CharField(max_length=50, verbose_name='LAST NAME'),
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')], verbose_name='MOBILE'),
        ),
        migrations.AlterField(
            model_name='guaranteermodel',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
