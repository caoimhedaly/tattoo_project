from django.test import TestCase

from .models import Post

# Create your tests here.

class TestDjango(TestCase):
    
    def test_view_test(self):
        page = self.client.get('/blog/test-posts.html')
        self.assertEqual(page.status_code, 200)
        
        
    # def test_post_like(self):
    #     post = Post(title='Create a Test')
    #     post.save()
    #     page = self.client.get('posts/{0}/read/like')
    #     self.assertEqual(page.status_code, 200)
       
    # def test_add_post(self):
    #     resp= self.client.post('/posts/add/', {'title': 'Write Test'})
    #     self.assertEqual(resp.status_code, 302)
    #     # test for a return redirect/post   
     
        
        
    # def test_add_post(self):
    #     page = self.client.get("/posts/add")
    #     self.assertEqual(page.status_code, 302)
    #     self.assertRedirects(page, '/posts/add')
    
    
    # def test_add_post(self):
    #     page=self.client.get("/blog/form.html")
    #     self.assertEqual(page.status_code, 200)
        
    def test_edit_post(self):
        post = Post(title='Create a Test')
        post.save()
        
        page = self.client.get("/posts/{0}/edit".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'blog/form.html')
        
    def test_read_post(self):
        post = Post(title= 'Create a Test')
        post.save()
         
        page = self.client.get("/posts/{0}/read".format(post.id))
        self.assertEqual(page.status_code, 200)
        # self.assertTemplateUsed(page, "blog/read_post.html")
    
    
    def test_get_edit_page_for_post_that_doesnt_exist(self):
        page = self.client.get("/posts/1/edit")
        self.assertEqual(page.status_code, 404)
        
        
    
         
         
        