# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20140927_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeBegin', models.DateTimeField(auto_now_add=True)),
                ('channelName', models.CharField(max_length=100)),
                ('gameStatus', models.CharField(max_length=50)),
                ('gameMembers', models.ManyToManyField(to='players.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameEndResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_end', models.DateTimeField(auto_now_add=True)),
                ('position', models.IntegerField()),
                ('game', models.ForeignKey(to='game.Game')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionUnitTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstInput2', models.CharField(max_length=50)),
                ('secondInput2', models.CharField(max_length=50)),
                ('result2', models.CharField(max_length=300)),
                ('question2', models.ForeignKey(to='game.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='question',
            field=models.ForeignKey(to='game.Question'),
            preserve_default=True,
        ),
    ]
