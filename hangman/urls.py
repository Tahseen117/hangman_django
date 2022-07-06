from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('game', views.game, name='game')
]