# Generated by Django 3.0.5 on 2020-12-24 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0061_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='click_item',
            name='admin_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recommend_system.Admin'),
            preserve_default=False,
        ),
    ]
