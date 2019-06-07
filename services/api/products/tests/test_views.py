import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product
from ..serializers import ProductSerializer


client = Client()


class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            code="HWR16-03", position=1, quantity=1,
            image="01.png", price=500,
            description='Upright for room designs incl.'
        )
        Product.objects.create(
            code="SPUD90-X", position=2, quantity=1,
            image="02.png", price=750,
            description="XL Sink base unit 1 internal panel, 2 continuous doors"
        ),
        Product.objects.create(
            code="UDASL-EC60-X", position=3, quantity=1,
            image="03.png", price=1000,
            description="XL Base unit with waste separation system Euro-Cargo 1 internal panel,"
        ),
        Product.objects.create(
            code="UA80-X", position=4, quantity=1,
            image="04.png", price=600,
            description="XL Pull-out unit 1 drawer, 2 pull-outs"
        )

    def test_get_all_products(self):
        response = client.get(reverse('get_post_products'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(TestCase):
    """ Test module for GET single product API """

    def setUp(self):
        self.product1 = Product.objects.create(
            code="HWR16-03", position=1, quantity=1,
            image="01.png", price=500,
            description='Upright for room designs incl.'
        )
        self.product2 = Product.objects.create(
            code="SPUD90-X", position=2, quantity=1,
            image="02.png", price=750,
            description="XL Sink base unit 1 internal panel, 2 continuous doors"
        ),
        self.product3 = Product.objects.create(
            code="UDASL-EC60-X", position=3, quantity=1,
            image="03.png", price=1000,
            description="XL Base unit with waste separation system Euro-Cargo 1 internal panel,"
        ),
        self.product4 = Product.objects.create(
            code="UA80-X", position=4, quantity=1,
            image="04.png", price=600,
            description="XL Pull-out unit 1 drawer, 2 pull-outs"
        )

    def test_get_valid_single_product(self):
        response = client.get(
            reverse(
                'get_delete_update_product',
                kwargs={'pk': self.product1.pk}
            )
        )
        product = Product.objects.get(pk=self.product1.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse(
                'get_delete_update_product',
                kwargs={'pk': 30}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(TestCase):
    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            "code": "SPUD90-X",
            "position": 2,
            "quantity": 1,
            "image": "02.png",
            "price": 750,
            "description": "XL Sink base unit 1 internal panel, 2 continuous doors"
        }
        self.invalid_payload = {
            "code": "",
            "position": 2,
            "quantity": 1,
            "image": "",
            "price": 750,
            "description": "XL Sink base unit 1 internal panel, 2 continuous doors"
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('get_post_products'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProductTest(TestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.product1 = Product.objects.create(
            code="HWR16-03", position=1, quantity=1,
            image="01.png", price=500,
            description='Upright for room designs incl.'
        )
        self.valid_payload = {
            "code": "SPUD90-X",
            "position": 2,
            "quantity": 1,
            "image": "02.png",
            "price": 750,
            "description": "XL Sink base unit 1 internal panel, 2 continuous doors"
        }
        self.invalid_payload = {
            "code": "",
            "position": 2,
            "quantity": 1,
            "image": "",
            "price": 750,
            "description": "XL Sink base unit 1 internal panel, 2 continuous doors"
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse(
                'get_delete_update_product',
                kwargs={'pk': self.product1.pk}
            ),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_product(self):
        response = client.put(
            reverse(
                'get_delete_update_product',
                kwargs={'pk': self.product1.pk}
            ),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):
    """ Test module for deleting an existing product record """

    def setUp(self):
        self.product1 = Product.objects.create(
            code="HWR16-03", position=1, quantity=1,
            image="01.png", price=500,
            description='Upright for room designs incl.'
        )

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
