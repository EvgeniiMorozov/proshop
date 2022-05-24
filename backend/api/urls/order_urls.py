from django.urls import path

from api.views.order_views import add_order_items

urlpatterns = [
    path("add/", add_order_items, name="orders-add"),
]
