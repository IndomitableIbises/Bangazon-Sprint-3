from django.shortcuts import render
from website.models import Profile
from django.contrib.auth.models import User

# from website.forms.forms import UserForm, ProductForm


def profile(request):
    user = request.user
    u = User.objects.get(id=request.user.id)
    profile = u.profile
    return render(request, 'profile.html', {'user': user, 'profile': profile})