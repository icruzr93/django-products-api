from django.test import TestCase
from ..models import Product


class ProductTest(TestCase):
    """ Test module for Product model """

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

    def test_product(self):
        product1 = Product.objects.get(code='HWR16-03')
        self.assertEqual(
            product1.get_price(), "HWR16-03 has a price of 500"
        )
        product2 = Product.objects.get(code='SPUD90-X')
        self.assertEqual(
            product2.get_price(), "SPUD90-X has a price of 750"
        )
        product3 = Product.objects.get(code='UDASL-EC60-X')
        self.assertEqual(
            product3.get_price(), "UDASL-EC60-X has a price of 1000"
        )
        product4 = Product.objects.get(code='UA80-X')
        self.assertEqual(
            product4.get_price(), "UA80-X has a price of 600"
        )
