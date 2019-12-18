from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product 
from .forms import ProductCreateForm
# Create your views here.

def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        "form": form 
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, id):
    # two ways to handle exceptions
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

