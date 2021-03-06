# Author:  Erin Agobert
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from website.models import Product
from website.forms import ProductForm

@login_required
def sell_product(request):
    """ View manages GETs the product form view and product detail view from POST request """
    if request.method == 'GET':

        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':

        form_data = request.POST

        p = Product(  # p is a built in DOM manipulator - makes the form show up in paragraph form
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            quantity = form_data['quantity'],
        )
        p.save()
        template_name = 'product/success.html'
        context = {'product': p}
        return render(request, template_name, context)