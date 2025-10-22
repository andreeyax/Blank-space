from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
import random
from .duel import duel_runda, nova_soba, provera_sobe, provera_dosao, obrada_rezultata, gotov_duel, provera_zavrsio, obrisi_ako_postoji_soba
import json
import re

from .models import Predlaze_Izvodjaca,Predlaze_Pesmu,Zanr,Izvodjac,Pesma
from .predlozi import *
from .models import Predlaze_Izvodjaca,Predlaze_Pesmu,Zanr,Izvodjac,Korisnik

from .viewsM import *


# Autori: Svi članovi tima

# pomocne funkcije

def logout(request):
    """
    Izloguje korisnika i vrati ga na pocetnu stranicu.
    """
    request.session.flush()
    response = pocetna(request)
    response.delete_cookie('korisnickoIme')
    response.delete_cookie('ulogovanTip')
    response.delete_cookie('sessionid')
    return response

def vrati_na_pocetnu(request):
    """
    U zavisnosti od tipa korisnika (brucos, student, master, administrator ili neregistrovan korisnik), ucitava se odgovarajuca pocetna stranica.
    """
    if 'korisnickoIme' in request.COOKIES:
        korisnik = exists(request.COOKIES['korisnickoIme'])
        if korisnik.tip == 'B':
            return pocetna_brucos(request)
        if korisnik.tip == 'S':
            return pocetna_student(request)
        if korisnik.tip == 'M':
            return pocetna_master(request)
        if korisnik.tip == 'A':
            return pocetna_administrator(request)
    return pocetna(request)

# pocetne

def pocetna(request):
    """
    Prikazuje pocetnu stranicu.
    """
    response=render(request,'./pocetne/pocetna.html',{})
    #for cookie in request.COOKIES:
        #response.delete_cookie(cookie)
    sesskorime = request.session.get('korime', '')
    if (sesskorime!=''):
        korisnik = exists(sesskorime)
        return mainpage(korisnik, request)
    return response
    

def pocetna_brucos(request):
    """
    Korisnik je registrovan kao brucos - prikazuje se pocetna stranica.
    """
    korisnik = exists(request.COOKIES['korisnickoIme'])
    response=render(request,'./pocetne/pocetna_brucos.html',{'korisnik': korisnik})
    response.set_cookie('ulogovanTip', 'brucos', max_age=3600)  
    return response

def pocetna_administrator(request):
    """
    Korisnik je registrovan kao administrator - prikazuje se pocetna stranica.
    """
    korisnik = exists(request.COOKIES['korisnickoIme'])
    response=render(request,'./pocetne/pocetna_administrator.html',{'korisnik': korisnik})
    response.set_cookie('ulogovanTip', 'administrator', max_age=3600)  
    return response

def pocetna_master(request):
    """
    Korisnik je registrovan kao master - prikazuje se pocetna stranica.
    """
    korisnik = exists(request.COOKIES['korisnickoIme'])
    response= render(request,'./pocetne/pocetna_master.html',{'korisnik': korisnik})
    response.set_cookie('ulogovanTip', 'master', max_age=3600)  
    return response

def pocetna_student(request):
    """
    Korisnik je registrovan kao student - prikazuje se pocetna stranica.
    """
    korisnik = exists(request.COOKIES['korisnickoIme'])
    response= render(request,'./pocetne/pocetna_student.html',{'korisnik': korisnik})
    response.set_cookie('ulogovanTip', 'student', max_age=3600)  
    return response


# duel

def duel(request):
    """
    Obradjuje jednu rundu duela.
    U kolacicima cuva broj runde, do sada prikazane pesme u trenutnom duelu i trenutan broj poena.
    """

    ret = duel_runda(request)
    response = render(request,'./duel/duel.html',{'stihovi': ret['stihovi'], 
                    'zvuk': ret['zvuk'], 'crtice': ret['crtice'], 'runda': ret['runda'], 'poeni': ret['poeni']})
    response.set_cookie('runda', ret['runda'])
    response.set_cookie('poeni', ret['poeni'])
    return response


def generisi_sifru(request):
    """
    Generise novu sifru sobe.
    """
    sifra, stihovi = nova_soba(request)
    response = render(request,'./duel/generisana_sifra.html', {'sifra': sifra})
    response.set_cookie('soba', sifra)
    response.set_cookie('stihovi', stihovi)
    response.set_cookie('redni_broj', '1')
    return response


