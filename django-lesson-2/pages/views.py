from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function-based vs Class-based
# takes in an HTTP request and returns an HTTP response

# homepage
def home(request):
    # grab some data from the database
    # some refinement of data here
    context = {
        "page_name": "Home Page",
        "title": "Home"}
    return render(request, 'pages/home.html', context)

# about us
def about(request):
    # return HttpResponse("<h1>About us Page</h1>")
    context = {
        "page_name": "About Us Page",
        "title": "About"
        }
    return render(request, 'pages/about.html')

# contact us
def contact(request):
    context = {
        "page_name": "Contact Us Page",
        "title": "Contact"
        }
    return render(request, 'pages/contact.html')

# services
def services(request):
    context = {
        "page_name": "Our Services Page",
        "title": "Services"
        }
    return render(request, 'pages/services.html')