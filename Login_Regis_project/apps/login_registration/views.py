from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *
import bcrypt

def index(request):
    return render(request, 'login_registration/index.html')


def welcome(request, id):
    user = User.objects.values().get(id = id)
    return render(request, 'login_registration/welcome.html', user)


def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    # if it is not a post request return to the home page
    if request.method != "POST":
        return redirect('/')

    errors = User.objects.basic_validator(request.POST)
    # check if any errors exist
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, key)

            # record form data to sessions
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']
            request.session['email'] = request.POST['email']
            request.session['birthday'] = request.POST['birthday']
            request.session['city'] = request.POST['city']
            request.session['state'] = request.POST['state']
            request.session['zipcode'] = request.POST['zipcode']
        return redirect('/')
    else:
        # check email already exist in the database
        # user = Uber.objects.filter(email = request.POST['email'])

        # Hash the user password first
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    
        user = User.objects # create an object of the user table
        user.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            birthday = request.POST['birthday'],
            city = request.POST['city'],
            state = request.POST['state'],
            zipcode = request.POST['state'],
            password = hash_pw
        )
    
    
    request.session.clear()
    request.session['user_id'] = user.last().id
    return redirect('/welcome/'+str(user.last().id))

