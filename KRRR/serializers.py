from pyexpat import model
from attr import fields
from rest_framework import serializers

from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price', 'description', 'photo', 'salePrice')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')