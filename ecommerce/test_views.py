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
        # self.assertTemplateUsed(page, "ecommerce/form.html") 
        
        
        
    #   def test_edit_post(self):
    #     post = Post(title='Create a Test')
    #     post.save()
        
    #     page = self.client.get("/posts/{0}/edit".format(post.id))
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTemplateUsed(page, 'blog/form.html')
  

        
   
        
        
    
