from django.test import TestCase
from .models import Review, Comment
from ecommerce.models import Product


class TestDjango(TestCase):
    
    def test_make_review(self):
        product = Product(name='Create a Test', price=0)
        product.save()
        
        
        page = self.client.get('/review/{0}/form'.format(product.id) )
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'reviews/form.html')
        