# Generated by Django 3.0.5 on 2020-10-06 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0030_auto_20200925_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='category',
        ),
        migrations.RemoveField(
            model_name='search',
            name='city',
        ),
        migrations.RemoveField(
            model_name='search',
            name='location',
        ),
        migrations.RemoveField(
            model_name='search',
            name='price',
        ),
        migrations.RemoveField(
            model_name='search',
            name='sft',
        ),
    ]
