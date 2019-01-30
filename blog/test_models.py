from django.test import TestCase
from .models import Post



class TestPostModel(TestCase):
    
    def test_post_str_is_title(self):
        post = Post(title='Write Tests')
        self.assertEqual(str(post), 'Write Tests')
    
    def test_views_defaults_to_0(self):
        post = Post(title='Create a Test')
        post.save()
        self.assertEqual(post.title, 'Create a Test')
        self.assertEqual(post.views, 0)
        
    def test_can_create_post_with_title_and_content(self):
        post = Post(title='Create a Test', content=True)
        post.save()
        self.assertEqual(post.title, 'Create a Test')
        self.assertTrue(post.content)
        
    def test_cannot_create_post_without_content(self):
        post = Post(title='Create a Test', content=False)
        post.save()
        self.assertEqual(post.title, 'Create a Test')
        self.assertTrue(post.title)
        
    def test_can_create_post_without_tags(self):
        post = Post(title='Create a Test', tags=False)
        post.save()
        self.assertEqual(post.title, 'Create a Test')
        self.assertFalse(post.tags)
        
   
        
        
    
            
    
        
    
    
    