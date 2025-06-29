from django.shortcuts import get_object_or_404 , render
from django.shortcuts import redirect
from .forms import ProductForm
# Create your views here.

from .models import Product
def index(request):
    product_list = Product.objects.all()
    return render(request, "stock/index.html", {"product_list": product_list})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "stock/detail.html", {"product": product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'stock/add_product.html', {'form': form})


