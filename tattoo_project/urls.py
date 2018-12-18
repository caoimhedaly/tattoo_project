"""tattoo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from accounts.views import get_index
from accounts.views import register_artist, register_lover, read_profile
from blog import urls as blog_urls
from django.views.static import serve
from django.conf import settings
from ecommerce.views import product_detail, product_list, add_product, edit_product
from cart.views import add_to_cart, view_cart, remove_from_cart
from checkout.views import show_checkout, submit_payment
from reviews.views import make_review
from blog.views import make_comment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name='get_index'),
    path('', include(blog_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('accounts/profile/', read_profile, name='read_profile'),
    path('register/artist', register_artist, name="register_artist"),
    path('register/lover', register_lover, name="register_lover"),
    path('ecommerce/product_list', product_list, name = 'product_list'),
    path('ecommerce/<int:id>/product_detail', product_detail, name = 'product_detail'),
    path('cart/add', add_to_cart, name = 'add_to_cart'),
    path('cart/view', view_cart, name= 'view_cart'),
    path('cart/remove', remove_from_cart, name = 'remove_from_cart'),
    path('checkout/show_checkout/', show_checkout, name = 'show_checkout'),
    path('payment/', submit_payment, name = 'submit_payment'),
    path('products/<int:id>/edit', edit_product, name='edit_product'),
    path('products/add', add_product, name='add_product'),
    path('review/<int:id>/form', make_review, name= 'make_review'),
    path('comment/<int:id>/form', make_comment, name= 'make_comment'),
]