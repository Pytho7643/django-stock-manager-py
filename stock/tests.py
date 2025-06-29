from django.test import TestCase

# Create your tests here.

from django.urls import reverse

class StockIndexViewTests(TestCase):
    def test_no_products(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products available.")
        self.assertEqual(list(response.context['product_list']), [])

    def test_one_product(self):
        create_product(name="TestProduct", price=5.0, quantity=10)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestProduct")
        self.assertEqual(len(response.context['product_list']), 1)

    def test_multiple_products(self):
        create_product(name="Apple", price=2.0, quantity=200)
        create_product(name="Orange", price=2.5, quantity=250)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apple")
        self.assertContains(response, "Orange")
        self.assertEqual(len(response.context['product_list']), 2)

    def test_detail_view_with_invalid_product(self):
        response = self.client.get(reverse('detail', args=(999,)))
        self.assertEqual(response.status_code, 404)
    
    def test_detail_view_with_one_product(self):
        product = create_product(name="TestProduct", price=5.0, quantity=10)
        response = self.client.get(reverse('detail', args=(product.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestProduct")

from .models import Product

def create_product(name, price=0.0, quantity=0):
    return Product.objects.create(name=name, price=price, quantity=quantity)

class StockAddProductViewTests(TestCase):
    def test_add_product_get(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add a new product")

    def test_add_product_post(self):
        response = self.client.post(reverse('add_product'), {
            'name': 'testproduct',
            'price': 10.0,
            'quantity': 5,
        })
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Product.objects.filter(name='testproduct').exists())

