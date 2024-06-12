#Autor: Maša Nikolić 2021/0439

from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from appblankspace.models import Korisnik
from appblankspace.views import exists, authorize, mainpage
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from appblankspace.views import login, mainpage

class AutorizacijaTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.korisnik = Korisnik.objects.create(
            korisnicko_ime='korisnik22',
            sifra=make_password('korisnik22'),
            ime='Korisnik',
            prezime='Prezime',
            tip='S',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka=make_password('Odgovor'),
            licni_poeni=10,
            rang_poeni=5
        )
        self.client = Client()

    def test_exists(self):
        # Testiranje da li funkcija exists pronalazi korisnika
        korisnik = exists('korisnik22')
        self.assertIsNotNone(korisnik)
        self.assertEqual(korisnik.korisnicko_ime, 'korisnik22')

        # Testiranje da li funkcija exists vraća None za nepostojećeg korisnika
        korisnik = exists('nepostojeci')
        self.assertIsNone(korisnik)

    def test_authorize_correct_credentials(self):
        # Kreiranje korisnika za testiranje
        korisnik = Korisnik.objects.create(
            korisnicko_ime='testkorisnik',
            sifra=make_password('testlozinka')
        )

        # Pravljenje zahteva sa ispravnim korisničkim imenom i lozinkom
        request = self.factory.post('/login/', {'korime': 'testkorisnik', 'loz': 'testlozinka'})
        
        # Poziv funkcije authorize() sa ispravnim podacima
        result = authorize('testkorisnik', 'testlozinka', request)

        # Provera da li je korisnik uspešno autorizovan
        self.assertIsNotNone(result)
        self.assertEqual(result.korisnicko_ime, 'testkorisnik')

        # Provera da li nema poruka o grešci
        storage = get_messages(request)
        self.assertEqual(len(storage), 0)

    def test_authorize_incorrect_credentials(self):
        # Kreiranje korisnika za testiranje
        Korisnik.objects.create(
            korisnicko_ime='testkorisnik',
            sifra=make_password('testlozinka')
        )

        # Pravljenje zahteva sa netačnim korisničkim imenom i lozinkom
        request = self.factory.post('/login/', {'korime': 'testkorisnik', 'loz': 'netacnalozinka'})

        # Dodavanje podrške za poruke u zahtev
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        # Poziv funkcije authorize() sa netačnim podacima
        result = authorize('testkorisnik', 'netacnalozinka', request)

        storage = list(get_messages(request))
      
        found_error_message = False
        for message in storage:
            if str(message) == 'Pogrešna loznika!':  
                found_error_message = True
                break

        self.assertTrue(found_error_message)

    def test_mainpage(self):
        request = self.factory.post(reverse('login'), {'korime': 'korisnik22', 'loz': 'korisnik22'})
        response = mainpage(self.korisnik, request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('korisnickoIme', response.cookies)

    def test_login_view(self):
        # Testiranje GET zahteva
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/login.html')

        # Testiranje uspešnog logovanja
        response = self.client.post(reverse('login'), {'korime': 'korisnik22', 'loz': 'korisnik22'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './pocetne/pocetna_student.html')
        self.assertIn('korime', self.client.session)
        self.assertEqual(self.client.session['korime'], 'korisnik22')
        self.assertEqual(response.cookies['korisnickoIme'].value, 'korisnik22')

        # Testiranje logovanja sa pogrešnom lozinkom
        response = self.client.post(reverse('login'), {'korime': 'korisnik22', 'loz': 'pogresna'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Pogrešna loznika!')

        # Testiranje logovanja sa nepostojećim korisnikom
        response = self.client.post(reverse('login'), {'korime': 'nepostojeci', 'loz': 'korisnik22'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './autorizacija/login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Pogrešno korisničko ime!')

    def test_login_unsuccessful(self):
        client = Client()
        # Kreiranje korisnika
        Korisnik.objects.create(
            korisnicko_ime='testuser',
            sifra=make_password('testpassword')
        )
        # Poziv funkcije za prijavljivanje sa pogrešnom lozinkom
        response = client.post(reverse('login'), {'korime': 'testuser', 'loz': 'wrongpassword'})
        
        # Provera da li se korisnik ne uspeva ulogovati
        self.assertNotIn('_auth_user_id', client.session)
        # Provera da li se korisnik ostaje na istoj stranici
        self.assertTemplateUsed(response, './autorizacija/login.html')
    
    def test_login_successful(self):
        client = Client()
        # Kreiranje korisnika
        Korisnik.objects.create(
            korisnicko_ime='testuser',
            sifra=make_password('testpassword')
        )
        # Poziv funkcije za prijavljivanje sa tačnim podacima
        request = self.factory.post(reverse('login'), {'korime': 'testuser', 'loz': 'testpassword'})
        request.session = self.client.session
        request.session['some_key'] = 'some_value'
        request.session.save()