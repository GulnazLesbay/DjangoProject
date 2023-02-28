from django.shortcuts import render, get_object_or_404

from itproger.main.models import Product, Category


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

#
# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, in_stock=True)
#     return render(request, 'main/products/single.html', {'product': product})
#
#
# def category_list(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.products.filter(category=category)
#     return render(request, 'main/products/category.html', {'category': category, 'products': products})
