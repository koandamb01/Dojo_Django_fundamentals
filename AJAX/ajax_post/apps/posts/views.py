from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from .models import *

def index(request):
    content = { 'posts': Post.objects.all() }
    return render(request, 'posts/index.html', content)

def add_post(request):
    if request.method != 'POST':
        return redirect('/')
    post = Post.objects.create(post=request.POST['post'])
    content = { 'posts': Post.objects.all() }
    return render(request, 'posts/posts.html', content)