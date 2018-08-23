from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from website.models import Product


def ProductDetailView(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product/detail.html', context)