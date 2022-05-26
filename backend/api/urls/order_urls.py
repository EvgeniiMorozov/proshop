from django.urls import path

from api.views.order_views import add_order_items, get_order_by_id

urlpatterns = [
    path("add/", add_order_items, name="orders-add"),
    path("<str:pk>/", get_order_by_id, name="user-order"),
]
