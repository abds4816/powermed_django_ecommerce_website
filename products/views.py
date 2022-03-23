from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

# Create your views here.

def categories(request):
    categories = Category.objects.all()

    paginator = Paginator(categories, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': page_obj
    }
    return render(request, 'products/categories.html', context)

def category(request, cat_id):
    products = Product.objects.all().filter(category=cat_id)
    category = Category.objects.get(id=cat_id)
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'products/products.html', context)

def products(request):
    name = None
    products = Product.objects.all()
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            products = products.filter(name__icontains=name)

    paginator = Paginator(products, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'name': name,
    }
    return render(request, 'products/products.html', context)

def product(request, pro_id):
    pro = get_object_or_404(Product, id=pro_id)
    other_products = Product.objects.filter(category=pro.category)
    related_products = []
    for product in other_products:
        if product.id != pro.id:
            related_products.append(product)
    context = {
        'related_products': related_products,
        'pro': pro
    }
    return render(request, 'products/product.html', context)