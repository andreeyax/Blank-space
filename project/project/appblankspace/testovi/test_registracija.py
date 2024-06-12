#Autor: Maša Nikolić 2021/0439


from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone
from appblankspace.models import Korisnik

class RegistrationViewTests(TestCase):

    def test_get_registration_page(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')

    def test_successful_registration(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zubicvila123',
            'plozinka': 'zubicvila123',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './pocetne/pocetna_brucos.html')
        korisnik = Korisnik.objects.get(korisnicko_ime='zubicvila')
        self.assertIsNotNone(korisnik)
        self.assertTrue(check_password('zubicvila123', korisnik.sifra))
        self.assertTrue('korisnickoIme' in response.cookies)

    
    def test_registration_existing_username(self):
        Korisnik.objects.create(
            korisnicko_ime='zubicvila',
            sifra=make_password('zubicvila123'),
            ime='Zubic',
            prezime='Vila',
            tip='B',
            pitanje_lozinka='Vila?',
            odgovor_lozinka=make_password('zubic'),
            rang_poeni=0,
            licni_poeni=0,
            poslednja_aktivnost=timezone.now()
        )
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zubicvila123',
            'plozinka': 'zubicvila123',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Korisnik sa tim imenom već postoji!')
    

    def test_registration_passwords_do_not_match(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zubicvila123',
            'plozinka': 'zubicvila124',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Lozinka i potvrda lozinke se ne poklapaju!')

    def test_registration_question_too_long(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zubicvila123',
            'plozinka': 'zubicvila123',
            'pitanje': 'P' * 256,
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Pitanje je duže od 255 karaktera!')

    def test_registration_answer_too_long(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zubicvila123',
            'plozinka': 'zubicvila123',
            'pitanje': 'Vila?',
            'odgovor': 'O' * 256
        }
         
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Odgovor je duži od 255 karaktera!')

    def test_registration_invalid_password(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zubicvila',
            'plozinka': 'zubicvila',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Lozinka mora imati bar jedan broj!')
    
    def test_registration_password_4(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zu12',
            'plozinka': 'zu12',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Lozinka mora biti duza od 5 karaktera!')
    
    def test_registration_password_5(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zu122',
            'plozinka': 'zu122',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/registration.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].message, 'Lozinka mora biti duza od 5 karaktera!')
    
    def test_registration_password_6(self):
        data = {
            'ime_prezime': 'Zubic Vila',
            'korime': 'zubicvila',
            'lozinka': 'zub123',
            'plozinka': 'zub123',
            'pitanje': 'Vila?',
            'odgovor': 'zubic'
        }
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './pocetne/pocetna_brucos.html')
        korisnik = Korisnik.objects.get(korisnicko_ime='zubicvila')
        self.assertIsNotNone(korisnik)
        self.assertTrue(check_password('zub123', korisnik.sifra))
        self.assertTrue('korisnickoIme' in response.cookies)