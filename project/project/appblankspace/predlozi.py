#Autor: Maša Nikolić 0439/2021

from django.conf import settings
from django.http import HttpResponse
from .models import Predlaze_Izvodjaca,Izvodjac,Predlaze_Pesmu,Zanr,Pesma,Stihovi,Korisnik

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
import os

def obrisi_podatak(request,id=None):
    """
    Administrator odbija predlog izvodjaca.
    Brisanje podataka iz baze sa odredjenim ID-om - tabela predlaze_izvodjaca.
    """
    if request.method == 'POST':
        Predlaze_Izvodjaca.objects.filter(id=id).delete()
    return redirect('predlozi_izvodjaca') 

def prihvati_predlog(request,id=None,zan_id=None,kor_id=None):
    """
    Administrator prihvata predlog izvodjaca.
    Preusmerava se na stranicu za dodavanje pesme.
    Brisanje podataka iz baze sa odredjenim ID-om - tabela predlaze_izvodjaca i dodavanje obrisanog podatka u tabelu Izvodjaci.
    """
    if request.method == 'POST':
        response = redirect('pesma_podaci')
        response.set_cookie("id_izvodjaca",id) 
        response.set_cookie('id_zanra', zan_id)
        response.set_cookie('id_korisnika', kor_id)
        response['Content-Type'] = 'text/plain; charset=utf-8'
        response.set_cookie("tipDodavanja","predlozi_izvodjaca")
        return response

def obrisi_podatak_pesme(request,id=None):
    """
    Administrator odbija predlog pesme.
    Brisanje podataka iz baze sa odredjenim ID-om - tabela Predlaze_Pesmu
    """
    if request.method == 'POST':
        Predlaze_Pesmu.objects.filter(id=id).delete()
        return redirect('predlozi_pesama')  
    return redirect('predlozi_pesama')  


def prihvati_predlog_pesme(request,id=None):
    """
    Brisanje podataka iz baze sa odredjenim ID-om - tabela Predlaze_Pesme i dodavanje obrisanog podatka u tabelu Izvodjaci.
    """
    if request.method == 'POST':
        return redirect('predlozi_pesama')  
    return redirect('predlozi_pesama')  


# predlaganje_izvodjaca - podfunkcije

def izvodjac_postoji(ime):
    """
    Provera da li se izvodjac pod datim imenom nalazi u tabeli izvodjac.
    """
    try:
        Izvodjac.objects.get(ime=ime)
        return True
    except Izvodjac.DoesNotExist:
        return False

def sacuvaj_predlog_izvodjaca(ime, korisnik_id, zanr_id):
    """
    Predlog izvodjaca upisuje u bazu sa prosledjenim vrednostima.
    """
    podatak = Predlaze_Izvodjaca(ime_izvodjaca=ime, kor_id=korisnik_id, zan_id=zanr_id)
    podatak.save()

def render_predlaganje_izvodjaca(request, message):
    """
    Ucitava stranicu predlaganje_izvodjaca.html sa odgovarajucom prosledjenom porukom message.
    """
    zanrovi = Zanr.objects.all()
    return render(request, './predlaganje/predlaganje_izvodjaca.html', {'zanrovi': zanrovi, 'message': message})

def korisnik_ima_previse_predloga(korisnik_id):
    """
    Proverava da li je korisnik dao maksimalan broj predloga. 
    Ako je korisnik dao 10 predloga koji još uvek nisu razrešeni - na stranici ce se prikazati 
    poruka o tome i dalji koraci ce biti onemogućeni. 
    """
    predlozi_korisnika = Predlaze_Izvodjaca.objects.filter(kor_id=korisnik_id)
    return predlozi_korisnika.count() > 9

def get_korisnik_id(korisnicko_ime):
    """
    Dohvata id korisnika iz tabele Korisnik po prosledjenom korisnickom imenu.
    """
    try:
        return Korisnik.objects.get(korisnicko_ime=korisnicko_ime).id
    except Korisnik.DoesNotExist:
        return None

