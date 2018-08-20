from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

# from website.forms.forms import UserForm, ProductForm


def index(request):
    template_name = 'index.html'
    return render(request, template_name, {})