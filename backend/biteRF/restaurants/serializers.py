from rest_framework import serializers
from .models import Restaurant, Menu, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source='image.url', read_only=True)
    class Meta:
        model = MenuItem
        fields = ('id', 'menu','name','price','image')

class MenuSerializer(serializers.ModelSerializer):
    item_set = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'restaurant','item_set')


class RestaurantSerializer(serializers.ModelSerializer):
    menu_set = MenuSerializer(many=True, read_only=True)
    logo = serializers.URLField(source='logo.url', read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'menu_set','logo')