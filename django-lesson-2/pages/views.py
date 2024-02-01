from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function-based vs Class-based
# takes in an HTTP request and returns an HTTP response

# homepage
def home(request):
    return HttpResponse("<h1>Home Page</h1>")

# about us
def about(request):
    return HttpResponse("<h1>About us Page</h1>")

# contact us
def contact(request):
    return HttpResponse("<h1>Contact us Page</h1>")

# services
def services(request):
    return HttpResponse("<h1>Services Page</h1>")