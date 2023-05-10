from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserAPIView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('auth/token/login/', UserLoginView.as_view(), name='user_login'),
    path('auth/token/', obtain_auth_token, name='token_obtain_pair'),
    path('auth/users/', UserRegistrationView.as_view(), name='user_registration'),
    path('auth/users/me/', UserAPIView.as_view(), name='user_profile'),
]
