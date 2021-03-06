# Generated by Django 3.0.5 on 2020-10-10 11:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0048_auto_20201006_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='post_id',
        ),
        migrations.AddField(
            model_name='click_item',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='search',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='search',
            name='city',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='search',
            name='location',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='search',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='search',
            name='sft',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wish_list',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='search',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recommend_system.User'),
        ),
    ]
