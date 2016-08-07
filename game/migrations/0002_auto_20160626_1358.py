# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('player', models.ForeignKey(to='game.Player')),
            ],
        ),
        migrations.RemoveField(
            model_name='joingame',
            name='Join_game',
        ),
        migrations.DeleteModel(
            name='JoinGame',
        ),
    ]
