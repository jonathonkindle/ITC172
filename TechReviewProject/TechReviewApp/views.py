from django.shortcuts import render
from .models import ProductType, Product, Review

# Create your views here.
def index(request):
    return render(request, 'TechReviewApp/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'TechReviewApp/types.html', {'type_list' : type_list})