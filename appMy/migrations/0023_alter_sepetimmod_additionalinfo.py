# Generated by Django 4.2.10 on 2024-04-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0022_adresmod_aktif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepetimmod',
            name='additionalinfo',
            field=models.CharField(max_length=650, verbose_name='Menü İçerik'),
        ),
    ]