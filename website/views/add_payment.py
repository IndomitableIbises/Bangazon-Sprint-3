from django.shortcuts import render
from website.forms import PaymentForm
from website.models import Payment
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

@login_required
def add_payment(request):
    if request.method == 'GET':
        payment_form = PaymentForm()
        template_name = 'payment/create.html'
        return render(request, template_name, {'payment_form': payment_form})

    elif request.method == 'POST':
        form_data = request.POST
        payment = PaymentForm(form_data)
        if payment.is_valid():
            payment.save()
            
        template_name = 'payment/success.html'
        return render(request, template_name, {})