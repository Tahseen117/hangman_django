import random
from django.shortcuts import render,get_object_or_404
from .models import Words

key=random.randint(1,2)
chosen_word = get_object_or_404(Words, pk=key)
print(f"chosen by main code {str(chosen_word)}")
display = []
for position in range(len(str(chosen_word))):
    display += "_"

def logic():
    global display
    key=random.randint(1,2)
    chosen_word = get_object_or_404(Words, pk=key)
    print(f"chosen by main logic code {str(chosen_word)}")
    display = []
    for position in range(len(str(chosen_word))):
        display += "_"   
    
    context = {'word': chosen_word, 'blank': display, 'art': '/hangman/art-1.png'}
    return context

def verify(user_input,cookie):
    global display
    found=0
    if "_" in display:
        for i in range(len(str(chosen_word))):
            if str(chosen_word)[i] == user_input[0]:
                display[i] = str(chosen_word)[i]
                found=1
        if found==1:
            if "_" not in display:
                context = {'word': chosen_word, 'blank': display, 'art': f'/hangman/art-{cookie}.png', 'cookie': cookie, 'won':'won' }
            else:
                context = {'word': chosen_word, 'blank': display, 'art': f'/hangman/art-{cookie}.png', 'cookie': cookie }
        else:
            cookie +=1
            if cookie == 7:
                context = {'word': chosen_word, 'blank': display, 'art': f'/hangman/art-{cookie}.png', 'cookie': cookie, 'lost':'lost' }
            else:
                context = {'word': chosen_word, 'blank': display, 'art': f'/hangman/art-{cookie}.png', 'cookie': cookie }

        return context
    else:
        context = 'won'
        return context