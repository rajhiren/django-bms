from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from bms.models import Team, Role, User_Role
from django.contrib.auth.models import User
from faker import Faker
from faker.providers import internet


class Command(BaseCommand):
    help = 'Polulate data for BMS'

    def team_data(self, fake):
        for t in range(15):
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
        for i in range(175):
            username = fake.user_name()
            try:
                user = User.objects.create_user(username=username, email=fake.safe_email(), password=username)
            except ObjectDoesNotExist:
                raise CommandError('User Model Does not exits')
            user.save()
            self.stdout.write(self.style.SUCCESS('User Created : "%s"' % user.username))

    def player_role_data(self, fake):
        users = User.objects.filter(is_superuser=False)
        role = Role.objects.filter(type='P')
        # role = Role.ROLE_TYPES
        # print(role)
        # for user in users[:1]:
        #     u = User_Role(user_id=user.id, roles_id=role[0], is_logged_in=fake.pybool())
        #     u.save()
        #     # print(user.id, role.get_id(), fake.pybool())


    def handle(self, *args, **options):
        fake = Faker()

        # initiate team data
        self.team_data(fake)

        # initiate role data
        self.role_data(fake)

        # initiate user data
        self.user_data(fake)

        # # initiate user_role data for players
        # self.player_role_data(fake)
