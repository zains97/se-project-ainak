# Generated by Django 3.0.5 on 2020-04-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0005_auto_20200414_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
    ]
