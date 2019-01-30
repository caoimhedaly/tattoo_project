from django.test import TestCase
from .forms import ReviewForm, CommentForm

# Create your tests here.

class TestReviewForm(TestCase):
    
    def test_can_create_review_with_just_a_title(self):
        form = ReviewForm({ 'title':'create product'})
        self.assertFalse(form.is_valid())
        
    def test_can_create_review_with_just_content(self):
        form = ReviewForm({ 'content':'create product'})
        self.assertFalse(form.is_valid())
        
        
    def test_correct_message_for_missing_title(self):
        form = ReviewForm({ 'title':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        
            
    def test_correct_message_for_missing_content(self):
        form = ReviewForm({ 'content':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
        

class TestCommentForm(TestCase):
    
    def test_can_create_comment_with_just_a_title(self):
        form = CommentForm({ 'title':'create comment'})
        self.assertFalse(form.is_valid())
        
    def test_can_create_comment_with_just_content(self):
        form = CommentForm({ 'content':'create comment'})
        self.assertFalse(form.is_valid())
        
    def test_correct_message_for_missing_content(self):
        form = CommentForm({ 'content':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
        
    def test_correct_message_for_missing_title(self):
        form = CommentForm({ 'title':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])
        