def proveri_sifru(request):
    """
    Proverava unetu sifru sobe i pokrece prvu rundu duela ako je ispravna, u suprotnom vraca odgovarajucu poruku.
    """
    provera, stihovi = provera_sobe(request)
    if provera:
        ret = duel_runda(request, stihovi)
        print("DUEL WEB")
        print(ret['stihovi'])
        response = render(request,'./duel/duel.html',{'stihovi': ret['stihovi'], 
                    'zvuk': ret['zvuk'], 'crtice': ret['crtice'], 'runda': ret['runda'], 'poeni': ret['poeni']})
        response.set_cookie('runda', ret['runda'])
        response.set_cookie('poeni', ret['poeni'])
        response.set_cookie('soba', request.POST.get('sifra'))
        response.set_cookie('stihovi', stihovi)
        response.set_cookie('redni_broj', '2')

        sifra_sobe = request.POST.get('sifra')
        
        try:
            soba = Soba.objects.get(pk=sifra_sobe)

            soba.poeni_2 = -1

            soba.save()
        except Soba.DoesNotExist:
            pass
        return response
    else:
        return render(request,'./duel/sifra_sobe.html',{'poruka': "Uneta šifra ne postoji!"})


def stigao_igrac(request):
    """
    Proverava da li je drugi igrac uneo generisanu sifru sobe i vraca tu informaciju kao json objekat.
    """
    sifra = int(request.COOKIES['soba'])
    return provera_dosao(sifra)


def cekanje_rezultata(request):
    """
    Nakon zavrsetka poslednje runde, upisuje rezultat u bazu.
    """
    postavi_cookie = obrada_rezultata(request)
    response = render(request,'./duel/cekanje_rezultata.html',{})
    if postavi_cookie:
        response.set_cookie('upisuj', '') # trenutni korisnik je drugi zavrsio duel
    return response


def zavrsio_igrac(request):
    """
    Proverava da li je drugi igrac zavrsio sve runde i vraca tu informaciju kao json objekat.
    """
    return provera_zavrsio(request)


def kraj_duela(request):
    """
    Obradjuje rezultate duela i azurira broj poena igraca nakon sto su oba zavrsila sve runde.
    """
    if('korisnickoIme') in request.COOKIES:
        ulogovan = True
    else:
        ulogovan = False

    rez = gotov_duel(request)
    response = render(request,'./duel/kraj_duela.html',{'poeni': rez['poeni'], 'poeni_runde': rez['poeni_runde'],
                                                        'igrac1': rez['igrac1'], 'igrac2': rez['igrac2'], 'ulogovan': ulogovan})
    response.delete_cookie('soba')
    response.delete_cookie('stihovi')
    response.delete_cookie('redni_broj')
    response.delete_cookie('runda')
    response.delete_cookie('poeni')
    if 'upisuj' in request.COOKIES:
        response.delete_cookie('upisuj')
    return response


def sifra_sobe(request):
    """
    Brise gerisanu sobu nakon sto igrac odustane od duela ili omogucava generisanje ili unos nove sifre.
    """
    obrisi_ako_postoji_soba(request)
    response = render(request,'./duel/sifra_sobe.html',{'poruka': ""})
    response.set_cookie('runda', 0)
    return response

# igra sam

def pravila_igre(request):
    """
    Prikazuje pravila igre.
    """
    if('korisnickoIme') in request.COOKIES:
        ulogovan = True
    else:
        ulogovan = False
    return render(request,'./profil_rang_pravila/pravila_igre.html',{'ulogovan': ulogovan})

def nivo(request):
    """Odabir tezine kada igrac igra sam sa sobom."""
    return render(request,'./igra_sam/nivo.html',{})

def zanr(request):
    """Odabir zanra kada igrac igra sa samim sobom."""
    zanrovi=Zanr.objects.all()
    response=render(request,'./igra_sam/zanr.html',{'zanrovi':zanrovi})
    response.delete_cookie('bilo')
    return response


