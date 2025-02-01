# Autor: Jana Stanisavljević 0381/2021
import random
from django.http import HttpResponse
from .models import Stihovi, Soba, Korisnik, Pesma
import os
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


def duel_runda(request, stihovi_niz=None):
    """
    ucitava jenu rundu duela (vraca odgovarajuce stihove, broj runde, putanju do mp3 fajla itd.);
    stihovi_niz nisu None u slucaju da se ucitava prva runda za igraca koji je uneo sifru sobe (on nema u cookies izabrane stihove jos uvek)
    """
    if 'runda' in request.COOKIES:
        runda = int(request.COOKIES['runda']) + 1
    else:
        runda = 1
    
    if 'stihovi' in request.COOKIES:
        stihovi_niz = json.loads(request.COOKIES['stihovi'])
    else:
        stihovi_niz = json.loads(stihovi_niz)
    print(stihovi_niz)
    
    stihovi_id = stihovi_niz[runda - 1]
    stihovi = Stihovi.objects.get(pk=stihovi_id)

    if runda != 1:
        poeni = request.COOKIES['poeni']
    else:
        poeni = 0
    
    zvuk = os.path.join('..', 'static', 'songs', stihovi.zvuk)

    crtice = ""
    for znak in stihovi.nepoznat_tekst:
        if znak != " ":
            crtice += "_ "
        else:
            crtice += "&nbsp;"
    
    ret = {
        'stihovi': stihovi,
        'zvuk': zvuk,
        'crtice': crtice,
        'runda': runda,
        'poeni': poeni
    }
    return ret


def nova_soba(request):
    """
    generise novu sobu i vraca njen identifikator;
    nasumicno bira 7 pesama za duel, upisuje ih u bazu i vraca ih;
    """
    if 'korisnickoIme' in request.COOKIES:
        korisnik = exists(request.COOKIES.get("korisnickoIme"))

    svi_stihovi_ids = list(Stihovi.objects.values_list('id', flat=True))
    random.shuffle(svi_stihovi_ids)
    id_stihovi = svi_stihovi_ids[:7]

    if 'korisnickoIme' in request.COOKIES:
        soba = Soba(kor_1=korisnik, stihovi=json.dumps(id_stihovi),poeni_1=-1)
    else:
        soba = Soba(stihovi=json.dumps(id_stihovi), poeni_1=-1)
    soba.save()

    return soba.id, soba.stihovi


def provera_sobe(request):
    """
    proverava da li postoji soba sa datom sifrom;
    upisuje drugog korisnika u datu sobu;
    takodje vraca izabrane stihove za taj duel;
    """
    sifra = request.POST.get('sifra')
    try:
        soba = Soba.objects.get(pk=sifra)
        if 'korisnickoIme' in request.COOKIES:
            soba.kor_2 = exists(request.COOKIES.get("korisnickoIme"))

        soba.poeni_2 = -1 # da bi se znalo da je dosao
        soba.save()
        return True, soba.stihovi
    except Soba.DoesNotExist:
        return False, None
    

def provera_dosao(sifra):
    """
    proverava da li je drugi igrac uneo generisanu sifru sobe i vraca tu informaciju kao json objekat;
    """
    soba = Soba.objects.get(pk=sifra)
    if soba.poeni_2 == -1:
        return JsonResponse({'dosao': True})
    else:
        return JsonResponse({'dosao': False})
    

def provera_zavrsio(request):
    """
    proverava da li je drugi igrac zavrsio sve runde i vraca tu informaciju kao json objekat;
    """
    poeni = int(request.COOKIES['poeni'])
    soba_id = int(request.COOKIES['soba'])
    soba = Soba.objects.get(pk=soba_id)
    if request.COOKIES['redni_broj'] == '1':
        if(soba.poeni_2 == -1):
            return JsonResponse({'dosao': False})
        else:
            return JsonResponse({'dosao': True})

    else:
        if(soba.poeni_1 == -1):
            return JsonResponse({'dosao': False})
        else:
            return JsonResponse({'dosao': True})
    

