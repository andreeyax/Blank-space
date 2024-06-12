# Autor: Andrija Tomić 2021/0489
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik,Predlaze_Izvodjaca

class PredloziIzvodjacaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
     
    def test_predlozi_izvodjaca(self):
        client = Client()
        response = client.get(reverse('predlozi_pesama'))

        # provera da li je korisnik obrisan i da li drugi postoji
        #self.assertFalse(Korisnik.objects.filter(id=self.za_brisanje.id).exists())
        #self.assertTrue(Predlaze_Izvodjaca.objects.filter(id=self.za_prikaz.id).exists())

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './predlozi/predlozi_pesama.html')
        
