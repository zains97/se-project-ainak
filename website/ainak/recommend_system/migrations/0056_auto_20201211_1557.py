# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0055_remove_home_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='landscape1',
        ),
        migrations.RemoveField(
            model_name='home',
            name='landscape2',
        ),
        migrations.RemoveField(
            model_name='home',
            name='landscape3',
        ),
    ]
