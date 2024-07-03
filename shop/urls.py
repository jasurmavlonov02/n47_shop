from django.contrib import admin
from django.urls import path

from shop.views import product_list, product_detail, add_comment

urlpatterns = [
    path('', product_list, name='products'),
    path('category/<slug:category_slug>/products', product_list, name='products_of_category'),
    path('product/<slug:slug>', product_detail, name='product_detail'),

    # Comment urls
    path('product/<slug:product_slug>/detail/add-comment/',add_comment,name='add_comment' )

]
