# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0058_auto_20201211_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='landscape1',
            field=models.ImageField(default='', upload_to='recommend_system/images'),
        ),
        migrations.AddField(
            model_name='home',
            name='landscape2',
            field=models.ImageField(default='', upload_to='recommend_system/images'),
        ),
        migrations.AddField(
            model_name='home',
            name='landscape3',
            field=models.ImageField(default='', upload_to='recommend_system/images'),
        ),
    ]
