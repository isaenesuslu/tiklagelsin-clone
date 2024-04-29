# Generated by Django 4.2.10 on 2024-04-28 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0019_sepetimmod_adresmod'),
    ]

    operations = [
        migrations.CreateModel(
            name='ekbilgiMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=50, verbose_name='Telefon Numarası')),
                ('cinsiyet', models.CharField(max_length=50, verbose_name='Cinsiyet')),
                ('takim', models.CharField(max_length=50, verbose_name='Takım')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]