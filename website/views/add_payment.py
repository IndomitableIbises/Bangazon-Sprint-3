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

        p = Payment(
            user = request.user,
            name = form_data['name'],
            account_num = form_data['account_num'],
            active = form_data['active'],
        )
        p.save()
        template_name = 'payment/success.html'
        return render(request, template_name, {})