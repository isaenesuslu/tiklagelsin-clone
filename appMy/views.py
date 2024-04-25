from django.shortcuts import render
from appMy.models import *

# Create your views here.

def Anasayfa(request):
    context = {}
    return render(request, 'anasayfa/anasayfa.html', context)

def ozelMenuler(request):
    context = {}
    return render(request, 'anasayfa/ozelmenuler.html', context)

def blogPage(request):
    
    import random
    
    carousel_list = []
    carousel_list2 = []
    detay_list = []
    sonkart = ""
    detay_list += MenulerMod.objects.all()
    detay_list += TariflerMod.objects.all()
    detay_list += TrendEglenceMod.objects.all()
    
    random.shuffle(detay_list)
    sonsuz_elemanlar = set()

    # Sayfa her yenilendiğinde blog ana sayfanın carousel yapısına rastgele bloglar gönderiyor. 

    for item in detay_list:
        if len(carousel_list) == 8:
         break

        if item not in sonsuz_elemanlar:
            carousel_list.append(item)
            sonsuz_elemanlar.add(item)
            if len(carousel_list2) < 6:
                carousel_list2.append(item)

    for sonitem in detay_list:
        if sonitem not in carousel_list:
            sonkart = sonitem
            break
            
    
    context = {
        "carousel_list":carousel_list,
        "carousel_list2":carousel_list2,
        "sonkart":sonkart,
    }
    return render(request, 'blog/bloganasayfa.html', context)

def Menuler(request):
    
    menu_list = MenulerMod.objects.all()
    
    context = {
        "menu_list":menu_list,
    }
    return render(request, 'blog/blogmenuler.html', context)

def Tarifler(request):
    
    tarif_list = TariflerMod.objects.all()
    
    context = {
        "tarif_list":tarif_list,
    }
    return render(request, 'blog/blogtarifler.html', context)

def TrendEglence(request):
    
    trendeglence_list = TrendEglenceMod.objects.all
    
    context = {
        "trendeglence_list":trendeglence_list,
    }
    return render(request, 'blog/blogtrendeglence.html', context)

def BlogDetaylar(request, slug):
    
    detay = ''
    detay_list = []
    detay_list += MenulerMod.objects.all()
    detay_list += TariflerMod.objects.all()
    detay_list += TrendEglenceMod.objects.all()
    
    import random
    random.shuffle(detay_list)
    sonsuz_elemanlar = set()
    carousel_list = []
    carousel_list2 = []
    carousel_list3 = []

    for item in detay_list:
        if len(carousel_list) == 3:
            break
        #* <<-- MEVCUT SAYFANIN ÖNERİSİ ALT CAROUSEL'DE GÖSTERİLMESİN -->>
        if item.slug == slug:
            continue 
        if item not in sonsuz_elemanlar:
            carousel_list.append(item)
            sonsuz_elemanlar.add(item)  
            
    for item2 in detay_list:
        if len(carousel_list2) == 3:
            break
        #* <<-- MEVCUT SAYFANIN ÖNERİSİ ALT CAROUSEL'DE GÖSTERİLMESİN -->>
        if item2.slug == slug:
            continue 
        if item2 not in sonsuz_elemanlar:
            carousel_list2.append(item2)
            sonsuz_elemanlar.add(item2)         
    
    for item3 in detay_list:
        if len(carousel_list3) == 3:
            break
        #* <<-- MEVCUT SAYFANIN ÖNERİSİ ALT CAROUSEL'DE GÖSTERİLMESİN -->>
        if item3.slug == slug:
            continue 
        if item3 not in sonsuz_elemanlar:
            carousel_list3.append(item3)
            sonsuz_elemanlar.add(item3)         
        
        
    for i in detay_list:
        if i.slug == slug:
            detay = i

    context = {
        "detay":detay,
        "carousel_list":carousel_list,
        "carousel_list2":carousel_list2,
        "carousel_list3":carousel_list3,
    }
    return render(request, 'blog/blogdetaylar.html', context)


def TemplatePage(request):
    context = {}
    return render(request, 'anasayfa/uruntemplate.html', context)

def burgerPage(request):
    context = {}
    return render(request, 'anasayfa/burgerking.html', context)


# HESAP AYARLARI

def hesapgirisPage(request):
    context = {}
    return render(request, 'hesabim/hesabimgiris.html', context)

def hesabimPage(request):
    context = {}
    return render(request, 'hesabim/hesabim.html', context)

def adressPage(request):
    context = {}
    return render(request, 'hesabim/adress.html', context)

def cuzdanimPage(request):
    context = {}
    return render(request, 'hesabim/cuzdanim.html', context)

def kuponlarimPage(request):
    context = {}
    return render(request, 'hesabim/kuponlarim.html', context)

def odemePage(request):
    context = {}
    return render(request, 'hesabim/odemebilgilerim.html', context)

def profilPage(request):
    context = {}
    return render(request, 'hesabim/profilbilgilerim.html', context)

def tiklaparamPage(request):
    context = {}
    return render(request, 'hesabim/tiklaparam.html', context)

def settingsPage(request):
    context = {}
    return render(request, 'hesabim/settings.html', context)

def sepetimPage(request):
    context = {}
    return render(request, 'hesabim/sepetim.html', context)

def siparislerimPage(request):
    context = {}
    return render(request, 'hesabim/siparislerim.html', context)

def siparisonayPage(request):
    context = {}
    return render(request, 'hesabim/siparisonay.html', context)

def menuDetayPage(request, dt):
    context = {}
    return render(request, 'anasayfa/burgermenus/detaysayfasi.html', context)

def adreseklePage(request):
    context = {}
    return render(request, 'hesabim/adresekle.html', context)

