from django.shortcuts import render
from website.models import Product
#from website.forms import ProductForm


def ProductDetailView(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product/detail.html', context)