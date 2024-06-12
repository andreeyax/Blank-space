# Autor: Maša Nikolić 2021/0439

from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik

class PregledRangListeViewTests(TestCase):

    def setUp(self):
        # napravicemo nove korisnike za testiranje
        # lozinka i odgovor_lozinka nece biti sifrovani, za testiranje to nije bitno zato sto testiramo samo pregled rang liste
        
        # Kreiramo nekoliko korisnika za testiranje rang liste - ukupno 5+1
        self.korisnik1 = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='sifra1',
            ime='Ime1',
            prezime='Prezime1',
            tip='M',
            pitanje_lozinka='Pitanje1',
            odgovor_lozinka='Odgovor1',
            licni_poeni=100,
            rang_poeni=50
        )
        self.korisnik2 = Korisnik.objects.create(
            korisnicko_ime='korisnik2',
            sifra='sifra2',
            ime='Ime2',
            prezime='Prezime2',
            tip='M',
            pitanje_lozinka='Pitanje2',
            odgovor_lozinka='Odgovor2',
            licni_poeni=200,
            rang_poeni=100
        )
        self.korisnik3 = Korisnik.objects.create(
            korisnicko_ime='korisnik3',
            sifra='sifra3',
            ime='Ime3',
            prezime='Prezime3',
            tip='M',
            pitanje_lozinka='Pitanje3',
            odgovor_lozinka='Odgovor3',
            licni_poeni=150,
            rang_poeni=75
        )
        self.korisnik4 = Korisnik.objects.create(
            korisnicko_ime='korisnik4',
            sifra='sifra4',
            ime='Ime4',
            prezime='Prezime4',
            tip='M',
            pitanje_lozinka='Pitanje4',
            odgovor_lozinka='Odgovor4',
            licni_poeni=80,
            rang_poeni=40
        )
        self.korisnik5 = Korisnik.objects.create(
            korisnicko_ime='korisnik5',
            sifra='sifra5',
            ime='Ime5',
            prezime='Prezime5',
            tip='M',
            pitanje_lozinka='Pitanje5',
            odgovor_lozinka='Odgovor5',
            licni_poeni=120,
            rang_poeni=60
        )
        self.korisnik6 = Korisnik.objects.create(
            korisnicko_ime='korisnik6',
            sifra='sifra6',
            ime='Ime6',
            prezime='Prezime6',
            tip='M',
            pitanje_lozinka='Pitanje6',
            odgovor_lozinka='Odgovor6',
            licni_poeni=90,
            rang_poeni=45
        )
        
    # korisnik je svakako ulogovan ako uopste moze da pristupi datoj stranici, tako da to ne treba proveravati
    def test_pregled_rang_liste(self):
        # postavlja cookie
        client = Client()
        client.cookies['korisnickoIme'] = 'korisnik1'

        response = client.get(reverse('rang_lista'))

        # Provera statusa i šablona
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './profil_rang_pravila/rang_lista.html')

        # Provera da li u odgovoru postoji sve što treba
        # Koristimo enumerate da proverimo rang svakog korisnika
        korisnici_poeni = [
            ('korisnik2', 100),
            ('korisnik3', 75),
            ('korisnik5', 60),
            ('korisnik1', 50),
            ('korisnik6', 45),
        ]
        for i, (korisnicko_ime, rang_poeni) in enumerate(korisnici_poeni, start=1):
            self.assertContains(response, korisnicko_ime)
            self.assertContains(response, str(i)) 
            self.assertContains(response, str(rang_poeni))          