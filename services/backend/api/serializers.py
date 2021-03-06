from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Order, OrderItem, Product, Review, ShippingAddress


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "_id", "username", "email", "name", "isAdmin"]

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "_id", "username", "email", "name", "isAdmin", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    numReviews = serializers.SerializerMethodField(read_only=True)
    countInStock = serializers.SerializerMethodField(read_only=True)
    createdAt = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def get_numReviews(self, obj):
        return obj.num_reviews

    def get_countInStock(self, obj):
        return obj.count_in_stock

    def get_createdAt(self, obj):
        return obj.created_at

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    createdAt = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

    def get_createdAt(self, obj):
        return obj.created_at


class ShippingAddressSerializer(serializers.ModelSerializer):
    postalCode = serializers.SerializerMethodField(read_only=True)
    shippingPrice = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ShippingAddress
        fields = "__all__"

    def get_postalCode(self, obj):
        return obj.postal_code

    def get_shippingPrice(self, obj):
        return obj.shipping_price


class OrderSerializer(serializers.ModelSerializer):
    taxPrice = serializers.SerializerMethodField(read_only=True)
    shippingPrice = serializers.SerializerMethodField(read_only=True)
    totalPrice = serializers.SerializerMethodField(read_only=True)
    isPaid = serializers.SerializerMethodField(read_only=True)
    paidAt = serializers.SerializerMethodField(read_only=True)
    isDelivered = serializers.SerializerMethodField(read_only=True)
    deliveredAt = serializers.SerializerMethodField(read_only=True)
    createdAt = serializers.SerializerMethodField(read_only=True)

    paymentMethod = serializers.SerializerMethodField(read_only=True)
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    def get_createdAt(self, obj):
        return obj.created_at

    def get_deliveredAt(self, obj):
        return obj.delivered_at

    def get_isDelivered(self, obj):
        return obj.is_delivered

    def get_paidAt(self, obj):
        return obj.paid_at

    def get_isPaid(self, obj):
        return obj.is_paid

    def get_totalPrice(self, obj):
        return obj.total_price

    def get_shippingPrice(self, obj):
        return obj.shipping_price

    def get_taxPrice(self, obj):
        return obj.tax_price

    def get_paymentMethod(self, obj):
        return obj.payment_method

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(
                obj.shippingaddress,
                many=False,
            ).data
        except Exception:
            address = False

        return address

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
