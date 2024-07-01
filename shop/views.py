from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from shop.models import Product, Category


# Create your views here.

# @login_required
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)


    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'shop/detail.html', {'product': product})

# def comment_add(request):
#     pass
#
#
# def order_add():
#     pass
