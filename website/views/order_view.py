
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models import Order, Payment
from django.contrib.auth.models import User


@login_required
def order_view(request):

    userorder = Order.objects.filter(user=request.user.id).filter(payment__isnull=True)
    total = 0
    userorderid = "error"
    userpayment = "None"
    if(len(userorder)):
        items = userorder[0].shopping_cart.all()
        userorderid = userorder[0]
        userpayment = Payment.objects.filter(user=request.user.id)
        
        for item in items:
            total += item.price
    else:
        items = ["No Active Orders"]

    context = {
        'items': items,
        'total': total,
        'userorderid': userorderid,
        'userpayment': userpayment
    }
    
    return render(request, "order.html", context)
