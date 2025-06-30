
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from subscriptions.models import Tariff, UserSubscription
from subscriptions.serializers import (
    TariffSerializer,
    UserSubscriptionSerializer,
    UserSubscriptionUpdateSerializer
)


class TariffsListAPIView(ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class UserSubscriptionsViewSet(ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

    def get_serializer_class(self):
        # Обновлять у подписки можно только тариф
        if self.action in ["update", "partial_update"]:
            return UserSubscriptionUpdateSerializer
        return super().get_serializer_class()
