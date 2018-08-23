# Author: Raf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.template import RequestContext
from website.models import Category
from website.forms import CategoryForm


@login_required
def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            new_category = category_form.save()
            new_category.save()
            return redirect('website:list_categories')


    return render(request, 'category/add_category.html', {'category_form': category_form})