from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from .viewsets import CartItemViewSet, ProductViewSet
from .models import Product, CartItem, ProductProperty


class TestCartItemViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse("cart_item-list")
        self.view = CartItemViewSet.as_view(
            {"post": "create", "get": "retrieve", "delete": "destroy"}
        )
        self.user = User.objects.create(
            username="test", password="test", email="usery@test.com"
        )
        self.product = Product.objects.create(title="Test product", sku="test sku")

    def test_create_unauthorized(self):
        request = self.factory.post(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create(self):
        request = self.factory.post(self.url, {"product": self.product.id, "amount": 5})
        force_authenticate(request, user=self.user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["product"], self.product.id)
        self.assertEqual(response.data["amount"], 5)

    def test_create_add_amount(self):
        request_1 = self.factory.post(
            self.url, {"product": self.product.id, "amount": 5}
        )
        force_authenticate(request_1, user=self.user)
        response_1 = self.view(request_1)

        request_2 = self.factory.post(
            self.url, {"product": self.product.id, "amount": 5}
        )
        force_authenticate(request_2, user=self.user)
        response_2 = self.view(request_2)

        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.data["product"], self.product.id)
        self.assertEqual(response_2.data["amount"], 10)
        self.assertEqual(response_1.data["id"], response_2.data["id"])
        self.assertEqual(CartItem.objects.count(), 1)

    def test_delete(self):
        item = CartItem.objects.create(user=self.user, product=self.product, amount=10)
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=item.pk)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CartItem.objects.count(), 0)

    def test_get(self):
        item = CartItem.objects.create(user=self.user, product=self.product, amount=10)
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=item.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": item.id,
                "amount": 10,
                "product": {
                    "id": self.product.id,
                    "title": self.product.title,
                    "sku": self.product.sku,
                    "short": None,
                    "price": 0.0,
                },
            },
        )

    def test_list(self):
        CartItem.objects.create(user=self.user, product=self.product, amount=10)
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        view = CartItemViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update(self):
        request = self.factory.put(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TestProductViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse("product-list")
        self.view = ProductViewSet.as_view({"get": "list"})

    def test_list(self):
        product_1 = Product.objects.create(
            title="Test product 1",
            sku="test sku 1",
            price=10,
            short="short desc",
            full="full desc",
        )
        Product.objects.create(title="Test product 2", sku="test sku 2", price=20)
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            response.data[0],
            {
                "id": product_1.id,
                "title": product_1.title,
                "sku": product_1.sku,
                "short": product_1.short,
                "price": product_1.price,
            },
        )

    def test_get(self):
        product = Product.objects.create(
            title="Test product 1",
            sku="test sku 1",
            price=10,
            short="short desc",
            full="full desc",
        )
        prop_1 = ProductProperty.objects.create(
            product=product, title="prop title 1", value="prop value 1"
        )
        prop_2 = ProductProperty.objects.create(
            product=product, title="prop title 2", value="prop value 2"
        )
        request = self.factory.get(self.url)
        view = ProductViewSet.as_view({"get": "retrieve"})
        response = view(request, pk=product.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": product.id,
                "title": product.title,
                "sku": product.sku,
                "short": product.short,
                "full": product.full,
                "price": 10.0,
                "properties": [
                    {"id": prop_1.id, "title": prop_1.title, "value": prop_1.value},
                    {"id": prop_2.id, "title": prop_2.title, "value": prop_2.value},
                ],
            },
        )

    def test_create(self):
        request = self.factory.post(self.url)
        response = self.view(request, {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update(self):
        request = self.factory.put(self.url)
        response = self.view(request, {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete(self):
        request = self.factory.delete(self.url)
        response = self.view(request, {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
