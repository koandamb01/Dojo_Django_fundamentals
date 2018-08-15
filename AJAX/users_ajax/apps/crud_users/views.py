from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from time import gmtime, strftime

def index(request):
    # get all users from the database
    users = User.objects.values().all()
    return render(request, 'crud_users/users.html', {'users': users})

def new(request):
    return render(request, 'crud_users/new.html')

def edit(request, id):
    # get the user info from the database
    u = User.objects.get(id = id)
    user = {
        'id': id,
        'first_name': u.first_name,
        'last_name': u.last_name,
        'email': u.email,
        'created_at': u.created_at
    }
    return render(request, 'crud_users/edit.html', user)

def show(request, id):
    # get the user info from the database
    u = User.objects.get(id = id)
    user = {
        'id': id,
        'first_name': u.first_name,
        'last_name': u.last_name,
        'email': u.email,
        'created_at': u.created_at
    }
    return render(request, 'crud_users/show.html', user)


def destroy(request, id):
    # get the user info from the database
    u = User.objects.get(id = id)
    u.delete()
    messages.success(request, "A user was delete from database")
    return redirect('/users')

def update(request):
    errors = User.objects.basic_validator(request.POST)

    # check if any error exist
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)

        # redirect to the form to display the message
        return redirect('/users/'+request.POST['id']+'/edit')
    else:
        # No erros so send the data to the database

        #first the the user info that needed to be update
        user = User.objects.get(id = request.POST['id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        # Redirect witht the new user id
        messages.success(request, 'This user info was was updated!')
        return redirect('/users/'+str(user.id))

def create(request):
    user = User.objects
    user.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])

    # Redirect witht the new user id
    return render(request, 'crud_users/all.html', {'users': User.objects.values().all() } )