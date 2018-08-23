from django.http import HttpResponseRedirect
from website.models import Payment
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def delete_payment(request, pk):

        payment = Payment.objects.get(pk=pk)
        if request.user == payment.user:
                payment.delete()
                return HttpResponseRedirect("/payment")
        else:
                return HttpResponseForbidden()