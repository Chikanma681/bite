from django.urls import path
from .views import RestaurantList, RestaurantDetail, MenuList, MenuDetail, MenuItemList, MenuItemDetail

urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name='restaurant_list'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant_detail'),
    path('menus/', MenuList.as_view(), name='menu_list'),
    path('menus/<int:pk>/', MenuDetail.as_view(), name='menu_detail'),
    path('menu-items/', MenuItemList.as_view(), name='menu_item_list'),
    path('menu-items/<int:pk>/', MenuItemDetail.as_view(), name='menu_item_detail'),
]
