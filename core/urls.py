from django.contrib import admin
from django.urls import path
from products.views import products_view, product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_view, name='index'),
    path('products/', products_view),
    path('products/<int:pk>/', product_view, name='product_detail')
]
