# every time model is changed run:
# >python manage.py makemigrations appName

# command takes migration names and returns their SQL (doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django):
# >python manage.py sqlmigrate appName 0001

# to create those model tables in your database (run every time the model is changed)
# >python manage.py migrate

from unicodedata import category
from django.db import models
from datetime import datetime
from django.db.models import Min


class Product(models.Model):
    name = models.CharField(max_length=50)
    CATEGORY_TYPE = (
        ('E-bike', 'E-bike'),
        ('Bike', 'Bike'),
        ('Other', 'Other')
    )
    category = models.CharField(max_length=10, choices=CATEGORY_TYPE, default='Bike')
    price = models.FloatField()
    description = models.CharField(max_length=250)
    photo = models.FileField(blank=True)
    sale_price = models.FloatField(blank=True, null=True)

    def test1(self):
        return 42
    
    def test2(self):
        cheapestPrice = self.objects.all().aggregate(Min('price'))
        return cheapestPrice
        

    def cheapestBike(self):
        cheapestPrice = self.objects.filter(self__category="Bike").all().aggregate(Min('price'))
        return cheapestPrice
    
    def cheapestEBike(self):
        cheapestPrice = self.objects.filter(self__category="Bike").all().aggregate(Min('price'))
        return cheapestPrice
    
    def personalizationPrice(self):
        cheapestPrice = self.objects.filter(self__name="Personalization option").all().aggregate(Min('price'))
        return cheapestPrice



class Customer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Order(models.Model):
    LOCATION_TYPE = (
        ('city', 'city centre'),
        ('MOA', 'AMFI Moa'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(default=datetime.now())
    location = models.CharField(max_length=4, choices=LOCATION_TYPE)


class Comment(models.Model):
    STARS_TYPE = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Neutral'),
        ('4', 'Positive'),
        ('5', 'Excelant'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=datetime.now())
    stars = models.CharField(max_length=1, choices=STARS_TYPE, default='5')
    content = models.CharField(max_length=1000, blank=True)
