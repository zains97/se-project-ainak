# Generated by Django 3.0.5 on 2020-10-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0039_auto_20201006_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recommend_system.Home'),
        ),
        migrations.AlterField(
            model_name='search',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recommend_system.User'),
        ),
    ]
