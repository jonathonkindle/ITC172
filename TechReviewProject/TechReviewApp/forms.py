from django import forms
from .models import ProductType, Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model=ProductType
        fields='__all__'