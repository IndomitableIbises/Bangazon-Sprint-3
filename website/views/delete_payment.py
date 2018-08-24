from django.http import HttpResponseRedirect
from website.models import Payment
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User

@login_required
def delete_payment(request, pk):
    """Displays template for deleting a payment
    Sean Irwin"""
    payment = get_object_or_404(Payment, pk=pk)
    payment.active = False
    payment.save()
    return HttpResponseRedirect('/')
