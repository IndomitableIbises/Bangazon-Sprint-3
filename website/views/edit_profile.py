from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def edit_profile(request):
    if request.method == "GET":
        user_data = request.user # this gets the currenty logged in user id. 
        return render(request, 'edit_profile.html', {'user_data': user_data})
        return "get method"

    elif request.method == "POST":
        return 'post method'