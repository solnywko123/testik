from django.urls import path
from .views import ProductListCreateView, EstablishmentListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('establishments/', EstablishmentListCreateView.as_view(), name='establishment-list-create'),
]
