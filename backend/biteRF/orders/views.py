from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, MenuItem
from .serializers import OrderSerializer

class OrderView(APIView):
    def get(self, request, order_id=None):
        if order_id:
            # Retrieve a specific order
            order = Order.objects.get(pk=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            # Retrieve a list of orders
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
            
class PlaceOrderView(APIView):
    def post(self, request):
        menu_item_ids = request.data.get('menu_items')
        quantity = int(request.data.get('quantity'))
        special_instructions = request.data.get('special_instructions')

        # Retrieve the menu items and calculate the total price
        menu_items = MenuItem.objects.filter(id__in=menu_item_ids)
        total_price = sum(menu_item.price * quantity for menu_item in menu_items)

        # Create the order instance
        order = Order.objects.create(
            customer=request.user,
            quantity=quantity,
            special_instructions=special_instructions,
            total_price=total_price,
            status='Placed'
        )

        # Add selected menu items to the order
        order.menu_items.set(menu_item_ids)

        serializer = OrderSerializer(order)
        return Response(serializer.data)
