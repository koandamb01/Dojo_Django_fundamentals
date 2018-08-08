from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello Mohamed')
    return render(request, 'firstapp/index.html')
