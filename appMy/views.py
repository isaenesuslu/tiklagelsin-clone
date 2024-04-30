from django.shortcuts import render, redirect
from appMy.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from tiklagelsin_clone.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
    submit = request.POST.get("submit")
    code = ""
    if request.method == "POST":
        email = request.POST.get("email")
        import random
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if submit == "kayit-ol":
                if email: 
                    request.session['email'] = email
                    while(len(code) < 6):
                        while(len(code) < 3):
                            code += random.choice(alphabet)
                        rastgeleSayi = random.randint(0,9)
                        code += str(rastgeleSayi)
                        request.session['code'] = code
                    send_mail(
                        "Devam etmek için kodunuz",
                        code,
                        EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                    )
                    messages.success(request, "Devam etmek için oluşturulan kodunuz mail adresinize başarıyla gönderilmiştir. Lütfen kodu giriniz:")
                    return redirect("hesapgirisPage")  
        if submit == "kayit-onay":
            onaykodu = request.POST.get("onay-kodu")
            code = request.session.get('code')
            email = request.session.get('email')
            if onaykodu == code:
                    if not User.objects.filter(email=email).exists():
                        user = User(username=email, email=email)
                        user.save()
                        ekbilgi = ekbilgiMod(user=user)
                        ekbilgi.save()
                        sepet = sepetimPage(user=user)
                        sepet.save()
                        login(request,user)
                        messages.success(request,"Başarıyla kayıt oldunuz. Profil bilgilerinizi güncelleyebilirsiniz.")
                        return redirect("profilPage")
                    else:
                        user = User.objects.get(email=email)
                        login(request,user)
                        messages.success(request, "Başarıyla giriş yaptınız.")
                        return redirect("Anasayfa")
            else:
                messages.warning(request, "HATALI KOD GİRDİNİZ! LÜTFEN TEKRAR GİRİNİZ.")
    
    context = {}
    return render(request, 'hesabim/hesabimgiris.html', context)

@login_required(login_url='hesapgirisPage')
def hesabimPage(request):
    context = {}
    return render(request, 'hesabim/hesabim.html', context)

@login_required(login_url='hesapgirisPage')
def adressPage(request):
    
    
    if request.method == "POST":
        submit = request.POST.get("submit")
        if AdresMod.objects.filter(aktif=True).exists():
            eskiadres = AdresMod.objects.get(aktif=True)
            eskiadres.aktif = False
            eskiadres.save()
        adres = AdresMod.objects.get(title=submit)
        adres.aktif = True
        adres.save()
        messages.success(request, "Adresiniz başarıyla güncellenmiştir.")
        return redirect("adressPage")
        
        
    
    
    adress_list = AdresMod.objects.filter(user=request.user)
    context = {
        "adress_list":adress_list,
    }
    return render(request, 'hesabim/adress.html', context)

@login_required(login_url='hesapgirisPage')
def cuzdanimPage(request):
    context = {}
    return render(request, 'hesabim/cuzdanim.html', context)

@login_required(login_url='hesapgirisPage')
def kuponlarimPage(request):
    context = {}
    return render(request, 'hesabim/kuponlarim.html', context)

@login_required(login_url='hesapgirisPage')
def odemePage(request):
    context = {}
    return render(request, 'hesabim/odemebilgilerim.html', context)

@login_required(login_url='hesapgirisPage')
def profilPage(request):
    
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        tel = request.POST.get("tel")
        cinsiyet = request.POST.get("cinsiyet")
        takim = request.POST.get("takim")

        if fname or lname or email or tel or cinsiyet or takim:
            if fname:
                request.user.first_name = fname
            if lname:
                request.user.last_name = lname
            if email:
                if "@" in email and ".com" in email:
                    request.user.email = email
                else:
                    messages.warning(request, "Lütfen geçerli bir mail giriniz.")
            if tel:
                if len(tel) >= 10 and tel.isdigit():
                    request.user.ekbilgimod.tel = tel
                else:
                    messages.warning(request, "Lütfen geçerli bir telefon numarası giriniz.")
            if cinsiyet:
                request.user.ekbilgimod.cinsiyet = cinsiyet
            if takim:
                request.user.ekbilgimod.takim = takim
                
            request.user.save()
            request.user.ekbilgimod.save()
            return redirect("profilPage")
        else:
            messages.warning(request, "Lütfen en az bir alanı doldurun.")
                
    
    context = {}
    return render(request, 'hesabim/profilbilgilerim.html', context)