def igra_sam(request):
    
    """Funkcija koja realizuje funkcionalnost kada igrac igra sam."""

    runda=request.COOKIES.get('runda_igra_sam')
    runda=int(runda)+1
    if(runda==8):
        kraj_igre(request)
    
    
    zanrovi=request.COOKIES.get('odabrani_zanrovi_igrasam')
    zanrovi=request.COOKIES.get('odabrani_zanrovi_igrasam')
    
    if(zanrovi=='[]'):
        zanrovii=Zanr.objects.all()
        response= render(request,'./igra_sam/zanr.html',{'zanrovi':zanrovii,'poruka':'Niste izabrali nijedan žanr'})
        return response
    tezina=request.COOKIES.get('odabrana_tezina_igra_sam')
    zanrovii=zanrovi[1:-1].split(',')
    novizanrovi= [element.strip().strip('"') for element in zanrovii]
    zanroviid=Zanr.objects.filter(naziv__in=novizanrovi)
    izvodjaci=Izvodjac.objects.filter(zan_id__in=zanroviid)
    print(izvodjaci)
    pesme=Pesma.objects.filter(izv_id__in=izvodjaci)
    print(pesme)
    stihovi=Stihovi.objects.filter(pes_id__in=pesme,nivo=tezina)
    stih=0
    
    niz=[]
    nizjs=[]
    
    if(not ('bilo' in request.COOKIES)):
        stih=random.choice(stihovi)
        niz.append(stih.id)
        nizjs=json.dumps(niz)
    else:
        while(True):
            stih=random.choice(stihovi)
            niz_json=request.COOKIES.get('bilo')
            #print(niz_json)
            niz=json.loads(niz_json)
            if(stih.id in niz):
                continue
            else:
                niz.append(stih.id)
                nizjs=json.dumps(niz)
                break

    pomoc1stih=Stihovi.objects.filter(id=stih.id)
    pomoc1stih2=pomoc1stih.values_list('pes_id', flat=True)
    pomoc1pesma=Pesma.objects.filter(id__in=pomoc1stih2)
    pomoc1pesma2=pomoc1pesma.values_list('izv_id',flat=True)

    pomoc1izvodjac=Izvodjac.objects.filter(id__in=pomoc1pesma2)
    izv=False
    for obj in pomoc1izvodjac:
        izv=obj.ime
        

    pomoc2stih=Stihovi.objects.filter(id=stih.id)
    pomoc2stih2=pomoc2stih.values_list('pes_id',flat=True)

    pomoc2pesma=Pesma.objects.filter(id__in=pomoc2stih2)
    pes=False
    for obj in pomoc2pesma:
        pes=obj.naziv
       

    s=stih.poznat_tekst.split("<br>")
   
    n=""
    for c in stih.nepoznat_tekst:
        if(c==' '):
            n+='  '
        elif(c=="'"):
            n+="'"
        else:
            n+="_&nbsp"

    tacno=""
    for c in stih.nepoznat_tekst:
        
        if(c=="'"):
            tacno+="&apos"
        else:
            tacno+=c
        
    zvuk = os.path.join('..', 'static', 'songs', stih.zvuk)
    response= render(request,'./igra_sam/igra_sam.html',{'stihpoznat':s,'crtice':n,'tacno':tacno,'izvodjac':izv,'zvuk':zvuk,'pesma':pes,'runda':str(runda-1)})
    response.set_cookie('bilo',nizjs)
    r=str(runda)
    response.set_cookie('runda_igra_sam',r)
        
    return response


def kraj_igre(request):
    """Funkcija koja se poziva kada igrac zavrsi igru sam sa sobom (ispisuje osvojen broj poena i dodaje u licne poene u bazi)."""
    if('korisnickoIme') in request.COOKIES:
        ulogovan = True
    else:
        ulogovan = False

    poeni=request.COOKIES.get('poeni_igra_sam')
   
    if('korisnickoIme' in request.COOKIES):
        ime=request.COOKIES.get('korisnickoIme')
        #print(ime)
        imezaazur=Korisnik.objects.get(korisnicko_ime=ime)
        novo=imezaazur.licni_poeni
        #print(imezaazur.licni_poeni)
        novo=novo+int(poeni)
        imezaazur.licni_poeni=novo

        if(novo>=100):
            imezaazur.tip='M'
        elif(novo>=50):
            imezaazur.tip='S'

        imezaazur.save()

        response= render(request,'./igra_sam/kraj_igre.html',{'poeni':poeni,'tip':imezaazur.tip, 'ulogovan': ulogovan})
        response.set_cookie('ima_pesama','')
        response.delete_cookie('bilo')
        return response
    
    return render(request,'./igra_sam/kraj_igre.html',{'poeni':poeni,'tip':'N', 'ulogovan': ulogovan})


