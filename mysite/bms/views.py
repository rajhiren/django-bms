from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Player_Stat, Team, Game
from django.db.models import Avg
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return HttpResponse("Basketball management system")


def coach_detail(request):
    return HttpResponse('take this')


@login_required
def player_detail(request, player_id=None):
    player = Player.objects.filter(id=player_id).first()
    stat = Player_Stat.objects.filter(player_id=player_id)
    context = {
        'player': player,
        'team': player.team.name,
        'games': len(stat),
        'average_score': Player_Stat.objects.aggregate(Avg('score'))
    }
    return render(request, 'bms/player.html', context)


@login_required
def team_detail(request, team_id=None):
    teams = Team.objects.all()
    # team = Team.objects.filter(id=team_id)
    context = {
        'teams': teams,
    }
    return render(request, 'bms/team.html', context)


@login_required
def scoreboard(request):
    games = Game.objects.all()
    context = {
        'games' : games,
    }
    return render(request, 'bms/home.html', context)

