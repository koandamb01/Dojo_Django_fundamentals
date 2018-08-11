# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!! 
# (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = BlogManager()
    # *************************



######## Now in our views.py file, we can use Blog.objects.basic_validator(postData):
# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
   
from .models import Blog
def update(request, id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Blog.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
        if len(errors):
            # if the errors object contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/blog/edit/'+id)
        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            blog = Blog.objects.get(id = id)
            blog.name = request.POST['name']
            blog.desc = request.POST['desc']
            blog.save()
            messages.success(request, "Blog successfully updated")
            # redirect to a success route
            return redirect('/blogs')