# autorizacija

def exists(korime):
    """
        Pomocna funkcija koja promerava da li korisnik sa odgovarajucim imenom vec postoji u bazi.
    """
    korisnici = Korisnik.objects.all()
    for korisnik in korisnici:
        if(korisnik.korisnicko_ime==korime):
            return korisnik
    return None

def authorize(user, password, request):
    """
    Pomocna funkcija koja proverava da li se uneto korisnicko ime i lozinka poklapaju sa onima u bazi.
    """
    korisnik = exists(user)
    if korisnik is not None:
        if check_password(password, korisnik.sifra):
            return korisnik
        else:
            messages.error(request, 'Pogrešna loznika!')
    else:
        messages.error(request, 'Pogrešno korisničko ime!')
    return None

def mainpage(korisnik, request):
    """
        Pomocna funkcija koja otvara odgovarajucu pocetnu stranicu (administrator/brucos/student/master).
    """
    if (korisnik.tip == 'A'):
        response = render(request, './pocetne/pocetna_administrator.html', {'korisnik': korisnik})
    if (korisnik.tip == 'B'):
        response = render(request, './pocetne/pocetna_brucos.html', {'korisnik': korisnik})
    if (korisnik.tip == 'S'):
        response = render(request, './pocetne/pocetna_student.html', {'korisnik': korisnik})
    if (korisnik.tip == 'M'):
        response = render(request, './pocetne/pocetna_master.html', {'korisnik': korisnik})
    response.set_cookie('korisnickoIme', korisnik.korisnicko_ime, max_age=3600)
    return response

def login(request):
    """
        Loguje korisnika nakon unosa odgovarajuceg korisnickog imena i lozinke.
        Takodje mu nudi i opciju da se registruje ili oporavi svoju lozinku.
    """
    if request.method != 'POST':
        return render(request, './autorizacija/login.html', {})
    k=request.POST.get("korime")
    l=request.POST.get("loz")
    korisnik=authorize(k, l, request)
    if korisnik is not None:
        request.session['korime']=k
        response = mainpage(korisnik, request)
    else:
        response=render(request,'./autorizacija/login.html',{})
    return response

def forgotpass(request):
    """
        Korisnik unosi svoje korisnicko ime kako bi mogao da nastavi sa oporavljanjem lozinke.
    """
    k = request.POST.get("korime")
    korisnik = exists(k)
    if korisnik is not None:
        response = render(request, './autorizacija/forgotpassq.html', {'pitanje': korisnik.pitanje_lozinka})
        response.set_cookie('korisnickoIme', korisnik.korisnicko_ime, max_age=3600)
        return response
    else:
        response = render(request, './autorizacija/forgotpass.html', {})
        messages.error(request, 'Pogrešno korisničko ime!')
        response.set_cookie('korisnickoIme',None)
        return response

def correctUser(request):
    """
        Proverava da li je uneto korisnicko ime, za koje se oporavlja lozinka, postojece u bazi.
    """
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    k = request.POST.get("korime")
    korisnik = exists(k)
    if korisnik is not None:
        response = redirect('forgotpassq')
        response.set_cookie('korisnickoIme', korisnik.korisnicko_ime, max_age=3600)
        return response
    else:
        return forgotpass(request)
def forgotpassq(request):
    """
        Omogucava korisniku da odgovori na njegovo sigurnosno pitanje iz baze kako bi mogao da oporavi svoju lozinku.
    """
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    korime = request.COOKIES.get('korisnickoIme')
    korisnik = exists(korime)
    if request.method != 'POST':
        return render(request, './autorizacija/forgotpassq.html', {'pitanje': korisnik.pitanje_lozinka})
    if korisnik is not None:
        odg=request.POST.get("odgovor")
        if check_password(odg, korisnik.odgovor_lozinka):
            return redirect('newpass')
        else:
            messages.error(request, 'Netačan odgovor!')
    return render(request,'./autorizacija/forgotpassq.html',{'pitanje': korisnik.pitanje_lozinka})

