# Generated by Django 3.0.5 on 2021-01-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0065_auto_20201230_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='lefteye',
            field=models.IntegerField(default='N/A'),
        ),
        migrations.AddField(
            model_name='buy',
            name='righteye',
            field=models.IntegerField(default='N/A'),
        ),
    ]
