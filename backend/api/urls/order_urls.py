from django.urls import path

from api.views.order_views import (
    add_order_items,
    get_order_by_id,
    get_orders,
    get_user_orders,
    update_order_to_paid,
)

urlpatterns = [
    path("<str:pk>/pay/", update_order_to_paid, name="pay"),
    path("<str:pk>/", get_order_by_id, name="user-order"),
    path("my-orders/", get_user_orders, name="my-orders"),
    path("add/", add_order_items, name="orders-add"),
    path("", get_orders, name="all-orders"),
]
