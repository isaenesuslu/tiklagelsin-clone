# Generated by Django 4.2.8 on 2024-01-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0016_menulermod_date_tariflermod_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menulermod',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tariflermod',
            name='date',
        ),
        migrations.RemoveField(
            model_name='trendeglencemod',
            name='date',
        ),
    ]
