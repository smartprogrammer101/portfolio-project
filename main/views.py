from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, "home.html")

def about(req):
    return render(req, "about.html")

def contact(req):
    return render(req, "contact.html")

def services(req):
    return render(req, "services.html")