# Generated by Django 3.0.5 on 2021-01-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0066_auto_20210103_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='lefteye',
            field=models.IntegerField(default='NA'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='righteye',
            field=models.IntegerField(default='NA'),
        ),
    ]