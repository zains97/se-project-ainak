# Generated by Django 3.0.5 on 2020-08-16 05:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0011_auto_20200816_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('date_comment', models.DateField(default=datetime.date.today)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_system.Home')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_system.User')),
            ],
        ),
    ]