def goodpass(lozinka):
    """
        Pomocna funkcija koja proverava da li lozinka koja je uneta ispunjava odredjene uslove.
    """
    if not (re.search(r'[a-zA-Z]', lozinka)):
        return 'Lozinka mora imati bar jedno slovo!'
    if not (re.search(r'\d', lozinka)):
        return 'Lozinka mora imati bar jedan broj!'
    if not len(lozinka) > 5:
        return 'Lozinka mora biti duza od 5 karaktera!'
    return None

def newpass(request):
    """
        Omogucava unosenje nove lozinke nakon autorizovanja korisnika pomocu sigurnosnog pitanja.
    """
    if request.method != 'POST':
        return render(request, './autorizacija/newpass.html', {})
    korime = request.COOKIES.get('korisnickoIme')
    l1 = request.POST.get("lozinka1")
    l2 = request.POST.get("lozinka2")
    if l1 == l2:
        mess=goodpass(l1)
        if mess is not None:
            messages.error(request, mess)
            return render(request, './autorizacija/newpass.html', {})
        korisnik = exists(korime)
        if korisnik is not None:
            korisnik.sifra = make_password(l1)
            korisnik.save()
            response = mainpage(korisnik, request)
            return response
    else:
        messages.error(request, 'Lozinke se ne poklapaju!')
        return render(request,'./autorizacija/newpass.html',{})

def registration(request):
    """
        Daje mogucnost novom korisniku da se registruje i pocne da sakuplja poene igranjem duela i samostalno.
    """
    if request.method != 'POST':
        return render(request, './autorizacija/registration.html', {})
    ime_prezime=request.POST.get("ime_prezime")
    ime, prezime = ime_prezime.split()
    kor_ime=request.POST.get("korime")
    lozinka=request.POST.get("lozinka")
    provera_lozinka=request.POST.get("plozinka")
    pitanje = request.POST.get("pitanje")
    odgovor = request.POST.get("odgovor")

    if(exists(kor_ime) is None):
        mess = goodpass(lozinka)
        if mess is None:
            if pitanje and len(pitanje) <= 255:
                if odgovor and len(odgovor) <= 255:
                    if(provera_lozinka == lozinka):
                        lozinka = make_password(lozinka)
                        odgovor = make_password(odgovor)
                        new_korisnik = Korisnik(
                            korisnicko_ime=kor_ime,
                            sifra=lozinka,
                            ime=ime,
                            prezime=prezime,
                            tip='B',
                            pitanje_lozinka=pitanje,
                            odgovor_lozinka=odgovor,
                            rang_poeni=0,
                            licni_poeni=0,
                            poslednja_aktivnost=timezone.now()
                        )
                        new_korisnik.save()
                        korisnik=exists(kor_ime)
                        response = render(request, './pocetne/pocetna_brucos.html', {'korisnik': korisnik})
                        response.set_cookie('korisnickoIme', korisnik.korisnicko_ime, max_age=3600)
                        return response
                    else:
                        mess='Lozinka i potvrda lozinke se ne poklapaju!'
                else:
                    mess='Odgovor je duži od 255 karaktera!'
            else:
                mess='Pitanje je duže od 255 karaktera!'
    else:
        mess='Korisnik sa tim imenom već postoji!'
    messages.error(request, mess)
    return render(request,'./autorizacija/registration.html',{})

def ranked(korisnicko_ime):
    """
        Pomocna funkcija koja izracunava rank (broj na listi) za poene iz duela za odgovarajuce korisnicko ime.
    """
    korisnici = Korisnik.objects.order_by('-rang_poeni')
    for index, korisnik in enumerate(korisnici, start=1):
        if(korisnik.korisnicko_ime == korisnicko_ime):
            return index

def pregled_profila(request):
    """
        Prikazuje sve dostupne informacije o ulogovanom korisniku.
    """
    korime = request.COOKIES.get('korisnickoIme')
    korisnik = Korisnik.objects.get(korisnicko_ime=korime)
    rank = ranked(korime)
    rank = '#'+str(rank)
    return render(request,'./profil_rang_pravila/pregled_profila.html',
                  {'korIme': korisnik.ime, 'korPrezime': korisnik.prezime, 'korisnIme': korime, 'korLicni': korisnik.licni_poeni, 'korRang': korisnik.rang_poeni, 'korRank': rank})

