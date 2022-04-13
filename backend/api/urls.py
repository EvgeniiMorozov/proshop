from django.urls import path
from .views import get_routes, get_products, get_product


urlpatterns = [
    path("", get_routes, name="Route"),
    path("products/", get_products, name="Products"),
    path("product/<str:pk>/", get_product, name="Product"),
]