def obrada_rezultata(request):
    """
    upisuje rezultat duela za jednog igraca u bazu, u tabelu Soba;
    """
    poeni_runde = []
    for i in range(1, 8):
        poeni_runde.append(int(request.COOKIES['runda' + str(i)]))
    poeni = int(request.COOKIES['poeni'])
    soba_id = int(request.COOKIES['soba'])
    soba = Soba.objects.get(pk=soba_id)
    if request.COOKIES['redni_broj'] == '1':
        soba.poeni_1 = poeni
        soba.poeni_runde_1 = json.dumps(poeni_runde)
        soba.save()
        if soba.poeni_2 == -1: # drugi igrac je zaduzen za upisivanje konacnih rezultata u bazu
            return False
        return True

    else:
        soba.poeni_2 = poeni
        soba.poeni_runde_2 = json.dumps(poeni_runde)
        soba.save()
        if soba.poeni_1 == -1: # drugi igrac je zaduzen za upisivanje konacnih rezultata u bazu
            return False
        return True

    


def gotov_duel(request):
    """
    vraca rezultate duela nakon sto oba igraca zavrse;
    azurira broj licnih i rang poena za oba igraca;
    """
    soba_id = int(request.COOKIES['soba'])
    soba = Soba.objects.get(pk=soba_id)
    poeni_runde = []
    pr1 = json.loads(soba.poeni_runde_1)
    pr2 = json.loads(soba.poeni_runde_2)
    for i in range(len(pr1)):
        poeni_runde.append([pr1[i], pr2[i]])
    poeni = []
    poeni.append(soba.poeni_1)
    poeni.append(soba.poeni_2)

    igrac1 = "gost"
    igrac2 = "gost"

    if 'upisuj' in request.COOKIES: # da bi se samo jednom odradilo, igrac koji je drugi zavrsio upisuje
        if soba.poeni_1 > soba.poeni_2:
            if soba.kor_1 != None:
                soba.kor_1.rang_poeni += soba.poeni_1 - soba.poeni_2
            if soba.kor_2 != None:
                soba.kor_2.rang_poeni -= soba.poeni_1 - soba.poeni_2
        elif soba.poeni_1 < soba.poeni_2:
            if soba.kor_1 != None:
                soba.kor_1.rang_poeni -= soba.poeni_2 - soba.poeni_1
            if soba.kor_2 != None:
                soba.kor_2.rang_poeni += soba.poeni_2 - soba.poeni_1
        if soba.kor_1 != None:
            soba.kor_1.licni_poeni += soba.poeni_1
            if(soba.kor_1.licni_poeni >= 50):
                soba.kor_1.tip = 'S'
            if(soba.kor_1.licni_poeni >= 100):
                soba.kor_1.tip = 'M'
            soba.kor_1.save()
            igrac1 = soba.kor_1.korisnicko_ime
        if soba.kor_2 != None:
            soba.kor_2.licni_poeni += soba.poeni_2
            if(soba.kor_2.licni_poeni >= 50):
                soba.kor_2.tip = 'S'
            if(soba.kor_2.licni_poeni >= 100):
                soba.kor_2.tip = 'M'
            soba.kor_2.save()
            igrac2 = soba.kor_2.korisnicko_ime
    
    if soba.kor_1 != None:
        igrac1 = soba.kor_1.korisnicko_ime
    if soba.kor_2 != None:
        igrac2 = soba.kor_2.korisnicko_ime

    rezultat = {
        'poeni_runde': poeni_runde,
        'poeni': poeni,
        'igrac1': igrac1,
        'igrac2': igrac2,
    }
    return rezultat


def obrisi_ako_postoji_soba(request):
    """
    brise gerisanu sobu nakon sto igrac odustane od duela;
    """
    if 'soba' in request.COOKIES:
        soba = Soba.objects.get(pk=request.COOKIES['soba'])
        soba.delete()


def exists(korime):
    return Korisnik.objects.get(korisnicko_ime=korime)
    