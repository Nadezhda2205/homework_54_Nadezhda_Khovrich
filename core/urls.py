from django.contrib import admin
from django.urls import path
from products.views import products_view, product_view, category_add_view, product_add_view, categories_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_view, name='index'),
    path('products/', products_view),
    path('products/<int:pk>/', product_view, name='product_detail'),
    path('categories/add/', category_add_view, name='category_add'),
    path('product/add/', product_add_view, name='product_add'),
    path('categories/', categories_view, name='categories'),
]
