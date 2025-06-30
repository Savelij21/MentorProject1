from django.contrib.auth import get_user_model
from rest_framework.request import Request

from subscriptions.models import UserSubscription


User = get_user_model()


class AuthSelectiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.resources_for_auth = [
            "orders",
        ]

    def __call__(self, request: Request):
        # Если путь содержит проверяемый ресурс
        if any(
            resource in request.path
            for resource in self.resources_for_auth
        ):
            # проверяем аутентификацию и наличие подписки
            user: User = request.user
            if not user.is_authenticated:
                raise Exception("User is not authenticated")

            try:
                UserSubscription.objects.get(user=user)
            except UserSubscription.DoesNotExist:
                raise Exception("User has no subscription")

        return self.get_response(request)

        