from typing import override

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Order
from products.serializers import OrderSerializer, OrderUpdateSerializer
from products.utils import send_telegram_message

User = get_user_model()


class OrdersViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return OrderUpdateSerializer
        return super().get_serializer_class()

    @override
    def create(self, request, *args, **kwargs) -> Response:
        response: Response = super().create(request, *args, **kwargs)
        # Если указан tg_id - отправляем уведомление о созданном заказе
        user: User = request.user
        if user.tg_id:
            send_telegram_message(
                user_tg_id=user.tg_id,
                text=(
                    f"Оформлен заказ No{response.data['id']}\n\n"
                    f"{response.data['description']}"
                )
            )

        return response
