# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20160626_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('game', models.ForeignKey(to='game.Game')),
            ],
        ),
    ]
