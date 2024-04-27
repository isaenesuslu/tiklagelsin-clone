from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MenulerMod(models.Model):
    title = models.CharField(("Başlık"), max_length=100)
    subtitle = models.CharField(("Alt başlık"), max_length=450)
    text = models.TextField(("İçerik"), null=True, blank=True)
    image = models.ImageField(("Fotoğraf"), upload_to=None, height_field=None, blank=True)
    category = models.CharField(("Kategori"), max_length=50, null=True)
    slug = models.SlugField(("Slug"), null=True)
    read_time = models.CharField(("Okuma Süresi"), max_length=50, null=True)
    date = models.DateField(("Tarih"), auto_now=False, auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.title
    
class TariflerMod(models.Model):
    title = models.CharField(("Başlık"), max_length=100)
    subtitle = models.CharField(("Alt başlık"), max_length=450)
    text = models.TextField(("İçerik"), null=True, blank=True)
    image = models.ImageField(("Fotoğraf"), upload_to=None, height_field=None, blank=True)
    category = models.CharField(("Kategori"), max_length=50, null=True)
    slug = models.SlugField(("Slug"), null=True)
    read_time = models.CharField(("Okuma Süresi"), max_length=50, null=True)
    date = models.DateField(("Tarih"), auto_now=False, auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.title
    
class TrendEglenceMod(models.Model):
    title = models.CharField(("Başlık"), max_length=100)
    subtitle = models.CharField(("Alt başlık"), max_length=450)
    text = models.TextField(("İçerik"), null=True, blank=True)
    image = models.ImageField(("Fotoğraf"), upload_to=None, height_field=None, blank=True)
    category = models.CharField(("Kategori"), max_length=50, null=True)
    slug = models.SlugField(("Slug"), null=True)
    read_time = models.CharField(("Okuma Süresi"), max_length=50, null=True)
    date = models.DateField(("Tarih"), auto_now=False, auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.title
    
class SepetimMod(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Menü Başlık"), max_length=150)
    additionalinfo = models.CharField(("Menü İçerik"), max_length=150)
    price = models.CharField(("Fiyat"), max_length=50)
    
class AdresMod(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title = models.CharField(("Adres Başlığı"), max_length=50)
    adrestype = models.CharField(("Adres Tipi"), max_length=50)
    il = models.CharField(("İl"), max_length=50)
    ilce = models.CharField(("İlce"), max_length=50)
    mahalle = models.CharField(("Mahalle"), max_length=50)
    cadde = models.CharField(("Cadde"), max_length=50)
    sokak = models.CharField(("Sokak"), max_length=50)
    binano = models.CharField(("Bina No"), max_length=50)
    daireno = models.CharField(("Daire No"), max_length=50)
    bina = models.CharField(("Bina Adı"), max_length=50)
    adrestarif = models.CharField(("Adres Tarifi"), max_length=50)