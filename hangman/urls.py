from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('game', views.game, name='game'),
    path('lose', views.lose, name='lose'),
    path('won', views.won, name='won')
]