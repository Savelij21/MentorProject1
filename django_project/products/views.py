from rest_framework.viewsets import ModelViewSet

from products.models import Order
from products.serializers import OrderSerializer, OrderUpdateSerializer


class OrdersViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return OrderUpdateSerializer
        return super().get_serializer_class()
