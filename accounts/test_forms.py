from django.test import TestCase
from .forms import SignUpForm, ArtistForm, AddictForm

# Create your tests here.
class TestSignUpForm(TestCase):
    
     def test_can_create_user_with_just_first_name(self):
        form = SignUpForm({'first_name': 'Bob'})
        self.assertFalse(form.is_valid())
        
     def test_can_create_user_with_just_last_name(self):
        form = SignUpForm({'last_name': 'Bob'})
        self.assertFalse(form.is_valid())
       
    
     def test_email_is_required(self):
        form = SignUpForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])
        
     def test_last_name_is_required(self):
        form = SignUpForm({})
        self.assertFalse(form.is_valid())
        
        
     def test_first_name_is_required(self):
        form = SignUpForm({})
        self.assertFalse(form.is_valid())
        
        
     def test_image_is_required(self):
        form = SignUpForm({})
        self.assertFalse(form.is_valid())
        
     def test_can_create_user_with_just_email(self):
        form = SignUpForm({'email': 'email@hotmail.com'})
        self.assertFalse(form.is_valid())
        
        
class TestArtistForm(TestCase):
    
    
    def test_can_create_artist_with_just_bio(self):
        form = ArtistForm({'Bio': 'Bob'})
        self.assertTrue(form.is_valid())
        
        
    def test_can_create_artist_with_just_salon(self):
        form = ArtistForm({'salon': 'cork'})
        self.assertTrue(form.is_valid())
        
    def test_image_is_required(self):
        form = ArtistForm({})
        self.assertTrue(form.is_valid())
        
        
class TestAddictForm(TestCase):
    
    def test_image_is_required(self):
        form = AddictForm({})
        self.assertTrue(form.is_valid())
    
   
        
    
        
        
       