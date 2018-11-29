from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# Create your models here.
class Artist(models.Model):

    image= models.ImageField(upload_to='avatars',default = 'avatars/anonymous.png', null=True, blank=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="artist")
    salon= models.CharField(max_length=100, null=True, blank=True)
    # experience=models.DecimalField(max_digits=6, decimal_places=2)
    Bio = models.TextField(max_length=1000, null=True, blank=True)
    
    # if user is deleted, delete the profile
    # related_name creates the link to the user
    
    def __str__(self):
        return '{0}'.format(self.user.username)
        
        
class Lover(models.Model):
    image= models.ImageField(upload_to='avatars',default = 'avatars/anonymous.png', null=True, blank=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="lover")
    # if user is deleted, delete the profile
    # related_name creates the link to the user
    
    def __str__(self):
        return '{0}'.format(self.user.username)
        
    
    