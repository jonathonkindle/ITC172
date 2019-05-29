from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product, Review
from .forms import ProductForm

# Create your views here.
def index(request):
    return render(request, 'TechReviewApp/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'TechReviewApp/types.html', {'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'TechReviewApp/products.html', {'products_list' : products_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'TechReviewApp/productdetails.html', context=context)

def newproduct(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
    else:
        form=ProductForm()
    return render(request, 'TechReviewApp/newproduct.html', {'form': form})