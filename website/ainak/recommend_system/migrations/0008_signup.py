# Generated by Django 3.0.5 on 2020-04-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0007_auto_20200416_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(default='', max_length=20)),
                ('fname', models.CharField(default='', max_length=20)),
                ('lname', models.CharField(default='', max_length=20)),
                ('email', models.TextField(default='', max_length=20)),
                ('pass1', models.TextField(default='', max_length=20)),
                ('pass2', models.TextField(default='', max_length=20)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
    ]
