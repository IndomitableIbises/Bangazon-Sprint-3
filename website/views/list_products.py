from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.models import Product


def list_products(request):
    search_terms = request.GET.get('search_terms', '')
    all_products = Product.objects.all()
    if search_terms:
        search_results = [item for item in all_products if search_terms in item.title]
        # filter all_products and render the filtered stuff
        return render(request,'product/list.html' , {'products': search_results})
    else:
        return render(request,'product/list.html' , {'products': all_products})
