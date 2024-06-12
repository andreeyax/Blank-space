#Autor: Tamara Radojčić 2021/0214

from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Izvodjac, Pesma, Zanr

class UklanjanjePesamaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.zanr1 = Zanr.objects.create(naziv='Rock')
        self.izvodjac1 = Izvodjac.objects.create(ime='John', zan_id=self.zanr1.id)
        self.pesma1 = Pesma.objects.create(naziv='Pesma 1', izv_id=self.izvodjac1.id)
        self.zanr2 = Zanr.objects.create(naziv='Pop')
        self.izvodjac2 = Izvodjac.objects.create(ime='Jane', zan_id=self.zanr2.id)
        self.pesma2 = Pesma.objects.create(naziv='Pesma 2', izv_id=self.izvodjac2.id)

    def test_uklanjanje_pesama(self):
        self.client.cookies['pesmaidbrisanje'] = str(self.pesma1.id)
        response = self.client.get(reverse('uklanjanje_pesama'))
        self.assertFalse(Pesma.objects.filter(id=self.pesma1.id).exists())
        self.assertTrue(Pesma.objects.filter(id=self.pesma2.id).exists())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_pesama.html')

    def test_uklanjanje_pesama_bez_cookie(self):
        response = self.client.get(reverse('uklanjanje_pesama'))
        self.assertTrue(Pesma.objects.filter(id=self.pesma1.id).exists())
        self.assertTrue(Pesma.objects.filter(id=self.pesma2.id).exists())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_pesama.html')

    def test_izbor_izvodjacaUklanjanje(self):
        # izbor izvodjaca od pesme koja se uklanja
        self.client.cookies['odabranzanrpesmazabrisanje'] = str(self.izvodjac1.zan_id)
        response = self.client.get(reverse('izbor_izvodjacaUklanjanje'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/izbor_izvodjaca.html')
        self.assertCountEqual(response.context['izvodjaci'], Izvodjac.objects.filter(zan_id=self.izvodjac1.zan_id))

    def test_izbor_zanra2Uklanjanje(self):
        # izbor zanra od pesme koja se uklanja
        response = self.client.get(reverse('izbor_zanra2Uklanjanje'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/izbor_zanra2.html')
        self.assertCountEqual(response.context['zanrovi'], Zanr.objects.all())