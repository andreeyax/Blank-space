# Autor: Andrija Tomić 2021/0489
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Zanr

class PredlaganjeIzvodjacaViewTests(TestCase):

     

   
    def test_pregled_pravila_igre(self):
        
        client = Client()
        response = client.get(reverse('predlaganje_izvodjaca'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './predlaganje/predlaganje_izvodjaca.html')

        # provera da li u  ogovoru postoji sve sto treba
        self.assertContains(response, 'Ime izvođača')
        self.assertContains(response, 'Naziv žanra')
        self.assertContains(response, 'Predloži')
        for i in range(Zanr.objects.count()):
            zanr=Zanr.objects.get(id=i+1)
            self.assertContains(response, zanr.naziv)
       

        
        
