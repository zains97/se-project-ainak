# Generated by Django 3.0.5 on 2020-12-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0060_buy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='', max_length=20)),
                ('email', models.TextField(default='', max_length=20)),
                ('pass1', models.TextField(default='', max_length=20)),
            ],
        ),
    ]
