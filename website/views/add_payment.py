from django.shortcuts import render, redirect
from website.forms import PaymentForm
from website.models import Payment
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required


@login_required
def add_payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            new_category = payment_form.save()
            new_category.save()
            return redirect('website:payment_success')


    return render(request, 'payment/create.html', {'payment_form': payment_form})

    # if request.method == 'GET':
    #     payment_form = PaymentForm()
    #     template_name = 'payment/create.html'
    #     return render(request, template_name, {'payment_form': payment_form})

    # elif request.method == 'POST':
    #     form_data = request.POST
    #     payment = PaymentForm(form_data)
    #     if payment.is_valid():
    #         payment.save()

    #     template_name = 'payment/success.html'
    #     return render(request, template_name, {})
