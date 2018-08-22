from django.shortcuts import render

# from website.forms.forms import UserForm, ProductForm


def profile(request):
    template_name = 'profile.html'
    return render(request, template_name, {})