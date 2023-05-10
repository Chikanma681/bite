from django.db import models
from django.contrib.auth.models import AbstractUser #, Group, Permission

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('C', 'Customer'),
        ('D', 'Driver'),
        ('R', 'Restaurant'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default='C')
    # Set the username field to be optional
    # Add a unique related name to the groups and user_permissions fields
    # groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    # user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)
