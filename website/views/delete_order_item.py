from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models import Order
from django.contrib.auth.models import User


def delete_order_item(request, pk):
    
    """Displays template for deleting a computer
    Sean Irwin"""
    user_order = Order.objects.filter(user=request.user.id).filter(payment__isnull=True)
    item = user_order.shopping_cart.objects.filter(product_id=pk)
    item.delete()
    return redirect('order')