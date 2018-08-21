# from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.shortcuts import render
# from django.template import RequestContext
# from website.models import Order
# from django.contrib.auth.models import User


# @login_required
# def order_view(request):
#     items = Order.objects.filter(completed_date=blank)
#     context = {
#         'items': items
#     }
#     return render(request, "website/order.html", context)