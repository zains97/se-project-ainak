# Generated by Django 3.0.5 on 2020-12-10 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0053_remove_home_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='location',
            new_name='glassesname',
        ),
        migrations.RemoveField(
            model_name='home',
            name='email',
        ),
        migrations.RemoveField(
            model_name='home',
            name='landscape4',
        ),
        migrations.RemoveField(
            model_name='home',
            name='landscape5',
        ),
        migrations.RemoveField(
            model_name='home',
            name='name',
        ),
        migrations.RemoveField(
            model_name='home',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='home',
            name='portrait',
        ),
        migrations.RemoveField(
            model_name='home',
            name='sft',
        ),
        migrations.RemoveField(
            model_name='home',
            name='status',
        ),
    ]