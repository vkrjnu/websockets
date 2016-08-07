# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_gamecolor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamecolor',
            old_name='game',
            new_name='player',
        ),
    ]
