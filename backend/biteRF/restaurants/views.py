from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer
from .models import Restaurant, Menu, MenuItem
from django.shortcuts import get_object_or_404

class RestaurantView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(APIView):
    def get(self, request, pk):
        restaurant= get_object_or_404(Restaurant,pk)
        serialized_data = RestaurantSerializer(restaurant)
        return Response(serialized_data.data)