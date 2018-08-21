# Author: Raf
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models import Category
from django.contrib.auth.decorators import login_required

@login_required
def list_categories(request):
    all_categories = Category.objects.all()
    return render(request, 'category.html', {'all_categories': all_categories})