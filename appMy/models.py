from django.db import models

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