from django.db import models
# from users.models import User
from restaurants.models import MenuItem
from django.conf import settings

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    quantity = models.PositiveIntegerField()
    special_instructions = models.TextField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
