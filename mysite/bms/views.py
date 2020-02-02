from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Player_Stat, Team, Game, User_Role
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def index(request):
    # user = request.user
    user = User.objects.get(username=request.user.username)
    user_role = User_Role.objects.get(user_id=user.id)
    context = {
        'user_role': user_role,
        'test' : request.user
    }
    return render(request, 'bms/home.html', context)


def coach(request):
    return HttpResponse('take this')


@login_required
def player(request, player_id=None):
    player = Player.objects.filter(id=player_id).first()
    stat = Player_Stat.objects.filter(player_id=player_id)
    context = {
        'player': player,
        'player_id': player.id,
        'team': player.team.name,
        'games': len(stat),
        'average_score': Player_Stat.objects.aggregate(Avg('score'))
    }
    return render(request, 'bms/player.html', context)


@login_required
def team(request, team_id=None):
    # teams = Team.objects.all()
    team = Team.objects.filter(id=team_id)
    context = {
        'team': team,
        'team_id': team_id,
    }
    return render(request, 'bms/team.html', context)


@login_required
def scoreboard(request):
    games = Game.objects.all()
    context = {
        'games': games,
        'test': request.body
    }
    return render(request, 'bms/home.html', context)