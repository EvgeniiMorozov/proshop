from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.models import Product, Review
from api.serializers import ProductSerializer


@api_view(["GET"])
def get_products(request):
    query = request.query_params.get("keyword")
    if query is None:
        query = ""

    products = Product.objects.filter(name__icontains=query)

    page = request.query_params.get("page")
    paginator = Paginator(products, 5)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page is None:
        page = 1

    page = int(page)

    serializer = ProductSerializer(products, many=True)
    return Response(
        {
            "products": serializer.data,
            "page": page,
            "pages": paginator.num_pages,
        }
    )


@api_view(["GET"])
def get_top_products(request):
    products = Product.objects.filter(rating__gte=4).order_by("-rating")[:5]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_product(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response("Product deleted")


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_product(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        name="Sample name",
        price=0,
        brand="Sample brand",
        countInStock=0,
        category="Sample category",
        description="",
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_product(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data["name"]
    product.price = data["price"]
    product.brand = data["brand"]
    product.countInStock = data["countInStock"]
    product.category = data["category"]
    product.description = data["description"]

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def upload_image(request):
    data = request.data
    product_id = data["product_id"]
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get("image")
    product.save()
    return Response("Image was uploaded")


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_product_review(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    data = request.data

    if product.review_set.filter(user=user).exists():
        content = {"detail": "Product already reviewed"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif data["rating"] == 0:
        content = {"detail": "Please select a rating"}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = product.review_set.all()
        product.numReviews = len(reviews)
        total = sum(i.rating for i in reviews)
        product.rating = total / len(reviews)
        product.save()
        return Response({"detail": "Review added"})
