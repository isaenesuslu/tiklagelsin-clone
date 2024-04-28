"""
URL configuration for tiklagelsin_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appMy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Anasayfa, name="Anasayfa"),
    path('ozel-menuler', ozelMenuler, name="ozelMenuler"),
    path('template', TemplatePage),
    path('burger', burgerPage),
    # BLOG
    path('blog', blogPage, name="blogPage"),
    path('menuler', Menuler),
    path('tarifler', Tarifler),
    path('trend-eglence', TrendEglence),
    path('detaylar/<slug>', BlogDetaylar),
    # HESAP AYARLARI
    path('a', hesapgirisPage, name="hesapgirisPage"),
    path('hesabim', hesabimPage, name="hesabimPage"),
    path('adreslerim', adressPage, name="adressPage"),
    path('cuzdanim', cuzdanimPage, name="cuzdanimPage"),
    path('kuponlarim', kuponlarimPage, name="kuponPage"),
    path('odeme-bilgilerim', odemePage, name="odemePage"),
    path('profil-bilgilerim', profilPage, name="profilPage"),
    path('tiklaparam', tiklaparamPage, name="tiklaparamPage"),
    path('ayarlarim', settingsPage, name="settingsPage"),
    path('sepetim', sepetimPage, name="sepetimPage"),
    path('siparislerim', siparislerimPage, name="siparislerimPage"),
    path('siparis-onay', siparisonayPage, name="siparisonayPage"),
    path('menudetay/<dt>', menuDetayPage),
    path('adres-ekle', adreseklePage, name="adreseklePage"),
    path('logout', logoutUser, name="logoutPage"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
