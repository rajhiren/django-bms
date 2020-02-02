from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .models import Player, Player_Stat, Team, Game, User_Role, Team_Stat, User_Stat
from django.db.models import Avg, Sum, Count
from django.contrib.auth.decorators import login_required
from django.db.models import ExpressionWrapper, F, fields

from django.shortcuts import get_object_or_404


@login_required
def index(request):
    games = Game.objects.all()
    user_role = User_Role.objects.get(user_id=request.user.id)
    context = {
        'games': games,
        'user_role': user_role,
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
    user_role = User_Role.objects.get(user_id=request.user.id)
    if user_role.role.type != 'P':

        players = Player.objects.filter(team_id=team_id)
        context = {
            'players': players,
            'average_score': Team_Stat.objects.filter(team_id=team_id).aggregate(Avg('score')),
        }
        return render(request, 'bms/team.html', context)
    else:
        return HttpResponseForbidden()


@login_required
def scoreboard(request):
    games = Game.objects.all()
    user_role = User_Role.objects.get(user_id=request.user.id)
    context = {
        'games': games,
        'user_role': user_role,
    }
    return render(request, 'bms/home.html', context)

@login_required
def stats(request):
    user_role = User_Role.objects.get(user_id=request.user.id)
    if user_role.role.type == 'A':
        duration = ExpressionWrapper(F('logout_time') - F('login_time'), output_field=fields.DurationField())
        stats = User_Stat.objects.values('user_id').annotate(duration=Sum(duration)).annotate(
            dcount=Count('user_id')).filter(duration__gt=timedelta(seconds=2)).order_by('user_id')

        context = {
            'stats' : stats,
            'total_online' : User_Role.objects.filter(is_logged_in=True).aggregate(Count('id')),
            'online_users' : User_Role.objects.filter(is_logged_in=True).values_list('user_id', flat=True),
        }
        return render(request, 'bms/stats.html', context)
    else:
        return HttpResponseForbidden()
