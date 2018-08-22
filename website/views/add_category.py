# Author: Raf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms import CategoryForm

@login_required
def add_category(request):
        if request.method == 'GET':
            category_form = CategoryForm()
            return render(request, 'add_category.html', {'category_form': category_form})

        elif request.method == 'POST':
            form_data = request.POST

        c = Category(
            cat_name = form_data['cat_name'],

        )
        c.save()
        return render(request, 'category/success.html', {})