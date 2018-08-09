# Token need for all django forms
# Prevents cross-site request forgery (place it in a form on the HTML/template side of your project)
{% csrf_token %}

# TO add SESSION to your DJango project:
# In our terminal, head to the directory where manage.py resides and run the following commands:
# Need to be in same directory as manage.py file
  > python manage.py makemigrations
  > python manage.py migrate



################# urls.py ##############
fromcopy django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index)   # This line has changed! Notice that urlpatterns is a list, the comma is in
]    

############### views.py ###############
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
  def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)