
# Models: Define the database schema and data types for your app's data.
# Serializers: Convert the database data to JSON or other formats that can be returned by the API.
# Views: Define the API endpoints, which specify what data can be retrieved, updated, or deleted.
# URLs: Map the views to specific URLs, so they can be accessed by clients.
# Here's an example of what this might look like:

from django.db import models
# from django.conf import settings

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    logo = models.URLField()

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField()




# Serializers:
# kotlin
# Copy code


# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = ('id', 'name', 'price')

# class RestaurantSerializer(serializers.ModelSerializer):
#     menu_set = MenuSerializer(many=True, read_only=True)

#     class Meta:
#         model = Restaurant
#         fields = ('id', 'name', 'address', 'phone_number', 'rating', 'menu_set')
# Views:
# python
# Copy code
# from rest_framework import generics
# from .models import Restaurant, Menu
# from .serializers import RestaurantSerializer, MenuSerializer

# class RestaurantList(generics.ListCreateAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class MenuList(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

# class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
# URLs:
# lua
# Copy code
# from django.urls import path
# from .views import RestaurantList, RestaurantDetail, MenuList, MenuDetail

# urlpatterns = [
#     path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),
#     path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
#     path('menus/', MenuList.as_view(), name='menu-list'),
#     path('menus/<int:pk>/', MenuDetail.as_view(), name='menu-detail'),
# ]