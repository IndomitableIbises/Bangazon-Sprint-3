from django.shortcuts import render
from website.forms import PaymentForm


def sell_product(request):
    if request.method == 'GET':
        product_form = PaymentForm()
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