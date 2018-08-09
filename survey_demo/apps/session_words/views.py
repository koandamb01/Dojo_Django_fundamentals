from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'session_words/index.html')


def clear(request):
  request.session.clear()
  return redirect('/session_words')

def add(request):
  print("FORM:", request.POST)

  if 'words' in request.session:
    temp_list = request.session['words']

    if 'big' in request.POST:
      temp_list.append({
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': request.POST['big'],
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime())
      })
    else:
      temp_list.append({
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': 'off',
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime())
      })
    request.session['words'] = temp_list
  
  else:
    if 'big' in request.POST:
      request.session['words'] = [{
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': request.POST['big'],
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime())
      }]
    else:
      request.session['words'] = [{
        'word': request.POST['word'],
        'color': request.POST['color'],
        'big': 'off',
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime())
      }]

  
  print("session:", request.session['words'])
  return redirect('/session_words')