from django.urls import path
from products import views

urlpatterns = [

    path("orders/", views.OrdersViewSet.as_view({
        "get": "list",
        "post": "create",
    }), name="orders"),
    path("orders/<int:pk>/", views.OrdersViewSet.as_view({
        "get": "retrieve",
        "patch": "partial_update",
        "delete": "destroy",
    }), name="order"),

]