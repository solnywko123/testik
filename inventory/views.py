from rest_framework import generics
from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer

from rest_framework.pagination import PageNumberPagination


class StandartPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page'


class ProductListCreateView(generics.ListCreateAPIView):
    pagination_class = StandartPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EstablishmentListCreateView(generics.ListCreateAPIView):
    pagination_class = StandartPagination
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