def proveraNone(promenljiva):
    """
    Proverava da li je prosledjena promenljiva NULL.
    """
    if(promenljiva==None):
        return redirect('vrati_na_pocetnu')

# predlaganje_izvodjaca

def dodaj_predlog_izvodjaca(request,ime=None,zanr=None):
    """
    U bazu dodaje predlog izvodjaca sa ispravno prosledjenim vrednostima ili ispisuje odgovarajucu poruku u slucaju neuspeha.
    """
    proveraNone(ime)
    proveraNone(zanr)

    id_korisnik = get_korisnik_id(request.COOKIES.get('korisnickoIme'))
    if not id_korisnik:
        return redirect('vrati_na_pocetnu')

    if korisnik_ima_previse_predloga(id_korisnik):
        return render_predlaganje_izvodjaca(request, "Dostigli ste maksimalan broj predloga koji nisu razrešeni! Pokušajte ponovo kasnije.")

    if izvodjac_postoji(ime):
        return render_predlaganje_izvodjaca(request, f"U bazi vec postoji izvodjac sa imenom: {ime}")

    sacuvaj_predlog_izvodjaca(ime, id_korisnik, zanr)
    return redirect('vrati_na_pocetnu')

# predlaganje_pesama - podfunkcije

def get_or_create_izvodjac(ime, zanr, korisnik_id):
    """
    Ako izvodjac postoji u tabeli dohvata se id izvodjaca. 
    U suprotnom se poziva odgovarajuca metoda za kreiranje predloga izvodjaca.
    """
    try:
        return Izvodjac.objects.get(id=ime).id
    except Izvodjac.DoesNotExist:
        return create_izvodjac(ime, zanr, korisnik_id)

def create_izvodjac(ime, zanr, korisnik_id):
    """
    Dodaje se podatak u tabelu predlaze_izvodjaca ako postoji zanr sa datim id-om. 
    """
    try:
        id_zanr = Zanr.objects.get(id=zanr)
        predlog_izvodjaca = Predlaze_Izvodjaca(ime_izvodjaca=ime, kor_id=korisnik_id, zan_id=id_zanr.id)
        predlog_izvodjaca.save()
        return None  
    except Zanr.DoesNotExist:
        print("Error: Zanr not found")
        return None

def sacuvaj_predlog_pesme(pesma, izvodjac_id, korisnik_id):
    """
    Dodaje se podatak u tabelu predlaze_pesmu sa odgovarajucim prosledjenim vrednostima.
    """
    predlog_pesme = Predlaze_Pesmu(naziv_pesme=pesma, izv_id=izvodjac_id, kor_id=korisnik_id)
    predlog_pesme.save()

def render_predlaganje_pesama(request, message):
    """
    Ucitava stranicu predlaganje_pesama.html sa odgovarajucom prosledjenom porukom message.
    """
    zanrovi = Zanr.objects.all()
    izvodjaci=Izvodjac.objects.all()
    return render(request, './predlaganje/predlaganje_pesama.html', {'zanrovi': zanrovi, 'izvodjaci':izvodjaci,'messageBroj': message})

def korisnik_ima_previse_predloga_pesama(korisnik_id):
    """
    Proverava da li je korisnik dao maksimalan broj predloga. 
    Ako je korisnik dao 10 predloga koji još uvek nisu razrešeni - na stranici ce se prikazati 
    poruka o tome i dalji koraci ce biti onemogućeni. 
    """
    predlozi_pesama = Predlaze_Pesmu.objects.filter(kor_id=korisnik_id)
    return predlozi_pesama.count() > 9

def izvodjac_naziv_pesme_postoji(id_korisnik,pesma):
    """
    Provera da li se izvodjac pod datim imenom nalazi u tabeli izvodjac i da li postoji pesma sa datim nazivom i datim izvodjacem.
    """
    try:
        Pesma.objects.get(naziv=pesma,izv_id=id_korisnik)
        return True
    except Pesma.DoesNotExist:
        return False

