from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    #fetch all the data from the databse
    courses = Course.objects.all()

    # combine two tables data togeter that has OneToOne relationship
    data = []
    d = Description.objects
    for course in courses:
        print(course.id)
        data.append({
            'id': course.id,
            'name': course.name,
            'description': d.filter(course = course).first().desc,
            'created_at': course.created_at
        })
    return render(request, 'courses/index.html', {'courses': data})

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    # check if there is any errors
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            request.session['name'] = request.POST['name']
            request.session['desc'] = request.POST['desc']
    else:
        #no error proceed to putting the data in the database
        course = Course.objects
        desc = Description.objects

        course.create(name = request.POST['name'])
        course = Course.objects.last()
        desc.create(desc = request.POST['desc'], course = course)

        messages.success(request, 'A new course was added!')
    # redirect to the home page
    return redirect('/')


def destroy(request, id):
    #fetch all the data from the databse
    c = Course.objects.get(id = id)
    d = Description.objects
    course = {
        'id': c.id,
        'name': c.name,
        'description': d.filter(course = c).first().desc,
        'created_at': c.created_at
    }
    return render(request, 'courses/warning.html', course)


def remove(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, "A course was remove from the list")
    return redirect('/')