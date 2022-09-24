from django.shortcuts import render, get_object_or_404
from products.models import Product

def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request=request, template_name='index.html', context=context)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context=context)
    