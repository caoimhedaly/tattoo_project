from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
    # model form, properties are already defined in models
    class Meta:
        model= Product
        fields='__all__'
# take form details from class order model in models.py