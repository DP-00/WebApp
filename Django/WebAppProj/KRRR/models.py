#every time model is changed run:
#>python manage.py makemigrations appName

#command takes migration names and returns their SQL (doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django):
#>python manage.py sqlmigrate appName 0001

#to create those model tables in your database (run every time the model is changed)
#>python manage.py migrate

from django.db import models
from datetime import datetime

class Products(models.Model):
    label = models.CharField(max_length = 50)
    price = models.FloatField
    description = models.CharField(max_length = 250)
    photo = models.BinaryField
    sale_price = models.FloatField

class Customers(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    nickname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)

class Orders(models.Model):
    LOCATION_TYPE=(
        ('city', 'city centre'),
        ('MOA', 'AMFI Moa'),
    )
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    order_date = models.DateTimeField(default=datetime.now())
    location = models.CharField(max_length = 4, choices=LOCATION_TYPE)

class Comments(models.Model):
    STARS_TYPE=(
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Neutral'),
        ('4', 'Positive'),
        ('5', 'Excelant'),
    )
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=datetime.now())
    stars = models.CharField(max_length=1, choices=STARS_TYPE, default='5')
    content = models.CharField(max_length = 1000, blank=True)
    
