from django.shortcuts import render
from .models import Product 

# Create your views here.


def product_list(request):
   products = Product.objects.all()
   return render(request, 'ecommerce/product_list.html', {'products': products})


def product_detail(request, id):
   
      product = get_object_or_404(Product, pk=id)
      return render(request, 'ecommerce/product_detail.html', {'product':product})
