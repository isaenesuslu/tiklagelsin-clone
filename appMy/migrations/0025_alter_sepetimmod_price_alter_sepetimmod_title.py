# Generated by Django 4.2.10 on 2024-04-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0024_remove_sepetimmod_additionalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepetimmod',
            name='price',
            field=models.CharField(blank=True, max_length=50, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='sepetimmod',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Menü Başlık'),
        ),
    ]