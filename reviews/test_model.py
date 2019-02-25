from django.test import TestCase
from .models import Review, Comment



class TestReviewtModel(TestCase):
    
    def test_review_str_is_title(self):
        review = Review(title='Write Tests')
        self.assertEqual(str(review), 'Write Tests')
    
    
    def test_comment_str_is_title(self):
        comment = Comment(title='Write Tests')
        self.assertEqual(str(comment), 'Write Tests')
    
   
        
   