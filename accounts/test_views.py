from django.test import TestCase



class TestDjango(TestCase):
    
       
    def test_get_index(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')
        
        

    
    def test_get_read_profile(self):
        page = self.client.get('/accounts/profile/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'profile2.html')
        
        
  

        
    def test_get_signup(self):
        page = self.client.get('/register/signup')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'signup.html')   
        
        