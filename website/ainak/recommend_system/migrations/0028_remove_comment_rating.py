# Generated by Django 3.0.5 on 2020-09-25 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0027_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
    ]