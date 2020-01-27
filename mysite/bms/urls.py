from django.http import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coach_detail', views.coach_detail, name='coach'),
    # ex: /bms/player/1
    path('player/<int:player_id>/', views.player_detail, name='player'),
    # path('player/', views.player, name='player'),
    path('team/', views.team_detail, name='team'),
    path('scoreboard/', views.scoreboard, name='home')
]
