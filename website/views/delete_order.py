from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models import Order
from django.contrib.auth.models import User




def delete_order(request, pk):
    """Displays template for deleting a computer
    Sean Irwin"""
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('list_products')