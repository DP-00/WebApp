# every time model is changed run:
# >python manage.py makemigrations appName

# command takes migration names and returns their SQL (doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django):
# >python manage.py sqlmigrate appName 0001

# to create those model tables in your database (run every time the model is changed)
# >python manage.py migrate

from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# from django.db.models import F, Q
from django.db.models.constraints import CheckConstraint, UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=50)
    CATEGORY_TYPE = (
        ('E-bike', 'E-bike'),
        ('Bike', 'Bike'),
        ('Other', 'Other')
    )
    category = models.CharField(max_length=10, choices=CATEGORY_TYPE, default='Bike')
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    photo = models.FileField(blank=True, upload_to='products')
    salePrice = models.IntegerField(blank=True, null=True)

    def clean(self):
        if (self.salePrice is not None) and (self.salePrice >= self.price):
            raise ValidationError({'salePrice':_('Sale price must be lower than normal price.')})


class Order(models.Model):
    LOCATION_TYPE = (
        ('city', 'city centre'),
        ('MOA', 'AMFI Moa'),
    )
    ORDER_STATUS = (
        ('cart', 'still shopping'),
        ('paid', 'shopping compleated'),
        ('done', 'order compleated'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=datetime.now())
    location = models.CharField(max_length=4, choices=LOCATION_TYPE, default='city')
    status = models.CharField(max_length=4, choices=ORDER_STATUS, default='cart')

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Comment(models.Model):
    STARS_TYPE = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Neutral'),
        ('4', 'Positive'),
        ('5', 'Excelant'),
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=datetime.now())
    stars = models.CharField(max_length=1, choices=STARS_TYPE, default='5')
    content = models.CharField(max_length=1000, blank=True)
    class Meta:
        constraints = [
            UniqueConstraint(fields=['customer', 'product','stars'], name='unique_stars'),
            UniqueConstraint(fields=['customer', 'product','content'], name='unique_review') 
        ]


