from django.urls import path

from api.views.product_views import (
    create_product,
    delete_product,
    get_product,
    get_products,
)

urlpatterns = [
    path("", get_products, name="products"),
    path("<str:pk>/", get_product, name="product"),
    path("create/", create_product, name="product-create"),
    path("update/<str:pk>/", delete_product, name="product-update"),
    path("delete/<str:pk>/", delete_product, name="product-delete"),
]
