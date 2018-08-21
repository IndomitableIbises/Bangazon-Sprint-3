from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.models import Product


def list_products(request):
    all_products = Product.objects.all()
    return render(request,'product/list.html' , {'products': all_products})
