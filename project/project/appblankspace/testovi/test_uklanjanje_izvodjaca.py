#Autor: Tamara Radojčić 2021/0214


from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Izvodjac, Zanr, Pesma

class UklanjanjeIzvodjacaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.zanr1 = Zanr.objects.create(naziv='Rock')
        self.izvodjac1 = Izvodjac.objects.create(ime='John', zan_id=self.zanr1.id)
        self.pesma1 = Pesma.objects.create(naziv='Pesma 1', izv_id=self.izvodjac1.id)
        self.zanr2 = Zanr.objects.create(naziv='Pop')
        self.izvodjac2 = Izvodjac.objects.create(ime='Jane', zan_id=self.zanr2.id)
        self.pesma2 = Pesma.objects.create(naziv='Pesma 2', izv_id=self.izvodjac2.id)

    def test_uklanjanje_izvodjaca(self):
        self.client.cookies['izvodjacbrisanje'] = str(self.izvodjac1.id)
        response = self.client.get(reverse('uklanjanje_izvodjaca'))
        self.assertFalse(Izvodjac.objects.filter(id=self.izvodjac1.id).exists())
        self.assertTrue(Izvodjac.objects.filter(id=self.izvodjac2.id).exists())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_izvodjaca.html')
        # provera da li su sve pesme koje pripadaju obrisanom izvodjacu obrisane
        self.assertFalse(Pesma.objects.filter(id=self.pesma1.id).exists())

    def test_uklanjanje_izvodjaca_bez_cookie(self):
        response = self.client.get(reverse('uklanjanje_izvodjaca'))
        self.assertTrue(Izvodjac.objects.filter(id=self.izvodjac1.id).exists())
        self.assertTrue(Izvodjac.objects.filter(id=self.izvodjac2.id).exists())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_izvodjaca.html')
        # provera da li su sve pesme koje pripadaju izvodjacu i dalje u bazi
        self.assertTrue(Pesma.objects.filter(id=self.pesma1.id).exists())

    def test_izbor_zanra1Uklanjanje(self):
        # izbor zanra od izvodjaca koji se uklanja
        response = self.client.get(reverse('izbor_zanra1Uklanjanje'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/izbor_zanra1.html')
        self.assertCountEqual(response.context['zanrovi'], Zanr.objects.all())