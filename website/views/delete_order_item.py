from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from website.models import Order, Product
from django.contrib.auth.models import User


def delete_order_item(request, item_id):
    
    """Displays template for deleting a computer
    Sean Irwin"""
    user_order = Order.objects.filter(user=request.user.id).filter(payment__isnull=True)
    item = get_object_or_404(Product, pk=item_id)
    user_order[0].shopping_cart.remove(item)
    return HttpResponseRedirect('/order')