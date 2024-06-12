# Autor: Jana Stanisavljević 2021/0381
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik

class PregledProfilaViewTests(TestCase):

    def setUp(self):
        # pravi novog korisnika za testiranje
        # lozinka i odgovor_lozinka nisu sifrovani jer to ovde nije bitno
        self.korisnik = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='korisnik1',
            ime='Korisnik',
            prezime='1',
            tip='M',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            licni_poeni=100,
            rang_poeni=50
            )
        

    # korisnik je svakako ulogovan ako uopste moze da pristupi datoj stranici, tako da to ne treba proveravati
    def test_pregled_profila(self):
        # postavlja cookie
        client = Client()
        client.cookies['korisnickoIme'] = 'korisnik1'

        response = client.get(reverse('pregled_profila'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './profil_rang_pravila/pregled_profila.html')

        # provera da li u  ogovoru postoji sve sto treba
        self.assertContains(response, 'Korisnik')
        self.assertContains(response, '1')
        self.assertContains(response, 'korisnik1')
        self.assertContains(response, '100')
        self.assertContains(response, '50')
        self.assertContains(response, '#')
