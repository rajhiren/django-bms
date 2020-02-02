from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Player_Stat, Team, Game, User_Role, Team_Stat, User_Stat
# from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def index(request):
    user = request.user
    # user = User.objects.get(id=request.user.id)
    user_role = User_Role.objects.filter(user_id=10)
    # user_role = get_object_or_404(User_Role, user_id=10)
    context = {
        'user_role': user_role,
        # 'test' : "test",
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
        'average_score': Player_Stat.objects.filter(player_id=player_id).aggregate(Avg('score'))
    }
    return render(request, 'bms/player.html', context)


@login_required
def team(request, team_id=None):
    players = Player.objects.filter(team_id=team_id)
    context = {
        'players': players,
        'average_score': Team_Stat.objects.filter(team_id=team_id).aggregate(Avg('score')),
    }
    return render(request, 'bms/team.html', context)


@login_required
def scoreboard(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'bms/home.html', context)

@login_required
def user_stat(request):
    stats = User_Stat.objects.all()
    context = {
        'stats' : stats
    }
    return render(request, 'bms/user_stat.html', context)
