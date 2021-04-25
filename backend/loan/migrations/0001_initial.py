# Generated by Django 3.2 on 2021-04-23 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guaranteer', '0002_auto_20210423_0610'),
        ('customer', '0004_auto_20210423_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='LOAN NAME')),
            ],
            options={
                'verbose_name': 'LOAN TYPE',
                'verbose_name_plural': 'LOAN TYPES',
            },
        ),
        migrations.CreateModel(
            name='LoanModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(verbose_name='LOAN AMOUNT')),
                ('installment', models.IntegerField(verbose_name='INSTALLMENT AMOUNT')),
                ('installment_date', models.DateField(verbose_name='INSTALLMENT DATE')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customermodel', verbose_name='CUSTOMER NAME')),
                ('guaranteer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='guaranteer.guaranteermodel', verbose_name='GUARANTEER NAME')),
                ('loantype', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loan.loantypemodel', verbose_name='LOAN TYPE')),
            ],
            options={
                'verbose_name': 'LOAN',
                'verbose_name_plural': 'LOANS',
            },
        ),
    ]