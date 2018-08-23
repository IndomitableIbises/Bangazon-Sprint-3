from django.shortcuts import render
from website.models import Product
#from website.forms import ProductForm


def ProductDetailView(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(pk=product_id)
        template_name = 'product/detail.html'
        context = {'product': product}
        return render(request, template_name, context)