from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product, Category
from django.core.handlers.wsgi import WSGIRequest

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


def category_add_view(request: WSGIRequest):
    if request.method == 'POST':
        category_data = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
        }
        Category.objects.create(**category_data)
        return redirect('index')
    return render(request=request, template_name='category_add.html')