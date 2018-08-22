from django import forms
from website.models import Payment

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('name', 'account_num', 'active', 'user',)