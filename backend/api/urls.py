from django.urls import path

from .views import (
    MyTokenObtainPairView,
    get_product,
    get_products,
    get_routes,
    get_user_profile,
    get_users,
    register_user,
)

urlpatterns = [
    path("", get_routes, name="Route"),
    path("products/", get_products, name="Products"),
    path("products/<str:pk>/", get_product, name="Product"),
    path(
        "users/login/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("users/register/", register_user, name="register"),
    path("users/profile/", get_user_profile, name="users-profile"),
    path("users/", get_users, name="users"),
]
