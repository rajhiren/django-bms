from django.core.management.base import BaseCommand, CommandError
from bms.models import Team, Role
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
    help = 'Polulate data for BMS'

    def team_data(self, fake):
        for t in range(15):
            try:
                t = Team(name=fake.slug(), abbr=fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            except Team.DoesNotExists:
                raise CommandError('Team Model Does not exists')
            t.save()
            self.stdout.write(self.style.SUCCESS('Successfully inserted Team : "%s" , Abbr : "%s"' % (t.name, t.abbr)))

    def role_data(self, fake):
        types = ['C', 'P']
        for type in range(len(types)):
            try:
                role = Role(type=types[type])
            except Role.DoesNotExists:
                raise CommandError('Role Model Does not exists')
            role.save()
            self.stdout.write(self.style.SUCCESS('Successfully inserted data for Role "%s"' % role.type))



    def handle(self, *args, **options):
        fake = Faker()

        # initiate team data
        self.team_data(fake)

        # initiate role data
        self.role_data(fake)