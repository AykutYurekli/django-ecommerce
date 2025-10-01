from django.shortcuts import render,get_object_or_404
from .models import Product,Category

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request, "products/product_list.html", {"products": products, "category": category})

def product_category(request,category_id):
    selected_category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category= selected_category)
    categories  = Category.objects.all()
    return render(request, "products/product_list.html", {"products": products, "categories": categories , "selected_category": selected_category})

def product_category_shoe(request):
    products = Product.objects.filter(category__name='Shoe')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Shoe"})

def product_category_hat(request):
    products = Product.objects.filter(category__name='Hat')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Hat"})

def product_category_tshirt(request):
    products = Product.objects.filter(category__name='T-Shirt')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "T-Shirt"})

def product_category_accessories(request):
    products = Product.objects.filter(category__name='Accessories')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Accessorie"})

def product_category_pant(request):
    products = Product.objects.filter(category__name='Pant')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Pant"})

def product_category_beret(request):
    products = Product.objects.filter(category__name='Beret')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Beret"})

def product_category_sweatshirt(request):
    products = Product.objects.filter(category__name='Sweatshirt')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Sweatshirt"})

def product_category_shirt(request):
    products = Product.objects.filter(category__name='Shirt')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Shirt"})

def product_category_short(request):
    products = Product.objects.filter(category__name='Short')
    color = request.GET.get('color')
    if color:
        products = products.filter(color=color)
    return render(request, "products/product_list.html", {"products": products, "selected_category": "Short"})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    return render(request, "products/product_detail.html", {"product": product , 'similar_products': similar_products})

