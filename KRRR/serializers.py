from pyexpat import model
from attr import fields
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'description', 'photo', 'salePrice')