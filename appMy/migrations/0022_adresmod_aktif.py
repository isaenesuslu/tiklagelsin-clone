# Generated by Django 4.2.10 on 2024-04-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0021_alter_ekbilgimod_cinsiyet_alter_ekbilgimod_takim'),
    ]

    operations = [
        migrations.AddField(
            model_name='adresmod',
            name='aktif',
            field=models.BooleanField(null=True, verbose_name='Aktif Adres'),
        ),
    ]
