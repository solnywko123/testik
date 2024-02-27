# inventory_app/urls.py
from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    EstablishmentListCreateView,
    EstablishmentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('establishments/', EstablishmentListCreateView.as_view(), name='establishment-list'),
    path('establishments/<int:pk>/', EstablishmentRetrieveUpdateDestroyView.as_view(), name='establishment-detail'),
]
