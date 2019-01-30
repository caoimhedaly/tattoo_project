from django.test import TestCase
from .forms import PostForm

# Create your tests here.

class TestBlogForm(TestCase):
    
    def test_can_create_post_with_just_a_title(self):
        form = PostForm({ 'title':'create blog'})
        self.assertFalse(form.is_valid())
        
        
    
    def test_can_create_post_with_just_content(self):
        form = PostForm({ 'content':'create blog'})
        self.assertFalse(form.is_valid())
        
    def test_can_create_post_without_image(self):
        form = PostForm({ 'image':''})
        self.assertFalse(form.is_valid())
        
    def test_can_create_post_without_tags(self):
        form = PostForm({ 'tags':''})
        self.assertFalse(form.is_valid())
        
        
    def test_correct_message_for_missing_title(self):
        form = PostForm({ 'title':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
    def test_correct_message_for_missing_content(self):
        form = PostForm({ 'content':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
        
    def test_correct_message_for_missing_image(self):
        form = PostForm({ 'image':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['image'], [u'This field is required.'])
        
   
        
   
            
 
       
        
    
    
        
    
    

        
    
    
