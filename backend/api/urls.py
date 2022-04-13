from django.urls import path
from .views import get_routes, get_products


urlpatterns = [
    path("", get_routes, name="Route"),
    path("products/", get_products, name="Products"),
]
