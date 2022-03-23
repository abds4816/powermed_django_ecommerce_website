from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def index(request):
    categories = Category.objects.all().order_by('category_name')
    products = Product.objects.all().order_by('-publish_date')
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def thanks(request):
    return render(request, 'pages/thanks.html')