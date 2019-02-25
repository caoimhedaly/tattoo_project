from django.test import TestCase
from .models import Product



class TestDjango(TestCase):
    
    
    
       
    def test_product_list(self):
        page = self.client.get('/ecommerce/product_list')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ecommerce/product_list.html')
        
        
    def test_edit_product(self):
        product = Product(name='Create a Test', price=0)
        product.save()
        
        page = self.client.get('/products/{0}/edit'.format(product.id))
        self.assertEqual(page.status_code, 302)
        
        
    def test_add_product(self):
        product = Product(name='Create a Test', price=0)
        product.save()
        
        page = self.client.get('/products/add')
        self.assertEqual(page.status_code, 302)
        
        
        
        
    
  

        
   
        
        
    