# predlaganje_pesama
def dodaj_predlog_pesme(request,pesma=None,ime=None,zanr=None):
    """
    U bazu dodaje predlog pesme sa ispravno prosledjenim vrednostima ili ispisuje odgovarajucu poruku u slucaju neuspeha.
    """
    proveraNone(pesma);proveraNone(ime);proveraNone(zanr)

    id_korisnik = get_korisnik_id(request.COOKIES.get('korisnickoIme'))
    if id_korisnik is None:
        return redirect('vrati_na_pocetnu')

    if korisnik_ima_previse_predloga_pesama(id_korisnik):
        return render_predlaganje_pesama(request, "Dostigli ste maksimalan broj predloga koji nisu razrešeni! Pokušajte ponovo kasnije.")
    
    if izvodjac_naziv_pesme_postoji(ime,pesma):
        ime_izv=Izvodjac.objects.get(id=ime).ime
        return render_predlaganje_pesama(request, f"U bazi vec postoji pesma sa imenom: {pesma} datog izvodjaca {ime_izv}")

    id_izvodjac = get_or_create_izvodjac(ime, zanr, id_korisnik)
    if id_izvodjac is None:
        return redirect('vrati_na_pocetnu')

    sacuvaj_predlog_pesme(pesma, id_izvodjac, id_korisnik)
    return redirect('vrati_na_pocetnu')

def predlozi_pesama_kolacici(request,id=None,naziv=None,ime=None,zanr=None,korime=None):
    """
    Prosledjeni podaci se cuvaju u kolacicima. Administrator prihvata predlog pesme.
    Prelazi se na stranicu za dodavanje pesme
    """
    from urllib import parse
    response = redirect('pesma_podaci1')
    response.set_cookie("id_predlaze_pesmu",id) 
    response.set_cookie('naziv_pesme', parse.quote(naziv), max_age=3600)
    response.set_cookie('ime_izvodjaca', parse.quote(ime))
    response.set_cookie('zanr_pesme', zanr)
    response.set_cookie('korisnicko_ime', korime)
    response['Content-Type'] = 'text/plain; charset=utf-8'

    return response

def get_or_create_izv(ime, zanr):
    """
    Dohvata objekat iz tabele izvodjac na osnovu prosledjenog imena.
    U suprotnom kreira izvodjaca sa zadatim imenom.
    """
    try:
        izvodjac = Izvodjac.objects.get(ime=ime)
    except Izvodjac.DoesNotExist:
        izvodjac = Izvodjac(ime=ime, zan_id=zanr)
        izvodjac.save()
    return izvodjac


def get_or_create_pesma(naziv, izvodjac):
    """
    Dodavanje pesme sa prosledjenim podacima u tabelu pesma.
    """
    try:
        pesma = Pesma.objects.get(naziv=naziv)
    except Pesma.DoesNotExist:
        pesma = Pesma(naziv=naziv, izv_id=izvodjac.id)
        pesma.save()
    return pesma

def delete_predlog_pesme(id_predlaze_pesmu):
    """
    Brisanje podatka iz tabele predlaze_pesmu.
    """
    try:
        predlog = Predlaze_Pesmu.objects.get(id=id_predlaze_pesmu)
        predlog.delete()
    except Predlaze_Pesmu.DoesNotExist:
        print("error")

def pesma_podaci_dodavanje(request):
    """
    Administator je prihvatio predlog pesme.
    Dodajemo u bazu stihove, pesmu i izvodjaca (ako ne postoji)
    """
    if request.method=="POST":
        from urllib import parse

        naziv_pesme = parse.unquote(request.COOKIES.get('naziv_pesme'))
        ime_izvodjaca = parse.unquote(request.COOKIES.get('ime_izvodjaca'))
        zanr_pesme = request.COOKIES.get('zanr_pesme')
        korisnicko_ime = request.COOKIES.get('korisnicko_ime')
        id_predlaze_pesmu=request.COOKIES.get('id_predlaze_pesmu')

        izv=get_or_create_izv(ime_izvodjaca,zanr_pesme)
        pesm=get_or_create_pesma(naziv_pesme, izv)
        delete_predlog_pesme(id_predlaze_pesmu)
       
        poznati_stihovi=request.POST.get("stihovi1")
        poznati_stihovi=poznati_stihovi.replace(",", "<br>")
        nepoznati_stihovi=request.POST.get("stihovi2")
        nivo=request.POST.get("nivo")

        n=odredi_nivo(nivo)

        zvuk2 = request.FILES.get('fileInput')
        zvuk=zvuk2.name

        podaci=Stihovi(nivo=n,poznat_tekst=poznati_stihovi,nepoznat_tekst=nepoznati_stihovi,zvuk=zvuk,pes_id=pesm.id)
        podaci.save()

        #dodavanje u static
        sacuvaj_zvuk(zvuk2)

        response = redirect('pocetna_administrator') 
        response.delete_cookie('postavljenZanr', path='/') 
        response.delete_cookie('postavljenoImeIzvodjaca', path='/')
        response.delete_cookie('tipDodavanja', path='/')

    return response

