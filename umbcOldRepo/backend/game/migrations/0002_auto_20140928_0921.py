# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionunittest',
            old_name='firstInput2',
            new_name='firstInput',
        ),
        migrations.RenameField(
            model_name='questionunittest',
            old_name='question2',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='questionunittest',
            old_name='result2',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='questionunittest',
            old_name='secondInput2',
            new_name='secondInput',
        ),
    ]
