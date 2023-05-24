from django.db import models
from user.model import User
from restaurants.model import MenuItem

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(MenuItem)
    quantity = models.PositiveIntegerField()
    special_instructions = models.TextField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
