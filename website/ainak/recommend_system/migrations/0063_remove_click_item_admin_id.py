# Generated by Django 3.0.5 on 2020-12-24 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0062_click_item_admin_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='click_item',
            name='admin_id',
        ),
    ]
