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


def product_add_view(request: WSGIRequest):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        category: Category = Category.objects.get(name=category_name)
        product_data = {
            'name': request.POST.get('name'),
            'price': request.POST.get('price'),
            'img': request.POST.get('img'),
            'description': request.POST.get('description'),
            'category': category,
        } 
        product: Product = Product.objects.create(**product_data)
        return redirect('product_detail', pk=product.pk)

    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request=request, template_name='product_add.html', context=context)
