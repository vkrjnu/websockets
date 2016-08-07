# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fibo', '0002_auto_20160725_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacci',
            name='output',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=1),
        ),
    ]
