#Autor: Tamara Radojčić 2021/0214


from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Zanr, Izvodjac, Pesma

class UklanjanjeZanrovaViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.zanr1 = Zanr.objects.create(naziv='Rock')
        self.izvodjac1 = Izvodjac.objects.create(ime='John', zan_id=self.zanr1.id)
        self.pesma1 = Pesma.objects.create(naziv='Pesma 1', izv_id=self.izvodjac1.id)
        self.zanr2 = Zanr.objects.create(naziv='Pop')
        self.izvodjac2 = Izvodjac.objects.create(ime='Jane', zan_id=self.zanr2.id)
        self.pesma2 = Pesma.objects.create(naziv='Pesma 2', izv_id=self.izvodjac2.id)

    def test_uklanjanje_zanra(self):
        self.client.cookies['zanr'] = str(self.zanr1.id)
        response = self.client.get(reverse('uklanjanje_zanrova'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_zanrova.html')
        self.assertFalse(Zanr.objects.filter(id=self.zanr1.id).exists())
        self.assertEqual(response.cookies['zanr'].value, 'None')
        # provera da li su i izvodjaci obrisanog zanra obrisani
        self.assertFalse(Izvodjac.objects.filter(zan_id=self.zanr1.id).exists())
        # provera da li su i pesme obrisanog zanra obrisane
        self.assertFalse(Pesma.objects.filter(izv_id=self.izvodjac1.id).exists())

    def test_uklanjanje_zanra_bez_cookie(self):
        response = self.client.get(reverse('uklanjanje_zanrova'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './uklanjanje/uklanjanje_zanrova.html')
        self.assertTrue(Zanr.objects.filter(id=self.zanr1.id).exists())
        self.assertEqual(response.cookies['zanr'].value, 'None')
        # provera da li su izvodjaci i dalje u bazi
        self.assertTrue(Izvodjac.objects.filter(zan_id=self.zanr1.id).exists())
        # provera da li su pesme i dalje u bazi
        self.assertTrue(Pesma.objects.filter(izv_id=self.izvodjac1.id).exists())