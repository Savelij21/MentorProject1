
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from subscriptions.models import Tariff, UserSubscription
from subscriptions.serializers import (
    TariffSerializer,
    UserSubscriptionSerializer,
    UserSubscriptionUpdateSerializer
)


class TariffsListAPIView(ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    permission_classes = [IsAuthenticated]


class UserSubscriptionsViewSet(ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Юзер видит только свои подписки
        return UserSubscription.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        # Обновлять у подписки можно только тариф
        if self.action in ["update", "partial_update"]:
            return UserSubscriptionUpdateSerializer
        return super().get_serializer_class()
