from django.shortcuts import render

# from website.forms.forms import UserForm, ProductForm


def index(request):
    template_name = 'index.html'
    return render(request, template_name, {})