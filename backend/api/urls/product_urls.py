from django.urls import path

from api.views.product_views import delete_product, get_product, get_products

urlpatterns = [
    path("", get_products, name="products"),
    path("<str:pk>/", get_product, name="product"),
    path("delete/<str:pk>/", delete_product, name="product-delete"),
]
