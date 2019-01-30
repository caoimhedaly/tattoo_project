from django.test import TestCase
from .models import Product
from .forms import ProductForm

# Create your tests here.

class TestProductForm(TestCase):
    
    def test_str(self):
        test_name= Product(name='A Product')
        self. assertEqual(str(test_name), 'A Product')
        
        
    def test_can_create_product_with_just_a_name(self):
        form = ProductForm({ 'name':'create product'})
        self.assertFalse(form.is_valid())
        
    def test_can_create_product_with_just_artist(self):
        form = ProductForm({ 'artist':'create product'})
        self.assertFalse(form.is_valid())
        
    def test_can_create_product_without_image(self):
        form = ProductForm({ 'image':''})
        self.assertFalse(form.is_valid())
      
    def test_can_create_product_without_price(self):
        form = ProductForm({ 'price':''})
        self.assertFalse(form.is_valid())
        
        
    def test_can_create_product_without_description(self):
        form = ProductForm({ 'description':''})
        self.assertFalse(form.is_valid())
        
    def test_can_create_product_without_sku(self):
        form = ProductForm({ 'sku':''})
        self.assertFalse(form.is_valid())
        
    def test_can_create_product_without_stock(self):
        form = ProductForm({ 'stock':''})
        self.assertFalse(form.is_valid())
        
        
    def test_correct_message_for_missing_name(self):
        form = ProductForm({ 'name':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        
    def test_correct_message_for_missing_description(self):
        form = ProductForm({ 'description':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
        
    def test_correct_message_for_missing_price(self):
        form = ProductForm({ 'price':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['price'], [u'This field is required.'])
        
    def test_correct_message_for_missing_stock(self):
        form = ProductForm({ 'stock':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['stock'], [u'This field is required.'])
        
    def test_correct_message_for_missing_sku(self):
        form = ProductForm({ 'sku':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['sku'], [u'This field is required.'])
        
    def test_correct_message_for_missing_artist(self):
        form = ProductForm({ 'artist':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['artist'], [u'This field is required.'])
        
    def test_correct_message_for_missing_image(self):
        form = ProductForm({ 'image':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['image'], [u'This field is required.'])
   
        

        
        
    
    