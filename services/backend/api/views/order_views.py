from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api.models import Order, OrderItem, Product, ShippingAddress
from api.serializers import OrderSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_order_items(request):
    user = request.user
    data = request.data
    order_items = data["orderItems"]
    if order_items and len(order_items) == 0:
        return Response(
            {"detail": "No Order Items"}, status=status.HTTP_400_BAD_REQUEST
        )

    # (1) Create order
    order = Order.objects.create(
        user=user,
        payment_method=data["paymentMethod"],
        taxPrice=data["taxPrice"],
        shippingPrice=data["shippingPrice"],
        totalPrice=data["totalPrice"],
    )
    # (2) Create shipping address
    shipping = ShippingAddress.objects.create(
        order=order,
        address=data["shippingAddress"]["address"],
        city=data["shippingAddress"]["city"],
        postalCode=data["shippingAddress"]["postalCode"],
        country=data["shippingAddress"]["country"],
    )
    shipping.save()
    # (3) Create order items and set order to orderItem relation
    for i in order_items:
        product = Product.objects.get(_id=i["product"])
        item = OrderItem.objects.create(
            product=product,
            order=order,
            name=product.name,
            qty=i["qty"],
            price=i["price"],
            image=product.image.url,
        )
        # (4) Update stock
        product.countInStock -= item.qty
        product.save()

    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_order_by_id(request, pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "Not authorized to view this order"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except Exception:
        return Response(
            {"detail": "Order does not exist"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_order_to_paid(request, pk):
    order = Order.objects.get(_id=pk)
    order.isPaid = True
    order.paidAt = datetime.now()
    order.save()
    return Response("Order was paid")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_orders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_order_to_delivered(request, pk):
    order = Order.objects.get(_id=pk)
    order.isDelivered = True
    order.deliveredAt = datetime.now()
    order.save()
    return Response("Order was paid")
