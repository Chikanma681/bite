from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('restaurants.urls')),
    path('', include('orders.urls')),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name = 'token_refresh'),
    path('api/token/blacklist /',TokenBlacklistView.as_view(), name = 'token_blacklist')
]
