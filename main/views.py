from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductListSerializer, ProductDetailsSerializer

# Список товаров (FBV)
@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

# Детали товара (CBV)
class ProductDetailsView(APIView):
    def get(self, request, product_id,):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)