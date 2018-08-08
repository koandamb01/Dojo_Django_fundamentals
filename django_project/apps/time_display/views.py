from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def index(request):
    content = {
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime())
    }
    return render(request, 'time_display/index.html', content)