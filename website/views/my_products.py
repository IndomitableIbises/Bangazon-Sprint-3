from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.models import Product

@login_required
def my_products(request):
    all_products = Product.objects.filter(seller = request.user.id)
    productlist = []
    if len(all_products):
        for product in all_products:
            sales = len(product.order_set.all())
            sale_info = "Product: "+ product.title
            quantity = "Quantity Sold: "+ str(sales)
            productlist.append(sale_info)
            productlist.append(quantity)

    context = {
        'productlist': productlist,
    }
    
    return render(request, "my_products.html", context)
    