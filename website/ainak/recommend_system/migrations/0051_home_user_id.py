# Generated by Django 3.0.5 on 2020-11-09 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0050_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recommend_system.User'),
        ),
    ]