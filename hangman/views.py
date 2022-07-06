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
            response = redirect('won')
            response.delete_cookie('chance')
            return response
        
        if 'lost' in context.keys():
            image_number = context['lost']
            response = redirect('lose')
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

def lose(request):
    image_number= random.randint(1,3)
    response = render(request, 'hangman/lose.html', {'image_url': f"/hangman/lose-{image_number}.gif"})
    return response

def won(request):
    response = render(request, 'hangman/won.html')
    return response
