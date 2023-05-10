from djoser.serializers import UserCreateSerializer, UserSerializer 
from rest_framework import serializers
from .models import User

class UserRegistrationSerializers(UserCreateSerializer):
    user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)

    # make the client use username as email
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id','username', 'password','first_name','last_name','user_type']

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        # make the client use username as email
        model = User
        fields = ['id','username','password','first_name','last_name','user_type']



# from django.contrib.auth import get_user_model
# from rest_framework import serializers

# User = get_user_model()

# class UserRegistrationSerializers(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, min_length=6, write_only=True)
#     user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'username', 'password', 'user_type')

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             username=validated_data['username'],
#             password=validated_data['password'],
#             user_type=validated_data['user_type']
#         )
#         return user