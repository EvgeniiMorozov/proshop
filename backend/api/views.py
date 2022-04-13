from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products_dev import products


def get_routes(request):
    return JsonResponse("Hello", safe=False)


@api_view(["GET"])
def get_products(request):
    return Response(products)


@api_view(["GET"])
def get_product(request, pk):
    product = next((el for el in products if el["_id"] == pk), None)
    return Response(product)
