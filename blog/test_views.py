from django.test import TestCase

from .models import Post

# Create your tests here.

class TestDjango(TestCase):
    
    def test_view_test(self):
        page = self.client.get('/blog/test-posts.html')
        self.assertEqual(page.status_code, 200)
        
        
   
        
    def test_edit_post(self):
        post = Post(title='Create a Test')
        post.save()
        
        page = self.client.get("/posts/{0}/edit".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blog/form.html')

    
    
    def test_get_edit_page_for_post_that_doesnt_exist(self):
        page = self.client.get("/posts/1/edit")
        self.assertEqual(page.status_code, 404)
        
        
    
        
    
         
         
        