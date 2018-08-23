# Author:  Erin Agobert
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from website.models import Product


def ProductDetailView(request, pk):
    """ View manages the product detail from the product list view """
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product/detail.html', context)