# Generated by Django 3.0.5 on 2020-10-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_system', '0037_remove_search_post_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='User email')),
            ],
        ),
        migrations.DeleteModel(
            name='Search',
        ),
    ]
