from django.http import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coach/<int:coach_id>', views.coach, name='coach'),
    # ex: /bms/player/1
    path('player/<int:player_id>/', views.player, name='player'),
    path('player/', views.player, name='player'),
    path('team/', views.team, name='team'),
    path('team/<int:team_id>/', views.team, name='team'),
    path('scoreboard/', views.scoreboard, name='home')
]
