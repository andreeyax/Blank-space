# Autor: Jana Stanisavljević 2021/0381
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik

class UklanjanjeKorisnikaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.napravi_korisnike()


    def napravi_korisnike(self):
        # pravi dva korisnika od kojih ce jedan biti obrisan
        # lozinka i odgovor_lozinka nisu sifrovani jer to ovde nije bitno
        self.za_brisanje = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='korisnik1',
            ime='Korisnik',
            prezime='1',
            tip='B',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor'
            )
        self.korisnik_ostaje = Korisnik.objects.create(
            korisnicko_ime='korisnik2',
            sifra='korisnik2',
            ime='Korisnik',
            prezime='2',
            tip='B',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor'
        )


    def test_uklanjanje_korisnika_ispravan_id(self):
        client = Client()
        client.cookies['id'] = self.za_brisanje.id
        response = client.get(reverse('uklanjanje_korisnika'))

        # provera da li je korisnik obrisan i da li drugi postoji
        self.assertFalse(Korisnik.objects.filter(id=self.za_brisanje.id).exists())
        self.assertTrue(Korisnik.objects.filter(id=self.korisnik_ostaje.id).exists())

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_korisnika.html')


    def test_uklanjanje_korisnika_bez_cookie(self):
        client = Client()
        response = client.get(reverse('uklanjanje_korisnika'))

        # nista ne bi trebalo da bude obrisano
        self.assertTrue(Korisnik.objects.filter(id=self.za_brisanje.id).exists())
        self.assertTrue(Korisnik.objects.filter(id=self.korisnik_ostaje.id).exists())

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_korisnika.html')


    def test_uklanjanje_korisnika_los_id(self):
        client = Client()
        client.cookies['id'] = '222'
        response = client.get(reverse('uklanjanje_korisnika'))

        # nista ne bi trebalo da bude obrisano
        self.assertTrue(Korisnik.objects.filter(id=self.za_brisanje.id).exists())
        self.assertTrue(Korisnik.objects.filter(id=self.korisnik_ostaje.id).exists())

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_korisnika.html')
