from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Home Page")
def about(request):
    return HttpResponse("About Page")
def welcome(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
