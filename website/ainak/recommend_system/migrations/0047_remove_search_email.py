# Generated by Django 3.0.5 on 2020-10-06 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0046_remove_search_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='email',
        ),
    ]
