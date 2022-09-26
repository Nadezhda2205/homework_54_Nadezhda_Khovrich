from django.contrib import admin
from django.urls import path
from products.views import (
    products_view,
    product_view,
    product_add_view,
    product_del_view,
    product_edit_view,
    category_add_view,
    categories_view,
    category_del_view,
    category_edit_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_view, name='index'),
    path('products/', products_view),
    path('products/<int:pk>/', product_view, name='product_detail'),
    path('products/<int:pk>/del', product_del_view, name='product_del'),
    path('products/<int:pk>/edit', product_edit_view, name='product_edit'),

    path('categories/add/', category_add_view, name='category_add'),
    path('product/add/', product_add_view, name='product_add'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:pk>/del', category_del_view, name='category_del'),
    path('categories/<int:pk>/edit', category_edit_view, name='category_edit'),
]
