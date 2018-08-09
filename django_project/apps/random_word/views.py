from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    content = {
        'word': get_random_string(length=14)
    }

    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    return render(request, 'random_word/index.html', content)


def reset(request):
    request.session.clear()
    return redirect('/random_word')


