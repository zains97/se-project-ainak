# Generated by Django 3.0.5 on 2020-09-22 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0019_auto_20200827_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='User email')),
                ('category', models.CharField(default='', max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=70)),
                ('price', models.IntegerField(default=0)),
                ('sft', models.IntegerField(default=0)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_system.Home')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend_system.User')),
            ],
        ),
    ]
