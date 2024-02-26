# inventory_app/urls.py
from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    EstablishmentListCreateView,
    EstablishmentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
    path('establishments/', EstablishmentListCreateView.as_view()),
    path('establishments/<int:pk>/', EstablishmentRetrieveUpdateDestroyView.as_view()),
]