def rang_lista(request):
    """
        Prikazuje top 5 korisnika sa najvecim brojem poena sakupljenim u duelima.
    """
    korisnici = Korisnik.objects.order_by('-rang_poeni')[:5]
    ranks=[]
    for index, korisnik in enumerate(korisnici, start=1):
        ranks.append((index, korisnik.korisnicko_ime, korisnik.rang_poeni))
    return render(request,'./profil_rang_pravila/rang_lista.html',{'ranks': ranks})

# predlozi
def predlozi_izvodjaca(request):
    """
    Administrator prihvatata ili odbija predloge izvodjaca. 
    """
    if(Predlaze_Izvodjaca.objects.count()==0):
            return render(request,'./predlozi/predlozi_izvodjaca.html',{'message': "Nema novih predloga"})
    izvodjaci=Predlaze_Izvodjaca.objects.all().select_related('kor', 'zan')
    return render(request,'./predlozi/predlozi_izvodjaca.html',{'izvodjaci': izvodjaci})

def predlozi_pesama(request):
    """
    Administrator prihvatata ili odbija predloge pesama. 
    """
    if(Predlaze_Pesmu.objects.count()==0):
        return render(request,'./predlozi/predlozi_pesama.html',{'message': "Nema vise predloga"})
    pesme=Predlaze_Pesmu.objects.all().select_related("kor","izv", "izv__zan")
    return render(request,'./predlozi/predlozi_pesama.html',{'pesme':pesme})

def pesma_podaci(request):
    """
    Unos podataka o pesmi prilikom dodavanja. Ucitamo kolacic sa id-om zanra i id-om izvodjaca pre toga.
    """
    if(request.COOKIES.get("tipDodavanja")=="predlozi_izvodjaca"):
        return render(request,'./dodavanje/pesma_podaci.html',{})
    izvodjac=request.COOKIES.get("postavljenoImeIzvodjaca")
    try:
        Izvodjac.objects.get(ime=izvodjac)
        return render(request,'./dodavanje/ime_izvodjaca.html',{'message':"U bazi vec postoji izvodjac sa imenom: "+izvodjac})
    except:
        print("nema")
    return render(request,'./dodavanje/pesma_podaci.html',{})

def pesma_podaci1(request):
    return render(request,'./dodavanje/pesma_podaci1.html',{})

# predlaganje
def predlaganje_pesama(request):
    """
    Korisnici predlazu pesme. Dohvatanje izvodjaca i zanrova iz baze i prosledjivanje.
    """
    izvodjaci=Izvodjac.objects.all()
    zanrovi=Zanr.objects.all()
    return render(request,'./predlaganje/predlaganje_pesama.html',{'izvodjaci':izvodjaci,'zanrovi':zanrovi})

def predlaganje_izvodjaca(request):
    """
    Dohvatanje zanrova iz baze i prosledjivanje.
    """
    zanrovi=Zanr.objects.all()
    return render(request,'./predlaganje/predlaganje_izvodjaca.html',{'zanrovi':zanrovi})

def naziv_zanra(request):
    """
    Ucitava stranicu za unos naziva zanra.
    """
    return render(request,'./dodavanje/naziv_zanra.html',{})

def ime_izvodjaca(request):
    """
    Ucitava stranicu za unos imena izvodjaca i proverava unet naziv zanra.
    """
    zanr=request.COOKIES.get("postavljenZanr")
    try:
        Zanr.objects.get(naziv=zanr)
        return render(request,'./dodavanje/naziv_zanra.html',{'message':"U bazi vec postoji zanr sa nazivom: " +zanr})
    except: 
        return render(request,'./dodavanje/ime_izvodjaca.html',{})


def izbor_izvodjaca(request):
    """
    Izbor izvodjaca prilikom dodavanja. Ucitamo kolacic sa id-om zanra, a zatim prikazemo sve izvodjace tog zanra.
    """
    selected_genre = request.COOKIES.get('selectedGenre', None)
    if selected_genre:
        print("Vrednost kolacica selectedGenre:", selected_genre)
        izvodjaci=Izvodjac.objects.filter(zan_id=selected_genre)
        return render(request,'./dodavanje/izbor_izvodjaca.html',{'izvodjaci':izvodjaci})
    else:
        print("Kolacic selectedGenre nije postavljen.")
        return redirect('vrati_na_pocetnu')


