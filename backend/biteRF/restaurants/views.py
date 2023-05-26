from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Restaurant, Menu, MenuItem
from .serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer
import boto3
from io import BytesIO

def upload_image_to_s3(file_content, bucket_name, key):
    s3_client = boto3.client('s3')
    file_object = BytesIO(file_content)
    s3_client.upload_fileobj(file_object, bucket_name, key)

def get_s3_image_url(bucket_name, key):
    s3_resource = boto3.resource('s3')
    # trunk-ignore(ruff/F841)
    bucket = s3_resource.Bucket(bucket_name)
    object_url = f"https://s3.amazonaws.com/{bucket_name}/{key}"
    return object_url

class RestaurantList(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            # Get the uploaded image file
            logo_file = request.data.get('logo')

            # Handle the image file and get the content
            image_content = logo_file.read()

            # Generate a unique key for the image file
            key = f'restaurant/logos/{logo_file.name}'

            # Upload the image file to S3
            upload_image_to_s3(image_content, settings.AWS_STORAGE_BUCKET_NAME, key)

            # Get the S3 image URL
            image_url = get_s3_image_url(settings.AWS_STORAGE_BUCKET_NAME, key)
            print("IMAGE URL:", image_url)
            # Save the restaurant with the image URL
            serializer.save(logo=image_url)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetail(APIView):
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, pk):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant,pk=pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuList(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetail(APIView):
    def get(self, request, pk):
        menu = get_object_or_404(Menu,pk=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def put(self, request, pk):
        menu = get_object_or_404(Menu,pk=pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        menu = get_object_or_404(Menu,pk=pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MenuItemList(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = MenuItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         image_file = request.data.get('image')
    #         if image_file:
    #             serializer.validated_data['image'] = image_file
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            # Get the uploaded image file
            image_file = request.data.get('image')

            # Handle the image file and get the content
            image_content = image_file.read()

            # Generate a unique key for the image file
            key = f'menu-items/images/{image_file.name}'

            # Upload the image file to S3
            upload_image_to_s3(image_content, settings.AWS_STORAGE_BUCKET_NAME, key)

            # Get the S3 image URL
            image_url = get_s3_image_url(settings.AWS_STORAGE_BUCKET_NAME, key)
            print("IMAGE URL:", image_url)
            # Save the restaurant with the image URL
            serializer.save(image=image_url)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuItemDetail(APIView):
    def get(self, request, pk):
        menu_item = get_object_or_404(Restaurant,pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)

    def put(self, request, pk):
        menu_item = get_object_or_404(Restaurant,pk)
        serializer = MenuItemSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        menu = get_object_or_404(MenuItem,pk=pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)