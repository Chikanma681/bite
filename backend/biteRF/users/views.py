from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from djoser.views import TokenCreateView
from .serializers import UserRegistrationSerializers, UserSerializer
from django.contrib.auth.models import Group

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(TokenCreateView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = request.user
            data = {
                'username': user.username,
                'email': user.email,
                'user_type': user.user_type
            }
           # Assign groups based on user type
            if user.user_type == 'C':
                # Customer group
                group = Group.objects.get(name='Customer')
                user.groups.add(group)
            elif user.user_type == 'D':
                # Driver group
                group = Group.objects.get(name='Driver')
                user.groups.add(group)
            elif user.user_type == 'R':
                # Restaurant group
                group = Group.objects.get(name='Restaurant')
                user.groups.add(group)

            response.data.update(data)
        return response