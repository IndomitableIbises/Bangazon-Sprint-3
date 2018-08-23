from django.shortcuts import render
from website.models import Product
from django.contrib.auth.models import User


def ProductDetailView(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product/detail.html', context)