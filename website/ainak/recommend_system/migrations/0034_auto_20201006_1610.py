# Generated by Django 3.0.5 on 2020-10-06 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0033_search_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='email',
        ),
        migrations.RemoveField(
            model_name='search',
            name='post_id',
        ),
    ]
