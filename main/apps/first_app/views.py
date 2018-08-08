from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

# Create your views here.
def index(request):
    response = "Hello Med, I am your first app request!"
    return HttpResponse(response)