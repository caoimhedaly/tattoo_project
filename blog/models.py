from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User


from django.conf import settings

# Create your models here.

class Post(models.Model):
    """
    A single Blog post
    
    
    """
    
    class Meta:
        permissions =( 
            ("can_publish", "can publish a blog post"),
        )
        
    title = models.CharField(max_length=200)
    
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.ForeignKey(User, related_name='posts', null=False, default=1, on_delete=models.SET_DEFAULT) 
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    
    
    # counts views
    image= models.ImageField(upload_to='images', null=True, blank=False)
    tags = models.CharField(max_length=255, null=True, blank=True)
    
    
    @property
    def taglist(self):
        if self.tags:
            tag_values = self.tags.split(',')
            return tag_values
        else:
            return []
    
    
    def __str__(self):
        return self.title
        
        
    

   

    
    


