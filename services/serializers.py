from rest_framework import serializers
from .models import Product, Customer, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email']


class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'quantity', 'date']
