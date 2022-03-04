# Generated by Django 3.1 on 2022-03-04 16:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=datetime.datetime(2022, 3, 4, 17, 18, 37, 485635))),
                ('location', models.CharField(choices=[('city', 'city centre'), ('MOA', 'AMFI Moa')], max_length=4)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KRRR.customers')),
                ('products', models.ManyToManyField(to='KRRR.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2022, 3, 4, 17, 18, 37, 492638))),
                ('stars', models.CharField(choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Neutral'), ('4', 'Positive'), ('5', 'Excelant')], default='5', max_length=1)),
                ('content', models.CharField(blank=True, max_length=1000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KRRR.customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KRRR.products')),
            ],
        ),
    ]
