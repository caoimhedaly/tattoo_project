from django.db import models
from ecommerce.models import Product
from blog.models import Post
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='reviews', null=False, on_delete=models.PROTECT) 
    product= models.ForeignKey(Product, related_name= 'reviews', null=False, on_delete=models.PROTECT)
  
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='comments', null=False, on_delete=models.PROTECT) 
    post= models.ForeignKey(Post, related_name= 'comments', null=False, on_delete=models.PROTECT)
  
    def __str__(self):
        return self.title

