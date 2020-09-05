from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import App, RegistrationData
from .forms import RegistrationForm

# Create your views here.

def Home(request):

    context = {
        "name": "Bob",
        "list": ["Python", "Java", "c++"],
        "number": 0
    }
    return render(request, 'home.html', context)

def AppView(request):
    obj = App.objects.get(id=1)

    context = {
        "data": obj
    }
    return render(request, 'app.html', context)

def AppDateView(request, year):
    article_list = App.objects.filter(pub_date__year = year)
    
    context = {
        'year':year, 
        'article_list': article_list,
    }
    return render(request, 'appdate.html', context)

def Contact(request):
    return HttpResponse("<h1>Contact Page</h1>")

def register(request):

    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)

def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        register = RegistrationData(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    email=form.cleaned_data['email'],
                                    phone=form.cleaned_data['phone'])
        
        register.save() 

    return redirect('Home')
