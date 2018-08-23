from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from website.models import Order
from django.contrib.auth.models import User



@login_required
def order_detail(request, pk):
    """Displays template for deleting a computer
    Sean Irwin"""
    order = get_object_or_404(Order, pk=pk)
    total = 0
    items = order.shopping_cart.all()
    for item in items:
            total += item.price
    

    context = {
        'order': order,
        'total': total,
    }
    
    return render(request, "order_detail.html", context)

        
        