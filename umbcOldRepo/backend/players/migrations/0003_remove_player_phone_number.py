# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='phone_number',
        ),
    ]
