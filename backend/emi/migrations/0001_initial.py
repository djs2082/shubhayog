# Generated by Django 3.2 on 2021-04-23 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMIModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(verbose_name='EMI AMOUNT')),
                ('deadline_date', models.DateField(auto_now_add=True, verbose_name='LAST DATE FOR THIS EMI')),
                ('date', models.DateField(auto_now_add=True, verbose_name='DATE')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loanmodel', verbose_name='LOAN DETAILS')),
            ],
            options={
                'verbose_name': 'EMI',
                'verbose_name_plural': 'EMIS',
            },
        ),
    ]
