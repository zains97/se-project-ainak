# Generated by Django 3.0.5 on 2020-08-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0010_auto_20200430_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='', max_length=20)),
                ('fname', models.CharField(default='', max_length=20)),
                ('lname', models.CharField(default='', max_length=20)),
                ('email', models.TextField(default='', max_length=20)),
                ('pass1', models.TextField(default='', max_length=20)),
                ('pass2', models.TextField(default='', max_length=20)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.DeleteModel(
            name='Temp',
        ),
    ]