# dodavanje pesme, izvodjaca, zanra - pomocne funkcije
def dodaj_izvodjaca(request):
    """
    Dodavanje izvodjaca u tabelu izvodjac.
    Dohavatanje odgovarajucih podataka iz kolacica koji su potrebni za dodavanje izvodjaca.
    Povratna vrednost je dodat id izvodjaca.
    """
    id_z = request.COOKIES.get('selectedGenre')
    ime_izvodjaca = request.COOKIES.get('postavljenoImeIzvodjaca')
    podatakIzvodjac = Izvodjac(ime=ime_izvodjaca, zan_id=id_z)
    podatakIzvodjac.save()
    return Izvodjac.objects.get(ime=ime_izvodjaca).id

def dodaj_zanr(request):
    """
    Dodavanje zanra u tabelu zanr.
    Dohavatanje odgovarajucih podataka iz kolacica koji su potrebni za dodavanje zanra.
    Povratna vrednost je dodat id zanra.
    """
    zanr = request.COOKIES.get('postavljenZanr')
    podatakZanr = Zanr(naziv=zanr)
    podatakZanr.save()
    id_z = Zanr.objects.get(naziv=zanr).id
    ime_izvodjaca = request.COOKIES.get('postavljenoImeIzvodjaca')
    podatakIzvodjac = Izvodjac(ime=ime_izvodjaca, zan_id=id_z)
    podatakIzvodjac.save()
    return Izvodjac.objects.get(ime=ime_izvodjaca).id

def sacuvaj_pesmu(naziv, izv_id):
    """
    Dodavanje pesme u tabelu pesma sa prosledjenim vrednostima.
    Povratna vrednost je dodat id pesme.
    """
    podatakPesma = Pesma(naziv=naziv, izv_id=izv_id)
    podatakPesma.save()
    return podatakPesma.id

def sacuvaj_stihove(nivo, poznati_stihovi, nepoznati_stihovi, zvuk, pes_id):
    """
    Dodavanje stihova u tabelu stihovi sa prosledjenim vrednostima.
    Povratna vrednost je dodat id stihova.
    """
    podaci = Stihovi(nivo=nivo, poznat_tekst=poznati_stihovi, nepoznat_tekst=nepoznati_stihovi, zvuk=zvuk, pes_id=pes_id)
    podaci.save()

def sacuvaj_zvuk(zvuk2):
    """
    Dodavanje .mp3 fajla u folder static/songs.
    """
    static_dir = os.path.join(settings.SONG_UPLOAD_DIR, 'songs')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    with open(os.path.join(static_dir, zvuk2.name), 'wb+') as destination:
        for chunk in zvuk2.chunks():
            destination.write(chunk)

def obrisi_kolacice(response):
    """
    Brisanje odgovarajucih kolacica.
    """
    response.delete_cookie('postavljenoImeIzvodjaca', path='/')
    response.delete_cookie('postavljenZanr', path='/')
    response.delete_cookie('tipDodavanja', path='/')
    response.delete_cookie('selectedIzvodjac', path='/')
    response.delete_cookie('selectedGenre', path='/')

def preuzmi_izvodjaca(id_izvodjaca):
    """
    Dohvata objekat iz tabele predlaze_izvodjaca pomocu id-a izvodjaca
    """
    try:
        return Predlaze_Izvodjaca.objects.get(id=id_izvodjaca)
    except Predlaze_Izvodjaca.DoesNotExist:
        return None
    
