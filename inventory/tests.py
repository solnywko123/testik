from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer


class ProductTests(APITestCase):
    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '19.99',
            'quantity': 10,
        }
        self.product = Product.objects.create(**self.product_data)
        self.url = reverse('product-list')

    def test_create_product(self):
        response = self.client.post(self.url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_product_list(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the expected product data matches the returned product data
        expected_product_data = self.product_data
        returned_products = response.data['results']

        # Assuming that the first product in the list is the one created in the setUp method
        self.assertEqual(len(returned_products), 1)

        returned_product = returned_products[0]
        for key, value in expected_product_data.items():
            self.assertEqual(returned_product[key], value)

        # Alternatively, you can use the ProductSerializer for more precise comparison
        serializer = ProductSerializer(instance=self.product)
        self.assertEqual(returned_product, serializer.data)


    def test_retrieve_single_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.id})
        updated_data = {'name': 'Updated Product', 'price': 20.99,
                        'description': 'Updated Description', 'quantity': 5}

        response = self.client.put(url, updated_data, format='json')

        # Use self.fail() to print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data['name'], updated_data['name'])


class EstablishmentTests(APITestCase):
    def setUp(self):
        self.establishment_data = {
            'name': 'Test Establishment',
            'description': 'Test Description',
            'places': 50,
            'hours_of_operation': '9 AM - 5 PM',
            'requirements': 'Test Requirements',
        }
        self.establishment = Establishment.objects.create(**self.establishment_data)
        self.url = reverse('establishment-list')

    def test_create_establishment(self):
        response = self.client.post(self.url, self.establishment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_establishment_list(self):
        response = self.client.get(reverse('establishment-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the expected establishment data matches the returned establishment data
        expected_establishment_data = self.establishment_data
        returned_establishments = response.data['results']

        # Assuming that the first establishment in the list is the one created in the setUp method
        self.assertEqual(len(returned_establishments), 1)

        returned_establishment = returned_establishments[0]
        for key, value in expected_establishment_data.items():
            self.assertEqual(returned_establishment[key], value)

        # Alternatively, you can use the EstablishmentSerializer for more precise comparison
        serializer = EstablishmentSerializer(instance=self.establishment)
        self.assertEqual(returned_establishment, serializer.data)



    def test_retrieve_single_establishment(self):
        url = reverse('establishment-detail', kwargs={'pk': self.establishment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.establishment.name)

    def test_update_establishment(self):
        url = reverse('establishment-detail', kwargs={'pk': self.establishment.id})
        updated_data = {
            'name': 'Updated Establishment',
            'description': 'Updated Description',
            'places': 60,
            'hours_of_operation': 'Updated Hours',
            'requirements': 'Updated Requirements',
        }
        response = self.client.put(url, updated_data, format='json')

        # Use self.fail() to print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(response.data['name'], updated_data['name'])

    def test_delete_establishment(self):
        url = reverse('establishment-detail', kwargs={'pk': self.establishment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Establishment.objects.count(), 0)
