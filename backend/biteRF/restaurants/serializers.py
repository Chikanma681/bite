from rest_framework import serializers
from .models import Restaurant, Menu, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'restaurant','name')

class MenuSerializer(serializers.ModelSerializer):
    item_set = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'price','item_set')


class RestaurantSerializer(serializers.ModelSerializer):
    menu_set = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number', 'rating', 'menu_set')