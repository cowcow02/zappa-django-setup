from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import User
from django.utils import timezone


def createSuperUsers(apps, schema_editor):
    User.objects.create_superuser('admin@example.com', 'admin@example.com', 'generatedpassword',
                                  last_login=timezone.now())


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(createSuperUsers)
    ]
