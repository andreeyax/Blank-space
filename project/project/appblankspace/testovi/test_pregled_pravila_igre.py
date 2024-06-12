# Autor: Andrija Tomić 2021/0489
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik

class PregledPravilaIgreViewTests(TestCase):

     

    # korisnik je svakako ulogovan ako uopste moze da pristupi datoj stranici, tako da to ne treba proveravati
    def test_pregled_pravila_igre(self):
        # postavlja cookie
        client = Client()
        #client.cookies['korisnickoIme'] = 'korisnik1'

        response = client.get(reverse('pravila_igre'))

        # provera statusa i template-a
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './profil_rang_pravila/pravila_igre.html')

        # provera da li u  ogovoru postoji sve sto treba
        self.assertContains(response, 'Opis')
        self.assertContains(response, 'Mogućnosti')
        self.assertContains(response, 'Tok igre')
        self.assertContains(response, 'Sakupljaj poene')
        
