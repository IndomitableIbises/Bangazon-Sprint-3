
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models import Order, Payment
from django.contrib.auth.models import User


@login_required
def order_history(request):

    userorder = Order.objects.filter(user=request.user.id).filter(payment__isnull=False)
    userorderid = "error"
    userpayment = "None"
    userorderid = []
    if(len(userorder)):
        for order in userorder:
            items = order.shopping_cart.all()
            userorderid.append(order)
            userpayment = Payment.objects.filter(user=request.user.id)
        
    else:
        items = ["No Active Orders"]
        userorderid = "error"
    context = {
        'items': items,
        'userorderid': userorderid
    }

    return render(request, "order_history.html", context)
