from django.shortcuts import render
from products.models import Product

def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request=request, template_name='index.html', context=context)
