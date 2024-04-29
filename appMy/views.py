from django.shortcuts import render, redirect
from appMy.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from tiklagelsin_clone.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required

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
                        print(code)
                    # send_mail(
                    #     "Kayıt olmak için kodunuz",
                    #     code,
                    #     EMAIL_HOST_USER,
                    #     [email],
                    #     fail_silently=False,
                    # )
                    messages.success(request, "Giriş yapmak için oluşturulan kodunuz mail adresinize başarıyla gönderilmiştir. Lütfen kodu giriniz:")
                    return redirect("hesapgirisPage")  
        if submit == "kayit-onay":
            onaykodu = request.POST.get("onay-kodu")
            code = request.session.get('code')
            email = request.session.get('email')
            print(onaykodu)
            if onaykodu == code:
                    if not User.objects.filter(email=email).exists():
                        user = User(username=email, email=email)
                        user.save()
                        ekbilgi = ekbilgiMod(user=user)
                        ekbilgi.save()
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
    context = {}
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
    options = request.GET.get('options')

    context = {
        'title': title,
        'total_price': total_price,
        'options': options,
    }
    return render(request, 'hesabim/sepetim.html', context)

@login_required(login_url='hesapgirisPage')
def siparislerimPage(request):
    context = {}
    return render(request, 'hesabim/siparislerim.html', context)

@login_required(login_url='hesapgirisPage')
def siparisonayPage(request):
    context = {}
    return render(request, 'hesabim/siparisonay.html', context)

def menuDetayPage(request, dt):
    context = {}
    return render(request, 'anasayfa/burgermenus/detaysayfasi.html', context)

@login_required(login_url='hesapgirisPage')
def adreseklePage(request):
    context = {}
    return render(request, 'hesabim/adresekle.html', context)

@login_required(login_url='hesapgirisPage')
def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yapıldı.")
    return redirect("Anasayfa")
