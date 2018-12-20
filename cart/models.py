# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Product(models.Model):
#     name = models.CharField(max_length=254, default='')
#     user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="product")
#     sku = models.CharField(max_length=50, default='')
#     description = models.TextField()
#     image = models.ImageField(upload_to='images')
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     stock = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.name