@login_required(login_url='hesapgirisPage')
def tiklaparamPage(request):
    context = {}
    return render(request, 'hesabim/tiklaparam.html', context)

@login_required(login_url='hesapgirisPage')
def settingsPage(request):
    context = {}
    return render(request, 'hesabim/settings.html', context)

@login_required(login_url='hesapgirisPage')
def sepetimPage(request):
    title = request.GET.get('title')
    total_price = request.GET.get('total_price')
    user_adres = AdresMod.objects.filter(Q(aktif=True) & Q(user=request.user))
    user_sepet = SepetimMod.objects.filter(user=request.user)
    
    if not SepetimMod.objects.filter(title=title).exists():
        if title and total_price:    
            userSave = SepetimMod(user=request.user, title=title, price=total_price)
            userSave.save()
            user_sepet = SepetimMod.objects.filter(Q(user=request.user) & Q(title=title) & Q(price=total_price))
    user_sepet = list(user_sepet)
    if user_sepet[0].price:
        pass
    else:
        user_sepet.pop(0)
    
    toplam_fiyat = 0
    for p in user_sepet:
       toplam_fiyat += float(p.price)

    print(toplam_fiyat)
    
    context = {
        'title': title,
        'total_price': total_price,
        'user_adres': user_adres,
        'user_sepet': user_sepet,
        'toplam_fiyat': toplam_fiyat,
    }
    return render(request, 'hesabim/sepetim.html', context)

@login_required(login_url='hesapgirisPage')
def siparislerimPage(request):
    context = {}
    return render(request, 'hesabim/siparislerim.html', context)

@login_required(login_url='hesapgirisPage')
def siparisonayPage(request):
    user_adres = AdresMod.objects.filter(Q(aktif=True) & Q(user=request.user))
    user_sepet = SepetimMod.objects.filter(user=request.user)
    user_sepet = list(user_sepet)
    if user_sepet[0].price:
        pass
    else:
        user_sepet.pop(0)
    
    toplam_fiyat = 0
    for p in user_sepet:
       toplam_fiyat += float(p.price)
    
    context = {
        "user_adres" : user_adres,
        "toplam_fiyat" : toplam_fiyat,
    }
    return render(request, 'hesabim/siparisonay.html', context)

def menuDetayPage(request, dt):
    context = {}
    return render(request, 'anasayfa/burgermenus/detaysayfasi.html', context)

@login_required(login_url='hesapgirisPage')
def adreseklePage(request):
    
    if request.method == "POST":
        adrestitle = request.POST.get("adres-title")
        adrestype = request.POST.get("adres-tipi")
        il = request.POST.get("il")
        ilce = request.POST.get("ilce")
        mahalle = request.POST.get("mahalle")
        cadde = request.POST.get("cadde")
        sokak = request.POST.get("sokak")
        binano = request.POST.get("binano")
        daireno = request.POST.get("daireno")
        binaadi = request.POST.get("binaadi")
        adrestarifi = request.POST.get("adrestarifi")
        
        if adrestitle and adrestype and il and ilce and mahalle and cadde and sokak and binano and daireno and binaadi and adrestarifi:
            userSave = AdresMod(user=request.user, title=adrestitle, adrestype=adrestype, il=il, ilce=ilce, mahalle=mahalle, cadde=cadde, sokak=sokak, binano=binano, daireno=daireno, bina=binaadi, adrestarif=adrestarifi)
            userSave.save()
            messages.success(request, "Adresiniz başarıyla eklenmiştir.")
            return redirect("adressPage")
        else:
            messages.warning(request, "Bütün alanlar dolu olmak zorundadır!")
    
    context = {}
    return render(request, 'hesabim/adresekle.html', context)

@login_required(login_url='hesapgirisPage')
def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapıldı.")
    return redirect("Anasayfa")
