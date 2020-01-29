from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    def generate_superuser(self, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = 'mydemo'
        DJANGO_SU_EMAIL = 'hiren.raj@gmail.com'
        DJANGO_SU_PASSWORD = 'mydemo'

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]