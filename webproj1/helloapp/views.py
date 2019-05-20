from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.shortcuts import render

@csrf_exempt
def register(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "register.html", {'form': form}, status = 200)
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['passwordconf']:
                return HttpResponse("Invalid registration request.", status = 400)
            else:
                User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], 
                password = form.cleaned_data['password'], first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])

                return HttpResponse("Registered.")
        else:
            return HttpResponse("Invalid registration request.", status = 400)
    else:
        return HttpResponse("Method not allowed", status = 405)

