from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'amadon/index.html')

def add(request):
    total = float(request.POST['price']) * float(request.POST['quantity'])
    request.session['total'] = total
    request.session['quantity'] = request.POST['quantity']
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')