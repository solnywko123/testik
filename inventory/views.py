from rest_framework import generics
from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer
from rest_framework.pagination import PageNumberPagination


class StandartPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Class for creating and retrieving a list of products.

    Supported methods:
    - GET: Get a list of all products with pagination.
    - POST: Create a new product.

    Request parameters:
    - page: Page number for pagination.

    Request body (for POST method):
    - name (string): Product name.
    - description (string): Product description.
    - price (number): Product price.
    - quantity (number): Quantity of products.

    Example response (for GET method):
    [
        {
            "id": 1,
            "name": "Product 1",
            "price": 10.99
        },
        {
            "id": 2,
            "name": "Product 2",
            "price": 20.50
        },
        ...
    ]
    """
    pagination_class = StandartPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class for retrieving, updating, and deleting a specific product.

    Supported methods:
    - GET: Get information about a specific product.
    - PUT: Update information about a specific product.
    - DELETE: Delete a specific product.

    Request parameters:
    - id (number): Product identifier.

    Request body (for PUT method):
    - name (string): New product name.
    - price (number): New product price.

    Example response (for GET method):
    {
        "id": 1,
        "name": "Product 1",
        "price": 10.99
    }
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EstablishmentListCreateView(generics.ListCreateAPIView):
    """
    Class for creating and retrieving a list of establishments.

    Supported methods:
    - GET: Get a list of all establishments with pagination.
    - POST: Create a new establishment.

    Request parameters:
    - page: Page number for pagination.

    Request body (for POST method):
    - name
    - location
    - description
    - places
    - hours_of_operation
    - requirements

    Example response (for GET method):
    [
        {
            "id": 1,
            "name": "Establishment 1",
            "location": "City 1"
        },
        {
            "id": 2,
            "name": "Establishment 2",
            "location": "City 2"
        },
        ...
    ]
    """
    pagination_class = StandartPagination
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class for retrieving, updating, and deleting a specific establishment.

    Supported methods:
    - GET: Get information about a specific establishment.
    - PUT: Update information about a specific establishment.
    - DELETE: Delete a specific establishment.

    Request parameters:
    - id (number): Establishment identifier.

    Request body (for PUT method):
    - name (string): New establishment name.
    - location (string): New establishment location.

    Example response (for GET method):
    {
        "id": 1,
        "name": "Establishment 1",
        "location": "City 1"
    }
    """
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

