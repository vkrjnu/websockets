# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacci',
            name='num',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='fibonacci',
            name='output',
            field=models.BigIntegerField(default=1),
        ),
    ]
