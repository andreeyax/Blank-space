# Autor: Maša Nikolić 2021/0439

from django.test import TestCase, Client,RequestFactory
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from appblankspace.models import Korisnik
import unittest
from appblankspace.views import goodpass,newpass

class ForgotPasswordViewTests(TestCase):

    def setUp(self):
        # Kreiranje korisnika za testiranje
        self.korisnik = Korisnik.objects.create(
            korisnicko_ime='testKorisnik',
            sifra=make_password('testSifra'),
            ime='Test',
            prezime='Korisnik',
            tip='M',
            pitanje_lozinka='Kako se zove tvoj prvi ljubimac?',
            odgovor_lozinka=make_password('Rex'),
            licni_poeni=0,
            rang_poeni=0
        )
        self.client = Client()

    def test_forgotpass_correct_username(self):
        # Testiranje ispravnog korisničkog imena
        response = self.client.post(reverse('forgotpass'), {'korime': 'testKorisnik'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/forgotpassq.html')
        self.assertIn('pitanje', response.context)
        self.assertEqual(response.context['pitanje'], 'Kako se zove tvoj prvi ljubimac?')
        self.assertIn('korisnickoIme', response.cookies)
        self.assertEqual(response.cookies['korisnickoIme'].value, 'testKorisnik')
        print('TEST_OPORAVAK_LOZINKE_CORRECT_USERNAME')

    def test_forgotpass_incorrect_username(self):
        # Testiranje pogrešnog korisničkog imena
        response = self.client.post(reverse('forgotpass'), {'korime': 'pogresnoKorisnickoIme'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/forgotpass.html')
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Pogrešno korisničko ime!')
        self.assertNotIn('korisnickoIme', response.context)
        print('TEST_OPORAVAK_LOZINKE_INCORRECT_USERNAME')

    def test_forgotpassq_correct_answer(self):
        # Postavljanje cookie-a za korisničko ime
        self.client.cookies['korisnickoIme'] = 'testKorisnik'
        response = self.client.post(reverse('forgotpassq'), {'odgovor': 'Rex'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('newpass'))
        print('TEST_OPORAVAK_CORRECT_ANSWRER')

    def test_forgotpassq_incorrect_answer(self):
        # Postavljanje cookie-a za korisničko ime
        self.client.cookies['korisnickoIme'] = 'testKorisnik'
        response = self.client.post(reverse('forgotpassq'), {'odgovor': 'PogresanOdgovor'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/forgotpassq.html')
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Netačan odgovor!')
        self.assertIn('pitanje', response.context)
        self.assertEqual(response.context['pitanje'], 'Kako se zove tvoj prvi ljubimac?')
        print('TEST_OPORAVAK_INCORRECT_ANSWRER')

    def test_correctUser_existing_user(self):
        factory = RequestFactory()
        request = factory.post(reverse('correctUser'), {'korime': 'existinguser'})
        
        response = self.client.get(reverse('correctUser'))

        self.assertEqual(response.status_code, 200)
    
    def test_goodpass_valid(self):
        password = "Test123"
        self.assertIsNone(goodpass(password))  

    def test_goodpass_no_letter(self):
        password = "123456"
        expected_error = 'Lozinka mora imati bar jedno slovo!'
        self.assertEqual(goodpass(password), expected_error)

    def test_goodpass_no_digit(self):
        password = "TestTest"
        expected_error = 'Lozinka mora imati bar jedan broj!'
        self.assertEqual(goodpass(password), expected_error)

    def test_goodpass_short(self):
        password = "Tes12"
        expected_error = 'Lozinka mora biti duza od 5 karaktera!'
        self.assertEqual(goodpass(password), expected_error)
    
    def test_newpass_matching_passwords(self):
        factory = RequestFactory()
        request = factory.post('/newpass', {'korisnickoIme': 'testuser', 'lozinka1': 'Test123', 'lozinka2': 'Test123'})
        response = newpass(request)
        self.assertTemplateUsed(response, './autorizacija/newpass.html')

  