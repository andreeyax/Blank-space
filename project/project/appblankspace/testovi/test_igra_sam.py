# Autor: Jana Stanisavljević 2021/0381
import json
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik, Zanr, Izvodjac, Pesma, Stihovi

class IgraSamViewTests(TestCase):

    def setUp(self):
        # pravi nove zanrove za testiranje
        Zanr.objects.create(naziv='Indie Pop')
        Zanr.objects.create(naziv='Punk')

        # pravi nove stihove za testiranje
        self.zanr = Zanr.objects.create(naziv='Rok')
        self.izvodjac = Izvodjac.objects.create(ime='Queen', zan_id=self.zanr.id)
        self.pesma = Pesma.objects.create(naziv='Bohemian Rhapsody', izv_id=self.izvodjac.id)
        self.stih = Stihovi.objects.create(
            pes_id=self.pesma.id, 
            nivo='E', 
            poznat_tekst='Is this the real life?', 
            nepoznat_tekst='Is this just fantasy?',
            zvuk='bohemian.mp3'
        )
        # moraju i ovi jer ne smeju da se ponove isti stihovi
        self.stih1 = Stihovi.objects.create(
            pes_id=self.pesma.id, 
            nivo='E', 
            poznat_tekst='Is this the real life?', 
            nepoznat_tekst='Is this just fantasy?',
            zvuk='bohemian.mp3'
        )

        # pravi novog korisnika za testiranje
        # lozinka i odgovor_lozinka nisu sifrovani jer to ovde nije bitno
        self.korisnik = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='korisnik1',
            ime='Korisnik',
            prezime='1',
            tip='B',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            licni_poeni=48
        )


    def test_izbor_nivoa(self):
        client = Client()
        response = client.get(reverse('nivo'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/nivo.html')


    def test_izbor_zanra(self):
        client = Client()
        response = client.get(reverse('zanr'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/zanr.html')

        # provera da li su dobri nazivi zanrova prosledjeni
        zanrovi = response.context['zanrovi']
        self.assertEqual(len(zanrovi), 3)
        self.assertEqual(zanrovi[0].naziv, 'Indie Pop')
        self.assertEqual(zanrovi[1].naziv, 'Punk')


    def test_igra_sam_prva_runda(self):
        client = Client()

        # postavljanje cookie-a
        client.cookies['runda_igra_sam'] = '0'
        client.cookies['odabrani_zanrovi_igrasam'] = f'["{self.zanr.naziv}"]'
        client.cookies['odabrana_tezina_igra_sam'] = 'E'

        response = client.get(reverse('igra_sam'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/igra_sam.html')

        # provera da li je sve prosledjeno
        self.assertIn('stihpoznat', response.context)
        self.assertIn('crtice', response.context)
        self.assertIn('tacno', response.context)
        self.assertIn('izvodjac', response.context)
        self.assertIn('zvuk', response.context)
        self.assertIn('pesma', response.context)
        self.assertIn('runda', response.context)

        # provera da li cookie postoji
        self.assertIn('bilo', response.cookies)

        # provera da li je cookie postavljen na dobru vrednost
        self.assertEqual(response.cookies['runda_igra_sam'].value, '1')


    def test_igra_sam_izmedju_runda(self):
        client = Client()

        # postavljanje cookie-a
        client.cookies['runda_igra_sam'] = '1'
        client.cookies['odabrani_zanrovi_igrasam'] = f'["{self.zanr.naziv}"]'
        client.cookies['odabrana_tezina_igra_sam'] = 'E'
        client.cookies['bilo'] = json.dumps([self.stih.id])

        response = client.get(reverse('igra_sam'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/igra_sam.html')

        # provera da li cookie postoji
        self.assertIn('bilo', response.cookies)

        # provera da li je cookie postavljen na dobru vrednost
        self.assertEqual(response.cookies['runda_igra_sam'].value, '2')


    def test_kraj_igre_registrovani_korisnik_bez_promene_tipa(self):
        client = Client()

        # postavljanje cookie-a
        client.cookies['korisnickoIme'] = self.korisnik.korisnicko_ime
        client.cookies['poeni_igra_sam'] = '1'

        response = client.get(reverse('kraj_igre'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/kraj_igre.html')

        # uzima ponovo korisnika da bi proverio da li su dodati poeni i da li je tip promenjen
        self.korisnik.refresh_from_db()
        self.assertEqual(self.korisnik.licni_poeni, 49)
        self.assertEqual(self.korisnik.tip, 'B')

        # provera da li je sve prosledjeno
        self.assertIn('poeni', response.context)
        self.assertIn('tip', response.context)
        self.assertIn('ulogovan', response.context)

        # provere cookie-a
        self.assertEqual(response.cookies['ima_pesama'].value, '')


    def test_kraj_igre_gost(self):
        client = Client()

        # postavljanje cookie-a
        client.cookies['poeni_igra_sam'] = '5'

        response = client.get(reverse('kraj_igre'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/kraj_igre.html')

        # provera da li je sve prosledjeno
        self.assertIn('poeni', response.context)
        self.assertIn('tip', response.context)
        self.assertIn('ulogovan', response.context)

        # posto je u pitanju gost, tip u cookie-u treba da bude N
        self.assertEqual(response.context['tip'], 'N')
        self.assertFalse(response.context['ulogovan'])


    def test_kraj_igre_registrovani_korisnik_sa_promenom_tipa(self):
        client = Client()

        # postavljanje cookie-a
        client.cookies['korisnickoIme'] = self.korisnik.korisnicko_ime
        client.cookies['poeni_igra_sam'] = '2'

        response = client.get(reverse('kraj_igre'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './igra_sam/kraj_igre.html')

        # uzima ponovo korisnika da bi proverio da li su dodati poeni i da li je tip promenjen
        self.korisnik.refresh_from_db()
        self.assertEqual(self.korisnik.licni_poeni, 50)
        self.assertEqual(self.korisnik.tip, 'S')

        # provera da li je sve prosledjeno
        self.assertIn('poeni', response.context)
        self.assertIn('tip', response.context)
        self.assertIn('ulogovan', response.context)

        # provere cookie-a
        self.assertEqual(response.cookies['ima_pesama'].value, '')
