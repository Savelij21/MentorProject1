from django.urls import path
from subscriptions import views

urlpatterns = [

    path("tariffs/", views.TariffsListAPIView.as_view(), name="tariffs_list"),

    path("subscriptions/", views.UserSubscriptionsViewSet.as_view({
        "get": "list",
        "post": "create",
    }), name="subscriptions"),
    path("subscriptions/<int:pk>/", views.UserSubscriptionsViewSet.as_view({
        "get": "retrieve",
        "patch": "partial_update",
        "delete": "destroy",
    }), name="subscription"),

]