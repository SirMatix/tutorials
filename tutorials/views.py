from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages




def homepage(request):
    return render(request=request,
                  template_name="tutorials/home.html",
                  context={"tutorials": Tutorial.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():    # fields filled in the way the should be filled out
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}") # message for new account created
            login(request, user)
            messages.info(request, f"You are now logged in as {username}") # message for new account created
            return redirect("tutorials:homepage")
        else:     # if form is not valid
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request =request, 
                         template_name="tutorials/register.html",
                         context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "tutorials/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out succesfully!")
    return redirect("tutorials:homepage")

def login_request(request):
    form = AuthenticationForm()
    return render(request, 
                  "main/login.html",
                  {"form":form})
