from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login


def homepage(request):
    return render(request=request,
                  template_name="tutorials/home.html",
                  context={"tutorials": Tutorial.objects.all})

def register(request):
    form = UserCreationForm
    return render(request, 
                  "tutorials/register.html",
                  {"form":form})

