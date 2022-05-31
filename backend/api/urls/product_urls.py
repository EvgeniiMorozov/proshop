from django.urls import path

from api.views.product_views import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product,
    upload_image,
)

urlpatterns = [
    path("update/<int:pk>/", update_product, name="product-update"),
    path("delete/<int:pk>/", delete_product, name="product-delete"),
    path("upload/", upload_image, name="image-upload"),
    path("create/", create_product, name="product-create"),
    path("<int:pk>/", get_product, name="product"),
    path("", get_products, name="products"),
]
