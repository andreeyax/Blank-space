# Autor: Andrija Tomić 2021/0489
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik,Predlaze_Izvodjaca,Zanr

class PredloziIzvodjacaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        Zanr.objects.create(
            id='3',
            naziv='Narodna'
        )
        self.za_brisanje = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='korisnik1',
            ime='Korisnik',
            prezime='1',
            tip='B',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor'
            )

        self.za_odbijanje=Predlaze_Izvodjaca.objects.create(
            
            ime_izvodjaca='Taylor',
            kor_id=self.za_brisanje.id,
            zan_id='3'
        )
        Predlaze_Izvodjaca.objects.create(
            
            ime_izvodjaca='Taylor',
            kor_id=self.za_brisanje.id,
            zan_id='3'
        )
        Predlaze_Izvodjaca.objects.create(
            
            ime_izvodjaca='Taylor',
            kor_id=self.za_brisanje.id,
            zan_id='3'
        )
    

    def test_predlozi_izvodjaca(self):
        
        response = self.client.post(reverse('predlozi_izvodjaca'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './predlozi/predlozi_izvodjaca.html')
        self.assertTrue(Predlaze_Izvodjaca.objects.filter(id=self.za_odbijanje.id).exists())
        
