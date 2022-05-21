from django.urls import path

from .views import MyTokenObtainPairView, get_product, get_products, get_routes

urlpatterns = [
    path("", get_routes, name="Route"),
    path("products/", get_products, name="Products"),
    path("products/<str:pk>/", get_product, name="Product"),
    path(
        "users/login/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
]
