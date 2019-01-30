from django.test import TestCase
from .models import Product


class TestProductModel(TestCase):
    
    def test_post_str_is_title(self):
        product = Product(name='Write Tests')
        self.assertEqual(str(product), 'Write Tests')
        
    def test_cannot_create_product_without_name(self):
        product = Product(name='False', description=True, price=True)
        product.save()
        self.assertEqual(product.name, 'False')
        self.assertTrue(product.name)
        
    def test_cannot_create_product_without_price(self):
        product = Product(name='Create a Test', price=False)
        product.save()
        self.assertEqual(product.name, 'Create a Test')
        self.assertTrue(product.name)