def sacuvaj_izvodjaca(ime_izvodjaca, id_zanra):
    """
    Dodavanje izvodjaca u  tabelu izvodjac.
    Povratna vrednost je id izvodjaca.
    """
    podatak = Izvodjac(ime=ime_izvodjaca, zan_id=id_zanra)
    podatak.save()
    return podatak.id

def obrisi_predlog_izvodjaca(id_izvodjaca):
    """
    Uklanjanje podatka iz tabele predlaze_izvodjaca na osnovu id izvodjaca.
    """
    Predlaze_Izvodjaca.objects.filter(id=id_izvodjaca).delete()

def odredi_nivo(nivo):
    """
    Odredjivanje nivo-a na osnovu prosledjenog podatka iz forme.
    """
    if nivo == "easy" or nivo=="E":
        return "E"
    elif nivo == "normal" or nivo=="N":
        return "N"
    else:
        return "H"

# dodaj_pesmu
def pesma_podaci_dodavanje_dodaj(request):
    """
    Dodavanje pesme u zavisnosti od tipa dodavanja (dodavanje zanra, izvodjaca ili samo pesme).
    Ili prihvatanje predloga izvodjaca (dodavanje pesme i izvodjaca).
    """
    if request.method=="POST":
        tipDodavanja=request.COOKIES.get("tipDodavanja")
        if(tipDodavanja=="predlozi_izvodjaca"):
            id_izvodjaca=request.COOKIES.get("id_izvodjaca") 
            id_zanra=request.COOKIES.get("id_zanra") 
            id_korisnika=request.COOKIES.get("id_korisnika") 

            izvodjac = preuzmi_izvodjaca(id_izvodjaca)
            if izvodjac is None:
                return redirect('predlozi_izvodjaca')
            
            imeI=izvodjac.ime_izvodjaca

            id_izv = sacuvaj_izvodjaca(imeI, id_zanra)
            obrisi_predlog_izvodjaca(id_izvodjaca)

            naziv_pesme=request.POST.get("naziv")
            id_pes = sacuvaj_pesmu(naziv_pesme, id_izv)
            
            poznati_stihovi=request.POST.get("stihovi1")
            poznati_stihovi=poznati_stihovi.replace(",", "<br>")
            nepoznati_stihovi=request.POST.get("stihovi2")
            nivo=request.POST.get("nivo")

            n = odredi_nivo(nivo)

            zvuk2 = request.FILES.get('fileInput')
            zvuk=zvuk2.name

            sacuvaj_stihove(n, poznati_stihovi, nepoznati_stihovi, zvuk, id_pes)
            sacuvaj_zvuk(zvuk2)

            response = redirect('pocetna_administrator') 
            obrisi_kolacice(response)
            return response
        
        naziv=request.POST.get("naziv")
        poznati_stihovi=request.POST.get("stihovi1")
        poznati_stihovi=poznati_stihovi.replace(",", "<br>")
        nepoznati_stihovi=request.POST.get("stihovi2")
        nivo=request.POST.get("nivo")
        zvuk2 = request.FILES.get('fileInput')
        zvuk=zvuk2.name

        if tipDodavanja == "DodajIzvodjaca":
            id = dodaj_izvodjaca(request)
        elif tipDodavanja == "DodajZanr":
            id = dodaj_zanr(request)
        else:
            id=request.COOKIES.get("selectedIzvodjac")

        id_pes = sacuvaj_pesmu(naziv, id)
        sacuvaj_stihove(nivo, poznati_stihovi, nepoznati_stihovi, zvuk, id_pes)
        sacuvaj_zvuk(zvuk2)
    
        response = redirect('pocetna_administrator')  
        obrisi_kolacice(response)
    return response

def pocetnaUlogovanTip(request):
    tip=request.COOKIES.get("ulogovanTip")
    if(tip=="master"):
        return redirect('pocetna_master')
    elif(tip=="student"):
        return redirect('pocetna_student')