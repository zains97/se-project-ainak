# Generated by Django 3.0.5 on 2021-01-03 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0071_auto_20210103_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='lefteye',
            new_name='leye',
        ),
        migrations.RenameField(
            model_name='buy',
            old_name='righteye',
            new_name='reye',
        ),
    ]
