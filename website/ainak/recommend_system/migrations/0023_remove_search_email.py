# Generated by Django 3.0.5 on 2020-09-22 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0022_auto_20200922_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='email',
        ),
    ]
