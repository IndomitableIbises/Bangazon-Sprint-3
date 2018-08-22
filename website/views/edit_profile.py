from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from website.forms import ProfileForm, UserForm
from django.contrib.auth.models import User


@login_required
def edit_profile(request):
    if request.method == "GET":
        u = User.objects.get(id=request.user.id)
        # Here's where we load the form
        user_form = UserForm(initial={'first_name': request.user.first_name,
        'last_name': request.user.last_name},) # create user field and set defaults from currently signed in user
        profile_form = ProfileForm(initial={'address': u.profile.address,
        'phone': 123},) # create profile filds and set defaults. NEED TO MAKE THESE 
        return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

    elif request.method == "POST":
        # Here's where we post updated info to the user
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)


        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save()
            return login_user(request)