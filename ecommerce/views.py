from django.shortcuts import render, redirect, get_object_or_404
from .models import Product 
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.


def product_list(request):
   products = Product.objects.all()
   return render(request, 'ecommerce/product_list.html', {'products': products})


def product_detail(request, id):
   
      product = get_object_or_404(Product, pk=id)
      return render(request, 'ecommerce/product_detail.html', {'product':product})
      
      
@login_required     
def add_product(request):
    
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        product=form.save(commit=False)
        # dont save to database
        product.author = request.user
        # author= logged in user
        product.save()
        # finally save to database
        return redirect(product_detail, product.id)
    else:    
        form = ProductForm()
        return render(request, "ecommerce/form.html", {'form': form })
        
      

@login_required     
def edit_product(request, id):
    
    product = get_object_or_404(Product, pk=id)
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        form.save()
        return redirect('/ecommerce/product_list')
    else:        
        form=ProductForm(instance=product)
        return render(request, "ecommerce/form.html", {'form': form })
        