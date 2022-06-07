from django.urls import path

from api.views.product_views import (
    create_product,
    create_product_review,
    delete_product,
    get_product,
    get_products,
    get_top_products,
    update_product,
    upload_image,
)

urlpatterns = [
    path("<int:pk>/reviews/", create_product_review, name="review-create"),
    path("update/<int:pk>/", update_product, name="product-update"),
    path("delete/<int:pk>/", delete_product, name="product-delete"),
    path("upload/", upload_image, name="image-upload"),
    path("create/", create_product, name="product-create"),
    path("<int:pk>/", get_product, name="product"),
    path("top/", get_top_products, name="top-products"),
    path("", get_products, name="products"),
]
