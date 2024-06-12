#Autor: Maša Nikolić 2021/0439

import time
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.hashers import make_password
from django.test import LiveServerTestCase

class PregledRangListeViewTests(LiveServerTestCase):

    def setUp(self):
        # Kreiramo nekoliko korisnika za testiranje rang liste - ukupno 6
        Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='sifra1',
            ime='Ime1',
            prezime='Prezime1',
            tip='M',
            pitanje_lozinka='Pitanje1',
            odgovor_lozinka='Odgovor1',
            licni_poeni=100,
            rang_poeni=50
        )
        Korisnik.objects.create(
            korisnicko_ime='korisnik2',
            sifra='sifra2',
            ime='Ime2',
            prezime='Prezime2',
            tip='M',
            pitanje_lozinka='Pitanje2',
            odgovor_lozinka='Odgovor2',
            licni_poeni=200,
            rang_poeni=60
        )
        Korisnik.objects.create(
            korisnicko_ime='korisnik3',
            sifra='sifra3',
            ime='Ime3',
            prezime='Prezime3',
            tip='M',
            pitanje_lozinka='Pitanje3',
            odgovor_lozinka='Odgovor3',
            licni_poeni=150,
            rang_poeni=75
        )
        Korisnik.objects.create(
            korisnicko_ime='korisnik4',
            sifra='sifra4',
            ime='Ime4',
            prezime='Prezime4',
            tip='M',
            pitanje_lozinka='Pitanje4',
            odgovor_lozinka='Odgovor4',
            licni_poeni=80,
            rang_poeni=80
        )
        Korisnik.objects.create(
            korisnicko_ime='korisnik5',
            sifra='sifra5',
            ime='Ime5',
            prezime='Prezime5',
            tip='M',
            pitanje_lozinka='Pitanje5',
            odgovor_lozinka='Odgovor5',
            licni_poeni=120,
            rang_poeni=90
        )
        

        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        Korisnik.objects.create(
            korisnicko_ime='korisnik22',
            sifra=make_password('korisnik22'),
            ime='Korisnik',
            prezime='2',
            tip='S',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            licni_poeni=10,
            rang_poeni=5
        )

    def tearDown(self):
        self.browser.quit()
    
    def test_pregled_rang_liste(self):
        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik22')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik22')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # Dodajemo pauzu nakon logovanja
        time.sleep(2)

        # prelazak na 'Rang lista'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Rang lista')]"))
        ).click()

        # Dodajemo pauzu nakon prelaska na 'Rang lista'
        time.sleep(2)

        # Provera da li URL sadrži '/rang_lista/'
        self.assertIn('/rang_lista/', self.browser.current_url)

        # Pronalazak redova tabele sa korisnicima
        rang_list_items = self.browser.find_elements(By.XPATH, "//table/tbody/tr")

        # Provera da li su svi očekivani korisnici prikazani u rang listi
        expected_korisnici = ['korisnik1', 'korisnik2', 'korisnik3', 'korisnik4', 'korisnik5']
        print(expected_korisnici)
        found_korisnici = [item.text for item in rang_list_items]
        print(found_korisnici)

        for korisnik in expected_korisnici:
            self.assertTrue(any(korisnik in korisnik_text for korisnik_text in found_korisnici), f"Korisnik '{korisnik}' nije pronađen u rang listi")

        print("TEST_PREGLED_RANG_LISTE")

    def test_pregled_rang_liste_klik_pocetna(self):
        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik22')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik22')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # Dodajemo pauzu nakon logovanja
        time.sleep(2)

        # prelazak na 'Rang lista'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Rang lista')]"))
        ).click()

        # Dodajemo pauzu nakon prelaska na 'Rang lista'
        time.sleep(2)

        # Provera da li URL sadrži '/rang_lista/'
        self.assertIn('/rang_lista/', self.browser.current_url)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Početna')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Ulogovani ste kao', page_source)
        time.sleep(2)

        print("TEST_PREGLED_RANG_POCETNA")

    def test_pregled_rang_liste_klik_pravila(self):
        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik22')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik22')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # Dodajemo pauzu nakon logovanja
        time.sleep(2)

        # prelazak na 'Rang lista'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Rang lista')]"))
        ).click()

        # Dodajemo pauzu nakon prelaska na 'Rang lista'
        time.sleep(2)

        # Provera da li URL sadrži '/rang_lista/'
        self.assertIn('/rang_lista/', self.browser.current_url)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Pravila igre')]"))
        ).click()
        
        # Provera da li URL sadrži '/pravila_igre/'
        self.assertIn('/pravila_igre/', self.browser.current_url)
        time.sleep(2)

        print("TEST_PREGLED_RANG_PRAVILA")

    def test_pregled_rang_liste_klik_odjava(self):
        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik22')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik22')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # Dodajemo pauzu nakon logovanja
        time.sleep(2)

        # prelazak na 'Rang lista'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Rang lista')]"))
        ).click()

        # Dodajemo pauzu nakon prelaska na 'Rang lista'
        time.sleep(2)

        # Provera da li URL sadrži '/rang_lista/'
        self.assertIn('/rang_lista/', self.browser.current_url)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Izloguj se')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Igra dopunjavanja tekstova pesama', page_source)
        time.sleep(2)

        print("TEST_PREGLED_RANG_ODJAVA")