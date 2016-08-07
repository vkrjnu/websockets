# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20160704_1809'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameColor',
            new_name='GamePlayer',
        ),
        migrations.AlterField(
            model_name='gameplayer',
            name='player',
            field=models.ForeignKey(to='game.Player'),
        ),
    ]