def izbor_zanra1(request):
    """
    Izbor zanra (dodavanje iz baze) i prosledjivanje.
    """
    zanrovi=Zanr.objects.all()
    return render(request,'./dodavanje/izbor_zanra1.html',{'zanrovi':zanrovi})


def izbor_zanra2(request):
    """
    Izbor zanra (dodavanje iz baze) i prosledjivanje.
    """
    zanrovi=Zanr.objects.all()
    return render(request,'./dodavanje/izbor_zanra2.html',{'zanrovi':zanrovi})


def izbor_izvodjacaUklanjanje(request):
    """Odabir kom izvodjacu pripada pesma koju administrator zeli da obrise."""
    j=request.COOKIES.get('odabranzanrpesmazabrisanje')
    izvodjaci=Izvodjac.objects.all()

    if(j!='None'):
        izvodjaci=Izvodjac.objects.filter(zan_id=j)
       

    response = render(request,'./uklanjanje/izbor_izvodjaca.html',{'izvodjaci':izvodjaci})
    response.set_cookie('izvodjacbrisanje', None)
    return response
 


def uklanjanje_zanrova(request):
    """Uklanjanje zanra pored koga je kliknnuto dugme 'Ukloni'."""

    i=request.COOKIES.get('zanr')
    print(i)
    if(i!=None and i!='None'):
       
        zanr=Zanr.objects.filter(id=i)
        zanr.delete()
        print(i)
    zanrovi=Zanr.objects.all()
    response = render(request,'./uklanjanje/uklanjanje_zanrova.html',{'zanrovi':zanrovi})
    response.set_cookie('zanr', None)
    return response
    


def izbor_zanra1Uklanjanje(request):
    """Izbor zanra prilikom uklanjanja izvodjaca."""
    zanrovi=Zanr.objects.all()
    return render(request,'./uklanjanje/izbor_zanra1.html',{'zanrovi':zanrovi})


def izbor_zanra2Uklanjanje(request):
    """Izbor zanra prilikom uklanjanja pesama."""

    zanrovi=Zanr.objects.all()
    return render(request,'./uklanjanje/izbor_zanra2.html',{'zanrovi':zanrovi})

def uklanjanje_pesama(request):
    """Uklanja pesmu pored koje je kliknuto dugme 'Ukloni'."""

    j=request.COOKIES.get('odabranizvodjacpesmazabrisanje')
    i=request.COOKIES.get('pesmaidbrisanje')
    pesme=Pesma.objects.filter(izv_id=j)
    print(i)
    if(i!=None and i!='None'):
       
        pesma=Pesma.objects.filter(id=i)
        pesma.delete()
        print(i)
    response = render(request,'./uklanjanje/uklanjanje_pesama.html',{'pesme':pesme})
    response.set_cookie('pesmaidbrisanje',None)
    return response
   

def uklanjanje_korisnika(request):
    """Uklanja korisnika pored koga je kliknuto dugme 'Ukloni'."""

    i=request.COOKIES.get('id')
    print(i)
    if(i!=None and i!='None'):
       
        korisnik=Korisnik.objects.filter(id=i).exclude(tip='A')
        korisnik.delete()
        print(i)

    korisnici=Korisnik.objects.all().exclude(tip='A')
    response = render(request,'./uklanjanje/uklanjanje_korisnika.html',{'korisnici':korisnici})
    response.set_cookie('id', None)
    return response


def uklanjanje_izvodjaca(request):
    """Uklanja izvodjaca pored koga je kliknuto dugme 'Ukloni'."""

    i=request.COOKIES.get('izvodjacbrisanje')
    j=request.COOKIES.get('odabranzanrizvodjacazabrisanje')

    
    izvodjaci=Izvodjac.objects.all()

    if(j!='None'):
        izvodjaci=Izvodjac.objects.filter(zan_id=j)
       
    if(i!=None and i!='None'):
       
        izvodjac=Izvodjac.objects.filter(id=i)
        izvodjac.delete()

    response = render(request,'./uklanjanje/uklanjanje_izvodjaca.html',{'izvodjacibrisanje':izvodjaci})
    response.set_cookie('izvodjacbrisanje', None)
    return response
    