from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import CommentModelForm
from shop.models import Product, Category


@login_required(login_url='http://127.0.0.1:8000/admin/login/?next=/admin/')
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
    category = product.category
    related_products = Product.objects.filter(category=category).exclude(slug=slug)
    comments = product.comments.filter(is_possible=True)
    context = {
        'product': product,
        'comments': comments
    }
    return render(request, 'shop/detail.html', context)


def add_comment(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.product = product
            comment.save()
            print('Save Done ! ')
            return redirect('product_detail', product_slug)
    else:
        form = CommentModelForm(request.GET)
        print('Get method running')

    return render(request, 'shop/detail.html', {'form': form, 'product': product})


# def comment_add(request):
#     pass
#
#
# def order_add():
#     pass

def add_order(request):
    pass
