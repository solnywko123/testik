from rest_framework import generics
from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EstablishmentListCreateView(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
