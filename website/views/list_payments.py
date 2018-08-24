from django.shortcuts import render, redirect
from website.models import Payment
from django.contrib.auth.decorators import login_required


@login_required
def list_payments(request):

    if request.user is not None:
        payments = Payment.objects.filter(user=request.user)
        context = {"payments": payments}
        return render(request, "payment/list.html", context)
    else: 
        return redirect("/login")

        payment_form = PaymentForm()
        template_name = 'payment/create.html'
        return render(request, template_name, {'payment_form': payment_form})

