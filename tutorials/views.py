from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm # importing overwritten user creation form





def single_slug(request, single_slug):
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        # we are looking for tutorial series
        # we are going to match series with category by using filter
        # we are matching series foreign key - category with a category slug
        matching_series = TutorialSeries.objects.filter(category__slug=single_slug)
        series_urls = {}
        # we are sending user to part one of tutorial of matching series
        for m in matching_series.all():
            # filtering foreign key in tutorials matching to TutorialSeries series variable
            # part_one returns the earliest tutorial of particular series
            part_one = Tutorial.objects.filter(series__series=m.series).earliest("published")
            # key is the object(series), value is url(slug)
            series_urls[m] = part_one.slug
        # in the end we return a render
        return render(request=request,
                      template_name="tutorials/category.html",
                      context={"part_ones": series_urls})

    turorials = [t.slug for t in Tutorial.objects.all()]
    if single_slug in turorials:
        return HttpResponse(f"{single_slug} is a tutorial!!!")

    return HttpResponse(f"{single_slug} doesn't correspond to anything")


def homepage(request):
    return render(request=request,
                  template_name="tutorials/categories.html",
                  context={"categories": TutorialCategory.objects.all})


def register(request):
    '''

    '''
    if request.method == "POST":
        form = NewUserForm(request.POST)
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

    form = NewUserForm
    return render(request = request,
                  template_name = "tutorials/register.html",
                  context={"form":form})

def logout_request(request):
    '''

    '''
    logout(request)
    messages.info(request, "Logged out succesfully!")
    return redirect("tutorials:homepage")

def login_request(request):
    '''

    '''
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # grabbing username
            password = form.cleaned_data.get('password') # grabbing password
            user = authenticate(username=username, password=password)  # authenticating username and password
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("tutorials:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 
                  "tutorials/login.html",
                  {"form":form})



