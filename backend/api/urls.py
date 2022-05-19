from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import get_routes, get_products, get_product


urlpatterns = [
    path("", get_routes, name="Route"),
    path("users/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("products/", get_products, name="Products"),
    path("products/<str:pk>/", get_product, name="Product"),
]
