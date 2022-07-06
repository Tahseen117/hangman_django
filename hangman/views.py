from django.shortcuts import render, HttpResponse, redirect
from .models import Words
from .logic import *

def home(request):
    if request.method == "GET":
        return render(request, 'hangman/home.html')

def game(request):

    user_input= (request.GET.getlist("guess"))

    if len(user_input) > 0:
        if request.COOKIES.get('chance'):
            value = int(request.COOKIES.get('chance'))
        else:
            value=1

        context=verify(user_input,value)

        if 'won' in context.keys():
            return HttpResponse("<h1>You Won</h1>")
        
        if 'lost' in context.keys():
            response = HttpResponse("<h1>You LOST</h1>")
            response.delete_cookie('chance')
            return response

        if value < context['cookie']:
            response = render(request, 'hangman/game.html', context)
            response.set_cookie('chance',context['cookie'])
            return response
    else:
        context = logic()
        print("logic called")
    response = render(request, 'hangman/game.html', context)
    return response
