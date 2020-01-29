from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Role(models.Model):
    COACH = 'C'
    PLAYER = 'P'

    ROLE_TYPES = [
        (COACH, 'Coach'),
        (PLAYER, 'Player')
    ]
    type = models.CharField(
        max_length=2,
        choices=ROLE_TYPES,
        default=PLAYER,
        verbose_name='type of role'
    )

    def __str__(self):
        return str(self.type)
        # return 'Type : %s, Id : %s' % (self.type, self.id)

    def get_id(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('role_detail', args=[str(self.id)])


class User_Role(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return 'User : %s, Role : %s' % (self.user.username, self.role.type)

    def get_absolute_url(self):
        return reverse('user_role', args=[str(self.id)])


class User_Stat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_time = models.DateTimeField(verbose_name='login date time', default=timezone.now)
    logout_time = models.DateTimeField(verbose_name='logout date time')

    def __str__(self):
        return str(self.login_time)

    def get_absolute_url(self):
        return reverse('user_stat_detail', args=[str(self.id)])


class Team(models.Model):
    name = models.TextField(max_length=100)
    abbr = models.TextField(max_length=3)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('team', args=[str(self.id)])


class Game(models.Model):
    host = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest')
    host_score = models.IntegerField()
    guest_score = models.IntegerField()
    date = models.DateField(verbose_name='game date')

    def __str__(self):
        return 'Game # %s' % (self.id)

    def get_absolute_url(self):
        return reverse('game', args=[str(self.id)])


class Team_Stat(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('team_stat', args=[str(self.id)])


class Coach(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # name = models.TextField(max_length=200)

    def __str__(self):
        return 'Name : %s %s' % (self.user.first_name, self.user.last_name)
        # return str(self.id)

    def get_absolute_url(self):
        return reverse('coach', args=[str(self.id)])


class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # name = models.TextField(max_length=200)
    height = models.IntegerField()

    def __str__(self):
        return 'Name : %s , Height : %s' % (self.user.first_name, self.height)

    def get_absolute_url(self):
        return reverse('player', args=[str(self.id)])


class Player_Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('player_stat', args=[str(self.id)])
