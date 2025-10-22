# Autor: Maša Nikolić 0439/2021

# viewsM.py
import os
import re
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from appblankspace.duel import duel_runda, gotov_duel, nova_soba, obrada_rezultata, obrisi_ako_postoji_soba, provera_dosao, provera_sobe, provera_zavrsio
from project import settings

from .models import *
from .serializers import *

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import random
from .models import Zanr, Izvodjac, Pesma, Stihovi
from rest_framework.response import Response
from rest_framework import status
import random

class ZanrList(APIView):
    """ANDROID: Odabir zanra kada igrac igra sa samim sobom."""
    def get(self, request):
        zanrovi = Zanr.objects.all()  # Dohvatanje svih žanrova iz baze
        serializer = ZanrSerializer(zanrovi, many=True)
        return Response(serializer.data)

class IzvodjaciList(APIView):
    """ANDROID: Dohvatanje svih izvodjaca."""
    def get(self, request):
        izvodjaci=Izvodjac.objects.all() # Dohvatanje svih izvodjaca iz baze
        serializer = IzvodjacSerializer(izvodjaci, many=True)
        return Response(serializer.data)


class IgraSamAPIView(APIView):
    """ANDROID: Funkcija koja realizuje funkcionalnost kada igrac igra sam."""

    def post(self, request, *args, **kwargs):
        zanrovi = request.data.get('zanrovi', '')
        tezina = request.data.get('tezina', '')
        runda = request.data.get('runda','')
        poeni = request.data.get('poeni','')
        listaBilo=request.data.get('listaBilo','')
        if not zanrovi:
            return Response({'error': 'Niste izabrali nijedan žanr'}, status=status.HTTP_400_BAD_REQUEST)

        if not tezina:
            return Response({'error': 'Niste izabrali nivo'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            izvodjaci = Izvodjac.objects.filter(zan_id__in=zanrovi)
            for e in izvodjaci:
                print(e.ime)
        except:
            print("EXCEPTION")


        izvodjaci = Izvodjac.objects.filter(zan_id__in=zanrovi)
        pesme = Pesma.objects.filter(izv_id__in=izvodjaci)
        try:
            tezina = tezina.replace("[", "").replace("]", "")
        except:
            print("Exception")
        if(tezina=="easy"):
            stihovi = Stihovi.objects.filter(pes_id__in=pesme, nivo="E")
        elif(tezina=="normal"):
            stihovi = Stihovi.objects.filter(pes_id__in=pesme, nivo="N")
        else:
            stihovi = Stihovi.objects.filter(pes_id__in=pesme, nivo="H")

        if not stihovi:
            return Response({'error': 'Nema stihova koji odgovaraju izabranim žanrovima i nivou'}, status=status.HTTP_404_NOT_FOUND)

        # Biranje nasumičnog stiha
        stih = random.choice(stihovi)
        while(stih.pk in listaBilo):
            stih = random.choice(stihovi)
        listaBilo.append(stih.pk)

        niz = []
        nizjs = json.dumps(niz)
        izv=""
        pes=""
        
        try:
            pomoc1stih=Stihovi.objects.filter(id=stih.pk)
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
            zvuk = os.path.join('..', 'static', 'songs', stih.zvuk)
        except:
             print("An exception occurred")
    
        n=""
        for c in stih.nepoznat_tekst:
            if(c==' '):
                n+='  '
            elif(c=="'"):
                n+="'"
            else:
                n+="_ "

        
        print(runda)
        print(listaBilo)

        response_data = {
            'stihpoznat': stih.poznat_tekst.split("<br>"),
            'crtice': n,
            'tacno': stih.nepoznat_tekst,
            'izvodjac': izv,
            'zvuk': stih.zvuk,  
            'pesma': pes,
            'runda': runda+1,  # Početna runda,
            'poeni':poeni,
            'listaBilo':listaBilo
        }

        response_data['bilo'] = nizjs
        response_data['runda_igra_sam'] = 1  # Prva runda

        return Response(response_data, status=status.HTTP_200_OK)

class KrajIgre(APIView):
    def post(self,request,*args,**kwargs):
        """
        ANDROID:
        Funkcija koja se poziva kada igrac zavrsi igru sam sa sobom (ispisuje osvojen broj poena i dodaje u licne poene u bazi).
        """
        korisnickoIme=request.data.get('korisnickoIme','')
        if korisnickoIme is not None:
            ulogovan = True
        else:
            ulogovan = False

        poeni=request.data.get('poeni_igra_sam','')
    
        if korisnickoIme is not None:
            ime=korisnickoIme
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

            response_data = {
                'poeni': poeni,
                'tip': imezaazur.tip,
                'ulogovan': ulogovan
            }   
            return Response(response_data, status=200)

        response_data = {
            'poeni': poeni,
            'tip': 'N',
            'ulogovan': ulogovan
        }   
        return Response(response_data, status=200)
        

class RangLista(APIView):
    """ANDROID: Prikazuje top 5 korisnika sa najvecim brojem poena sakupljenim u duelima."""
    def get(self, request):
        korisnici = Korisnik.objects.order_by('-rang_poeni')[:5]
        serializer = RangListaSerializer(korisnici, many=True)
        data = serializer.data
        for index, item in enumerate(data, start=1):
            item['index'] = index  # Add the rank index
        
        return Response(data)

class MojProfil(APIView):
    """ANDROID: Prikazuje sve dostupne informacije o ulogovanom korisniku (android uređaji)."""

    def post(self, request, *args, **kwargs):
        korisnicko_ime = request.data.get('korisnicko_ime', '')
        
        try:
            korisnik = Korisnik.objects.get(korisnicko_ime=korisnicko_ime)
        except Korisnik.DoesNotExist:
            return Response({'error': 'Korisnik nije pronađen'}, status=404)

        serializer = MojProfilSerializer(korisnik) 
        data = serializer.data
        rank = ''
        
        # Get the rank by ordering by 'rang_poeni'
        korisnici = Korisnik.objects.order_by('-rang_poeni')
        for index, korisnik in enumerate(korisnici, start=1):
            if korisnik.korisnicko_ime == korisnicko_ime:
                rank = '#' + str(index)
                break 

        data['rank'] = rank        
        return Response(data)

class SongsApi(APIView):
    def post(self, request, *args, **kwargs):
        # Pretpostavljamo da od korisnika dobijamo naziv fajla (npr. 'song1.mp3')
        url =request.data.get('url','')
        # Vraćanje URL-a za preuzimanje fajla
        mp3_url = f"{settings.MOBILE_LINK}/static/songs/{url}"
        print(mp3_url)
        return Response({"audio_url": mp3_url}, status=status.HTTP_200_OK)
    

from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
    
class LoginApi(APIView):

    def exists(korime):
        korisnici = Korisnik.objects.all()
        for korisnik in korisnici:
            if(korisnik.korisnicko_ime==korime):
                return korisnik
        return None
    
    def authorize(user, password, request):
        
        korisnik = LoginApi.exists(user)
        if korisnik is not None:
            if check_password(password, korisnik.sifra):
                return korisnik
            else:
                print('Pogrešna loznika!')
        else:
            print('Pogrešno korisničko ime!')
        return None
    
    
    def post(self, request, *args, **kwargs):
        k=request.data.get('username','')
        l =request.data.get('password','')   

        if(k=="" and l==""):
            return Response({
                'acces':"",
                'refresh':"",
                'ime':"",
                'korisnicko_ime': "", 
                'tip': "", "odgovor": "Logout!"}
            , status=200)    
        
        #korisnik=LoginApi.authorize(k, l, request)

        korisnik = LoginApi.exists(k)
        if korisnik is not None:
            if check_password(l, korisnik.sifra)==False:
                return Response({
                'acces':"",
                'refresh':"",
                'ime':"",
                'korisnicko_ime': "", 
                'tip': "", "odgovor": "Pogrešna loznika!"}
            , status=200)

        if korisnik is not None:
            refresh = RefreshToken.for_user(korisnik)
            access_token = str(refresh.access_token)
            serializer = KorisnikSerializer(korisnik)  # No many=True
            data = serializer.data
            data['access'] = access_token
            data['refresh'] = str(refresh)
            data['odgovor']=""
            print(data)
            return Response(data)
        else:
            return Response({
                'acces':"",
                'refresh':"",
                'ime':"",
                'korisnicko_ime': "", 
                'tip': "", "odgovor": "Pogrešno korisničko ime!"}
            , status=200)
    

class PredlaganjePesmeApi(APIView):
    def post(self,request, *args, **kwargs):
        pesma = request.data.get('pesma','')
        izvodjac=request.data.get('izvodjac','')
        zanr =request.data.get('zanr','')
        korisnicko_ime =request.data.get('korisnicko_ime','')
        print(izvodjac)
        print(zanr)
        print(korisnicko_ime)

        
        id_izv=PredlaganjePesmeApi.izvodjac_postoji_pk(izvodjac)
        print(id_izv)
        b=PredlaganjePesmeApi.pesma_postoji(pesma,id_izv)
        if(b):
            return Response({"odgovor": "U bazi vec postoji pesma sa imenom: "+pesma+
                             "datog izvodjaca "+izvodjac}, status=200)
        
        k=Korisnik.objects.get(korisnicko_ime=korisnicko_ime)
        #z=Zanr.objects.get(zanr=zanr)
        PredlaganjePesmeApi.sacuvaj_predlog_pesme(pesma,id_izv,k.pk)
        
        return Response({"odgovor": "Uspesno dodat predlog"}, status=200)
    
    def izvodjac_postoji_pk(ime):
        try:
            izv_id= Izvodjac.objects.get(ime=ime)
            return izv_id.id
        except Izvodjac.DoesNotExist:
            return -1
    
    def pesma_postoji(pesma,id_izv):
        try:
            Pesma.objects.get(naziv=pesma,izv_id=id_izv)
            return True
        except Pesma.DoesNotExist:
            return False

    def sacuvaj_predlog_pesme(pesma, id_izv, korisnik_id):
        """
        Predlog pesme upisuje u bazu sa prosledjenim vrednostima.
        """
        podatak = Predlaze_Pesmu(naziv_pesme=pesma,izv_id=id_izv, kor_id=korisnik_id)
        podatak.save()


class PredlaganjeIzvodjacaApi(APIView):
    def post(self,request, *args, **kwargs):
        izvodjac=request.data.get('izvodjac','')
        zanr =request.data.get('zanr','')
        korisnicko_ime =request.data.get('korisnicko_ime','')
        print(izvodjac)
        print(zanr)
        print(korisnicko_ime)

        
        b=PredlaganjeIzvodjacaApi.izvodjac_postoji(izvodjac)
        if(b):
            return Response({"odgovor": "U bazi vec postoji izvodjac sa imenom: "+izvodjac}, status=200)
        
        k=Korisnik.objects.get(korisnicko_ime=korisnicko_ime)
        #z=Zanr.objects.get(zanr=zanr)
        PredlaganjeIzvodjacaApi.sacuvaj_predlog_izvodjaca(izvodjac,k.pk,zanr)
        
        return Response({"odgovor": "Uspesno dodat predlog"}, status=200)
    
    def izvodjac_postoji(ime):
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


class UklanjanjeZanrIzvodjaca(APIView):
    def post(self,request, *args, **kwargs):
        zanr=request.data.get('id','')
        izvodjaci=Izvodjac.objects.all()

        if(zanr!='None'):
            izvodjaci=Izvodjac.objects.filter(zan_id=zanr)

        serializer = IzvodjacSerializer(izvodjaci, many=True)
        return Response(serializer.data)
    
class UklanjanjePesmeIzvodjaca(APIView):
    def post(self,request, *args, **kwargs):
        izv=request.data.get('id','')
        pesme=Pesma.objects.all()

        if(izv!='None'):
            pesme=Pesma.objects.filter(izv_id=izv)

        serializer = PesmeSerializer(pesme, many=True)
        return Response(serializer.data)
        
class UklanjanjeKorisnika(APIView):
    def get(self, request):
        korisnici = Korisnik.objects.all()
        serializer = KorisnikUklanjanjeSerializer(korisnici, many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        print("ovde")
        korisnicko_ime=request.data.get('korisnicko_ime','')
        korisnik=Korisnik.objects.filter(korisnicko_ime=korisnicko_ime).exclude(tip='A')
        if korisnik is None:
            return Response({"odgovor":"Greska!"},status=200)
        korisnik.delete()
        return Response({"odgovor":"Uspesno uklonjen korisnik!"},status=200)

        
class UklanjanjeZanraAPI(APIView):
    """
    ANDROID:
    Uklanjanje zanra pored koga je kliknnuto dugme 'Ukloni'.
    """
    def post(self,request,*args,**kwargs):
        print("ovde")
        zanr_id=request.data.get('zanr','')
        zanr=Zanr.objects.filter(id=zanr_id)
        if zanr is None:
            return Response({"odgovor":"Greska!"},status=200)
        zanr.delete()
        return Response({"odgovor":"Uspesno uklonjen zanr!"},status=200)
    
class UklanjanjeIzvodjacaAPI(APIView):
    """
    ANDROID:
    Uklanjanje izvodjaca pored koga je kliknnuto dugme 'Ukloni'.
    """
    def post(self,request,*args,**kwargs):
        izv_id=request.data.get('izvodjac','')
        izvodjac=Izvodjac.objects.filter(id=izv_id)
        if izvodjac is None:
            return Response({"odgovor":"Greska!"},status=200)
        izvodjac.delete()
        return Response({"odgovor":"Uspesno uklonjen izvodjac!"},status=200)

class UklanjanjePesmeAPI(APIView):
    """
    ANDROID:
    Uklanjanje pesme pored koga je kliknnuto dugme 'Ukloni'.
    """
    def post(self,request,*args,**kwargs):
        pesma_id=request.data.get('pesma','')
        pesma=Pesma.objects.filter(id=pesma_id)
        if pesma is None:
            return Response({"odgovor":"Greska!"},status=200)
        pesma.delete()
        return Response({"odgovor":"Uspesno uklonjena pesma!"},status=200)
    
class ProveraPostojanja(APIView):
    def post(self,request,*args,**kwargs):
        vrednost=request.data.get('vrednost','')
        tip=request.data.get('tip','')
        if(tip=='zanr'):
            try:
                zanr = Zanr.objects.get(naziv=vrednost.lower())
                return Response({"odgovor": f"U bazi vec postoji zanr sa nazivom: {vrednost}"}, status=200)
            except Zanr.DoesNotExist:
                return Response({"odgovor": "Uspeh"}, status=200)
        elif(tip=='izvodjac'):
            try:
                izv=Izvodjac.objects.get(ime=vrednost.lower())
                return Response({"odgovor": f"U bazi vec postoji izvodjac sa imenom: {vrednost}"}, status=200)
            except Izvodjac.DoesNotExist:
                return Response({"odgovor": "Uspeh"}, status=200)
            
class DodajZanrAPI(APIView):
    def post(self,request,*args,**kwargs):
        
        try:
            # 1. Dohvatanje podataka iz zahteva
            naziv_pesme = request.data.get('naziv_pesme')
            ime_izvodjaca = request.data.get('izvodjac')
            zanr_pesme = request.data.get('zanr')
            poznati_stihovi = request.data.get('nepoznati_stihovi', '').replace(',', '<br>')
            nepoznati_stihovi = request.data.get('poznati_stihovi')
            nivo = request.data.get('nivo')

            zvuk_file = request.FILES.get('audio')  # multipart/form-data ključ (isti kao u Retrofit-u)
            
            if not all([naziv_pesme, ime_izvodjaca, zanr_pesme, poznati_stihovi, nepoznati_stihovi, nivo, zvuk_file]):
                return Response({"odgovor": "Nisu svi podaci prosleđeni."},status=200)

            # 2. Upis u bazu

            #provera da li postoji zanr
        
            podatakZanr =Zanr.objects.filter(naziv=zanr_pesme).first()
            if podatakZanr ==None:
                podatakZanr = Zanr(naziv=zanr_pesme)
                podatakZanr.save()
    
            #podatakZanr = Zanr(naziv=zanr_pesme)
            #podatakZanr.save()

            id_z = Zanr.objects.get(naziv=zanr_pesme).id

            #provera da li postoji izvodjac
            podatakIzvodjac = Izvodjac.objects.filter(ime=ime_izvodjaca, zan_id=id_z).first()
            if podatakIzvodjac is None:
                podatakIzvodjac = Izvodjac(ime=ime_izvodjaca, zan_id=id_z)
                podatakIzvodjac.save()

            #podatakIzvodjac = Izvodjac(ime=ime_izvodjaca, zan_id=id_z)
            #podatakIzvodjac.save()
            id_i = Izvodjac.objects.get(ime=ime_izvodjaca).id

            podatakPesma = Pesma(naziv=naziv_pesme, izv_id=id_i)
            podatakPesma.save()
            id_p = Pesma.objects.get(naziv=naziv_pesme).id
            
            n = DodajZanrAPI.odredi_nivo(nivo)
            
            stih = Stihovi(
                nivo=n,
                poznat_tekst=poznati_stihovi,
                nepoznat_tekst=nepoznati_stihovi,
                zvuk=zvuk_file.name,
                pes_id=id_p
            )
            stih.save()
            # 3. Snimi fajl na disk (kao u `sacuvaj_zvuk`)
            DodajZanrAPI.sacuvaj_zvuk(zvuk_file)
            print("Dodaj zanr uspesno dodato.")

            return Response({"odgovor": "Pesma uspešno dodata."}, status=201)

        except Exception as e:
            return Response({"odgovor": str(e)}, status=500)
    
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


    def sacuvaj_zvuk(zvuk2):
        static_dir = os.path.join(settings.SONG_UPLOAD_DIR, 'songs')
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        with open(os.path.join(static_dir, zvuk2.name), 'wb+') as destination:
            for chunk in zvuk2.chunks():
                destination.write(chunk)

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

class IzvodjaciZanr(APIView):
    def post(self,request, *args, **kwargs):
        zanr = request.data.get('zanr','')
        z=Zanr.objects.get(naziv = zanr)
        izvodjaci = Izvodjac.objects.filter(zan=z) 
        serializer = IzvodjacSerializer(izvodjaci, many=True)
        print(serializer.data)
        return Response(serializer.data)

class Registracija(APIView):
    def post(self,request, *args, **kwargs):
        
        ime_i_prezime = request.data.get('ime_i_prezime','')
        korisnicko_ime = request.data.get('korisnicko_ime','')
        lozinka = request.data.get('lozinka','')
        potvrda_lozinke = request.data.get('potvrda_lozinke','')
        pitanje = request.data.get('pitanje','')
        odgovor = request.data.get('odgovor','')
        print(ime_i_prezime)
        print(korisnicko_ime)
        print(lozinka)
        print(potvrda_lozinke)
        print(pitanje)
        print(odgovor)

        ime, prezime = ime_i_prezime.split()

        if(Registracija.exists(korisnicko_ime) is None):
            mess = Registracija.goodpass(lozinka)
            if mess is None:
                if pitanje and len(pitanje) <= 255:
                    if odgovor and len(odgovor) <= 255:
                        if(potvrda_lozinke == lozinka):
                            lozinka = make_password(lozinka)
                            odgovor = make_password(odgovor)
                            new_korisnik = Korisnik(
                                korisnicko_ime=korisnicko_ime,
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
                            korisnik=Registracija.exists(korisnicko_ime)

                            refresh = RefreshToken.for_user(korisnik)
                            access_token = str(refresh.access_token)
                            serializer = KorisnikSerializer(korisnik)  # No many=True
                            data = serializer.data
                            data['access'] = access_token
                            data['refresh'] = str(refresh)
                            data['odgovor']=""
                            print(data)
                            return Response(data)
                        else:
                            mess='Lozinka i potvrda lozinke se ne poklapaju!'
                    else:
                        mess='Odgovor je duži od 255 karaktera!'
                else:
                    mess='Pitanje je duže od 255 karaktera!'
        else:
            mess='Korisnik sa tim imenom već postoji!'
        print(mess )
        return Response({
                'acces':"",
                'refresh':"",
                'ime':"",
                'korisnicko_ime': "", 
                'tip': "", "odgovor": mess}
            , status=200)
    
    def exists(korime):
        korisnici = Korisnik.objects.all()
        for korisnik in korisnici:
            if(korisnik.korisnicko_ime==korime):
                return korisnik
        return None
    
    def goodpass(lozinka):
        if not (re.search(r'[a-zA-Z]', lozinka)):
            return 'Lozinka mora imati bar jedno slovo!'
        if not (re.search(r'\d', lozinka)):
            return 'Lozinka mora imati bar jedan broj!'
        if not len(lozinka) > 5:
            return 'Lozinka mora biti duza od 5 karaktera!'
        return None
    
class ZaboravljenaLozinka(APIView):
    def post(self,request, *args, **kwargs):
        k = request.data.get('korisnicko_ime','')
        print(k)
        korisnik = Registracija.exists(k)
        if korisnik is not None:
            serializer = KorisnikZaboravljenaLozinkaSerializer(korisnik)
            data=serializer.data
            data['odgovor']="Ok"
            print("ovde")
            return Response(data)
        else:
            return Response({
                'korisnicko_ime':"",
                'pitanje_lozinka':"",
                'odgovor_lozinka': "", 
                'tip': "", "odgovor": "Pogrešno korisničko ime"}
            , status=200)
           
        
class ZaboravljenaLozinkaPitanje(APIView):
    def post(self,request, *args, **kwargs):
        korime = request.data.get('korisnicko_ime','')
        korisnik = Registracija.exists(korime)
        if korisnik is not None:
            odg=request.data.get("odgovor",'')
            if check_password(odg, korisnik.odgovor_lozinka):
                return Response({"odgovor": "Tačan odgovor!"}, status=200)
            else:
                return Response({"odgovor": "Netačan odgovor!"}, status=200)
            
class NovaLozinka(APIView): 
    def post(self,request, *args, **kwargs):
        korime = request.data.get('korisnicko_ime','')
        l1 = request.data.get('lozinka','')
        l2 = request.data.get('potvrda_lozinke','')
        if l1 == l2:
            mess=NovaLozinka.goodpass(l1)
            if mess is not None:
                return Response({"odgovor": mess}, status=200)
            korisnik = Registracija.exists(korime)
            if korisnik is not None:
                korisnik.sifra = make_password(l1)
                korisnik.save()
                return Response({"odgovor": "Uspeh"}, status=200)
        else:
            return Response({"odgovor": "Lozinke se ne poklapaju!"}, status=200)

        return Response({"odgovor": "Greska"}, status=200)
    
    def goodpass(lozinka):
        if not (re.search(r'[a-zA-Z]', lozinka)):
            return 'Lozinka mora imati bar jedno slovo!'
        if not (re.search(r'\d', lozinka)):
            return 'Lozinka mora imati bar jedan broj!'
        if not len(lozinka) > 5:
            return 'Lozinka mora biti duza od 5 karaktera!'
        return None
     
class PredloziIzvodjaca(APIView):
    def get(self, request):
        if Predlaze_Izvodjaca.objects.count() == 0:
            return Response({
                'id':0,
                'ime_izvodjaca': "", 
                'kor_ime': "", 
                'zan_naziv': "",
                "odgovor": "Nema novih predloga"
            }, status=200)

        izvodjaci = Predlaze_Izvodjaca.objects.all().select_related('kor', 'zan')
        serializer = PredlazeIzvodjacaSerializer(izvodjaci, many=True)

        response_data = serializer.data
        for item in response_data:
            item['odgovor'] = "Uspešno učitano"  

        return Response(response_data)

class PredloziIzvodjacaOdbij(APIView):
    def post(self,request, *args, **kwargs):
        id=request.data.get('id','')
        Predlaze_Izvodjaca.objects.filter(id=id).delete()
        
        if Predlaze_Izvodjaca.objects.count() == 0:
            return Response({
                'id':0,
                'ime_izvodjaca': "", 
                'kor_ime': "", 
                'zan_naziv': "",
                "odgovor": "Nema novih predloga"
            }, status=200)

        izvodjaci = Predlaze_Izvodjaca.objects.all().select_related('kor', 'zan')
        serializer = PredlazeIzvodjacaSerializer(izvodjaci, many=True)

        response_data = serializer.data
        for item in response_data:
            item['odgovor'] = "Uspešno učitano" 

        return Response(response_data)
    
class PredloziPesme(APIView):
    def get(self, request):
        
        if Predlaze_Pesmu.objects.count() == 0:
            return Response({
                'id':0,
                'naziv_pesme':"",
                'izv_ime': "", 
                'kor_ime': "", 
                'zan_naziv': "",
                "odgovor": "Nema novih predloga"
            }, status=200)

        pesme = Predlaze_Pesmu.objects.all().select_related("kor","izv", "izv__zan")
        serializer = PredlazePesmaSerializer(pesme, many=True)

        response_data = serializer.data
        for item in response_data:
            item['odgovor'] = "Uspešno učitano"  

        return Response(response_data)
    
class PredloziPesmeOdbij(APIView):
    def post(self,request, *args, **kwargs):
        id=request.data.get('id','')
        Predlaze_Pesmu.objects.filter(id=id).delete()
        
        if Predlaze_Pesmu.objects.count() == 0:
            return Response({
                'id':0,
                'naziv_pesme':"",
                'izv_ime': "", 
                'kor_ime': "", 
                'zan_naziv': "",
                "odgovor": "Nema novih predloga"
            }, status=200)

        pesme = Predlaze_Pesmu.objects.all().select_related("kor","izv", "izv__zan")
        serializer = PredlazePesmaSerializer(pesme, many=True)

        response_data = serializer.data
        for item in response_data:
            item['odgovor'] = "Uspešno učitano"  

        return Response(response_data)
    

# duel

class GenerisiSifruAPI(APIView):
    def post(self, request):
        """
        ANDROID:
        get zahtev za generisanje sire
        """
        print("GENERISI")
        sifra, stihovi = GenerisiSifruAPI.nova_soba(request)
        print(stihovi)
        return Response({'sifra': sifra, 'stihovi': stihovi})
    
    def nova_soba(request):
        """
        ANDROID:
        generise novu sobu i vraca njen identifikator;
        nasumicno bira 7 pesama za duel, upisuje ih u bazu i vraca ih;
        """
        print("nova soba")
        korisnickoIme= request.data.get('korisnickoIme','')
        if korisnickoIme is not None:
            korisnik = GenerisiSifruAPI.exists(korisnickoIme)

        svi_stihovi_ids = list(Stihovi.objects.values_list('id', flat=True))
        random.shuffle(svi_stihovi_ids)
        id_stihovi = svi_stihovi_ids[:7]

        if korisnickoIme is not None:
            soba = Soba(kor_1=korisnik, stihovi=json.dumps(id_stihovi),poeni_1=-1)
        else:
            soba = Soba(stihovi=json.dumps(id_stihovi), poeni_1=-1)
        soba.save()

        return soba.id, soba.stihovi
    
    def exists(korime):
        """
        ANDROID:
        proverava da li postoji korisnik sa datim korisnickim imenom u bazi
        """
        return Korisnik.objects.get(korisnicko_ime=korime)

class ProveriSifruAPI(APIView):
    def post(self, request):
        provera, stihovi = ProveriSifruAPI.provera_sobe(request)
        
        if provera:
            ret = DuelAPI.duel_runda_android2(request, stihovi)
            print("ovde")
            return Response({
                'stihovi': stihovi,
                'zvuk': ret['zvuk'],
                'crtice': ret['crtice'],
                'runda': 0,
                'poeni': 0,
                'error':'NE'
            })
        return Response({'stihovi': '', 'zvuk':'','crtice': '','runda':'',
                'poeni': '','error': 'Šifra nije ispravna!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def provera_sobe(request):
        """
        ANDROID:
        proverava da li postoji soba sa datom sifrom;
        upisuje drugog korisnika u datu sobu;
        takodje vraca izabrane stihove za taj duel;
        """
        sifra = request.data.get('sifra','')
        korisnickoIme=request.data.get('korisnickoIme','')
        try:
            soba = Soba.objects.get(pk=sifra)
            #if 'korisnickoIme' in request.COOKIES:
             #   soba.kor_2 = GenerisiSifruAPI.exists(korisnickoIme)

            soba.poeni_2 = -1 # da bi se znalo da je dosao
            soba.save()
            return True, soba.stihovi
        except Soba.DoesNotExist:
            return False, None
    
class StigaoIgracAPI(APIView):
    """
    ANDROID
    Proverava da li je drugi igrac uneo generisanu sifru sobe i vraca tu informaciju kao json objekat.
    """
    def post(self, request):
        print("STIGAO IGRAC")
        sifra = request.data.get('sifra', '')
        stigao = self.provera_dosao(sifra)
        print(stigao)
        return Response({'stigao': stigao})

    def provera_dosao(self, sifra):
        """
        ANDROID:
        proverava da li je drugi igrac uneo generisanu sifru sobe i vraca tu informaciju kao json objekat;
        """
        try:
            soba = Soba.objects.get(pk=sifra)
            if soba.poeni_2 == -1:
                return "true"
            else:
                return "false"
        except Soba.DoesNotExist:
            return {'error': 'Soba sa ovom šifrom ne postoji'}, status.HTTP_404_NOT_FOUND
        
class CekanjeRezultataAPI(APIView):
    def post(self, request):
        postavi_cookie = CekanjeRezultataAPI.obrada_rezultata(request)
        #response = render(request,'./duel/cekanje_rezultata.html',{})
        if postavi_cookie:
            return Response({'odgovor': 'Gotovo'})
         #   response.set_cookie('upisuj', '') # trenutni korisnik je drugi zavrsio duel
        #return response
        return Response({'odgovor': 'Čeka se rezultat duela'})
    
    def obrada_rezultata(request):
        """
        upisuje rezultat duela za jednog igraca u bazu, u tabelu Soba;
        """
        #poeni_runde = []
        poeni_runde=request.data.get('rundaPoeni','')
        print(poeni_runde)
        #for i in range(1, 8):
        #    poeni_runde.append(int(request.COOKIES['runda' + str(i)]))
        poeni = int(request.data.get('poeni',''))
        soba_id = int(request.data.get('soba',''))
        soba = Soba.objects.get(pk=soba_id)
        print(soba)
        redniBroj=request.data.get('redniBroj','')
        print(redniBroj)
        
        if redniBroj == 1:
            soba.poeni_1 = poeni
            soba.poeni_runde_1 = json.dumps(poeni_runde)
            soba.save()
            if soba.poeni_2 == -1:  #drugi igrac je zaduzen za upisivanje konacnih rezultata u bazu
                return False
            return True

        else:
            soba.poeni_2 = poeni
            soba.poeni_runde_2 = json.dumps(poeni_runde)
            soba.save()
            if soba.poeni_1 == -1:  #drugi igrac je zaduzen za upisivanje konacnih rezultata u bazu
                return False
            return True
        
    
class ZavrsioIgracAPI(APIView):
    def get(self, request):
        zavrsio = provera_zavrsio(request)
        return Response({'zavrsio': zavrsio})

class KrajDuelaAPI(APIView):
    def post(self, request):
        korIme=request.data.get("korisnickoIme",'')
        if korIme is not "":
            ulogovan=True
        else:
            ulogovan=False
        rez = KrajDuelaAPI.gotov_duel(request)
        return Response({
            'poeni': rez['poeni'],
            'poeni_runde': rez['poeni_runde'],
            'igrac1': rez['igrac1'],
            'igrac2': rez['igrac2'],
            'ulogovan': ulogovan
        })
    
    def gotov_duel(request):
        """
        vraca rezultate duela nakon sto oba igraca zavrse;
        azurira broj licnih i rang poena za oba igraca;
        """
        soba_id = request.data.get('soba','')
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

        upisuj = request.data.get('upisuj','')

        if upisuj=='upisuj': 
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
        


class DuelAPI(APIView):
    def post(self, request):
        ret = DuelAPI.duel_runda_android(request)
        ru=request.data.get('rundePoeni','')
        return Response({
            'stihpoznat': ret['stihovi']['poznat_tekst'].split("<br>"),
            'crtice': ret['crtice'],
            'tacno': ret['stihovi']['nepoznat_tekst'],
            'zvuk': ret['stihovi']['zvuk'],
            'runda': ret['runda'],
            'poeni': ret['poeni'],
            'rundePoeni':ru
        })
    
    def duel_runda_android(request):
        stihovi_niz = json.loads(request.data.get('stihovi', '[]'))
        
        runda = request.data.get('runda', '')
        poeni = request.data.get('poeni', '')
       
        stihovi_id = stihovi_niz[runda - 1]
        stihovi = Stihovi.objects.get(pk=stihovi_id)

        stihovi_dict = {
            'id': stihovi.id,
            'poznat_tekst': stihovi.poznat_tekst,
            'nepoznat_tekst': stihovi.nepoznat_tekst,
            'zvuk': stihovi.zvuk
        }

        zvuk = os.path.join('..', 'static', 'songs', stihovi.zvuk)

        crtice = ""
        for znak in stihovi.nepoznat_tekst:
            if znak != " ":
                crtice += "_ "
            else:
                crtice += "  "

        return {
            'stihovi': stihovi_dict,  
            'zvuk': zvuk,
            'crtice': crtice,
            'runda': runda+1,
            'poeni': poeni
        }
    
    def duel_runda_android2(request,stihovi):
        stihovi_niz = json.loads(stihovi)
        print("DUEL 2 ANDROID")
        print(stihovi_niz)
        
        runda=1
        #if(runda==0):
         #   runda = runda + 1
        print(runda)

        poeni = request.data.get('poeni', '')
       
        stihovi_id = stihovi_niz[runda - 1]
        stihovi = Stihovi.objects.get(pk=stihovi_id)

        stihovi_dict = {
            'id': stihovi.id,
            'poznat_tekst': stihovi.poznat_tekst,
            'nepoznat_tekst': stihovi.nepoznat_tekst,
            'zvuk': stihovi.zvuk
        }

        zvuk = os.path.join('..', 'static', 'songs', stihovi.zvuk)

        crtice = ""
        for znak in stihovi.nepoznat_tekst:
            if znak != " ":
                crtice += "_ "
            else:
                crtice += "  "

        return {
            'stihovi': stihovi_niz,  # Vraćamo rečnik umesto objekta
            'zvuk': zvuk,
            'crtice': crtice,
            'runda': runda+1,
            'poeni': poeni
        }