from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from bms.models import Team, Role, User_Role, Coach, Player
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from faker import Faker


class Command(BaseCommand):
    help = 'Populate data for BMS'

    def team_data(self, fake):
        for t in range(16):
            try:
                team = Team(name=fake.slug(), abbr=fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            except Team.DoesNotExists:
                raise CommandError('Team Model Does not exists')
            team.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully inserted Team : "%s" , Abbr : "%s"' % (team.name, team.abbr)))

    def role_data(self, fake):
        types = ['C', 'P']
        for type in range(len(types)):
            try:
                role = Role(type=types[type])
            except Role.DoesNotExists:
                raise CommandError('Role Model Does not exists')
            role.save()
            self.stdout.write(self.style.SUCCESS('Successfully inserted data for Role "%s"' % role.type))

    def user_data(self, fake):
        for i in range(176):
            username = fake.user_name()
            password = 'mydemo'
            try:
                user = User.objects.create_user(username=username, email=fake.safe_email(), password=password,
                                                first_name=fake.first_name(), last_name=fake.last_name())
            except ObjectDoesNotExist:
                raise CommandError('User Model Does not exits')
            user.save()
            self.stdout.write(self.style.SUCCESS('User Created : "%s"' % user.username))

    def user_role_data(self, fake):
        users = User.objects.filter(is_superuser=False)
        player = get_object_or_404(Role, type='P')
        coach = get_object_or_404(Role, type='C')

        # players mapping
        for user in users[:159]:
            try:
                p = User_Role(user_id=user.id, role_id=player.id, is_logged_in=fake.pybool())
            except player.DoesNotExists:
                raise CommandError('Issue in adding user role mapping')
            p.save()
            self.stdout.write(self.style.SUCCESS('User Role Mapped : { %s : %s }' % (user.username, player.type)))

        # coach mapping
        for user in users[159:]:
            try:
                u = User_Role(user_id=user.id, role_id=coach.id, is_logged_in=fake.pybool())
            except coach.DoesNotExists:
                raise CommandError('Issue in adding user role mapping')
            u.save()
            self.stdout.write(self.style.SUCCESS('User Role Mapped : { %s : %s }' % (user.username, coach.type)))

    def coach(self, fake):
        teams = Team.objects.all()
        coach = Role.objects.filter(type='C').first()
        users = User_Role.objects.filter(role_id=coach.id)

        for i in range(len(teams)):
            try:
                coach = Coach(team_id=teams[i].id, user_id=users[i].id)
            except Coach.DoesNotExists:
                raise CommandError('Issue with adding user as Coach')
            coach.save()
            self.stdout.write(self.style.SUCCESS('Coach Created  : %s ' % users[i].id))

    def player(self, fake):
        teams = Team.objects.all()
        player = Role.objects.filter(type='P').first()
        users = User_Role.objects.filter(role_id=player.id)

        for i in range(len(teams)):
            for j in range(10):
                print(teams[i].id,users[j].user.id, fake.random_int(min=170, max=255, step=1))
                # try:
                #     coach = Player(team_id=teams[i].id, user_id=users[j].id,
                #                    height=fake.random_int(min=170, max=255, step=1))
                # except Coach.DoesNotExists:
                #     raise CommandError('Issue with adding user as Player')
                # coach.save()
                # self.stdout.write(self.style.SUCCESS('Player Created  : %s ' % users[j].id))

    def handle(self, *args, **options):
        fake = Faker()

        # # initiate team data
        # self.team_data(fake)
        #
        # # initiate role data
        # self.role_data(fake)
        #
        # # initiate user data
        # self.user_data(fake)
        #
        # # initiate user_role data for players
        # self.user_role_data(fake)
        #
        # # initiate coach data
        # self.coach(fake)

        # initiate player
        self.player(fake)