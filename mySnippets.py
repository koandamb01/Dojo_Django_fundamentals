# Token need for all django forms
# Prevents cross-site request forgery (place it in a form on the HTML/template side of your project)
{% csrf_token %}

# TO add SESSION to your DJango project:
# In our terminal, head to the directory where manage.py resides and run the following commands:
# Need to be in same directory as manage.py file
python manage.py makemigrations
python manage.py migrate

##### time and date ############
from time import gmtime, strftime
today = strftime("%Y-%m-%d %H:%M %p", gmtime())

################# urls.py ##############
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index)
]

############### views.py ###############
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
  def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

{% load static %}
# The line above tells Django to be ready to listen for static files -->
<link rel="stylesheet" href="{% static 'ourApp/css/main.css' %}">
# Put the static files in the static folder inside your app.  


############ EXAMPLE OF URLS REDIRECTION ################
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show), # for number
    url(r'^(?P<number>\d+)/edit$', views.edit), # for number/name
    url(r'^(?P<number>\d+)/delete$', views.destroy)
]

# In case the BIG URL need to redirect different route in to apps
# users app
# /register - display 'placeholder for users to create a new user record'
# /login - display 'placeholder for users to login' 
# /users/new - have the same method that handles /register also handle the url request of /users/new
# /users - display 'placeholder to later display all the list of users'
from apps.users import views as user_views
urlpatterns = [
    url(r'^blogs/', include('apps.blogs.urls')),
    url(r'^surveys/', include('apps.surveys.urls')),
    url(r'^users/', include('apps.users.urls')),
    url(r'^register/', user_views.register),
    url(r'^login/', user_views.login),
    url(r'^admin/', admin.site.urls)
]



############### BCRYPT PASSWORD HASH FOR DJANGO ##################
import bcrypt
hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
def validate_login(request):
    user = User.objects.get(email=request.POST['email'])
    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
        print("password match")
    else:
        print("failed password") 