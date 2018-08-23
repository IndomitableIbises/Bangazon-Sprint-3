from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models import Order, Payment
from django.contrib.auth.models import User
import datetime

@login_required
def complete_order(request):
    current_order = Order.objects.filter(user=request.user.id).filter(payment__isnull=True)
    current_order_object = current_order[0]
    current_order_object.payment_id = request.POST['payment']
    current_order_object.completed_date = datetime.date.today()
    current_order_object.save()
    return HttpResponseRedirect("/thankyou")