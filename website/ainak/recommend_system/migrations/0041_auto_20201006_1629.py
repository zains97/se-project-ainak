# Generated by Django 3.0.5 on 2020-10-06 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0040_auto_20201006_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='post_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recommend_system.Home'),
        ),
    ]
