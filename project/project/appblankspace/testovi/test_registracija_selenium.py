#Autor: Maša Nikolić 2021/0439

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appblankspace.models import Korisnik
from django.urls import reverse
from django.contrib.auth.hashers import make_password
import time

class RegistrationSeleniumTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_registracija_correct(self):
        self.browser.get(f'{self.live_server_url}{reverse("registration")}')
        time.sleep(1)

        ime_prezime_input = self.browser.find_element(By.NAME, 'ime_prezime')
        korime_input = self.browser.find_element(By.NAME, 'korime')
        lozinka_input = self.browser.find_element(By.NAME, 'lozinka')
        plozinka_input = self.browser.find_element(By.NAME, 'plozinka')
        pitanje_input = self.browser.find_element(By.NAME, 'pitanje')
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')

        ime_prezime_input.send_keys('Zubic Vila')
        korime_input.send_keys('zubicvila')
        lozinka_input.send_keys('zubicvila123')
        plozinka_input.send_keys('zubicvila123')
        pitanje_input.send_keys("Vila?")
        odgovor_input.send_keys('zubic')
        time.sleep(2)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        page_source = self.browser.page_source
        self.assertIn('Ulogovani ste kao', page_source)

        print("TEST_REGISTRACIJA_CORRECT")

    def test_registracija_postojece(self):
        Korisnik.objects.create(
            korisnicko_ime='zubicvila',
            sifra=make_password('zubicvila123!'),
            ime='Zubic',
            prezime='Vila',
            tip='B',
            pitanje_lozinka='Vila?',
            odgovor_lozinka=make_password('zubic'),
            rang_poeni=0,
            licni_poeni=0
        )

        self.browser.get(f'{self.live_server_url}{reverse("registration")}')
        
        ime_prezime_input = self.browser.find_element(By.NAME, 'ime_prezime')
        korime_input = self.browser.find_element(By.NAME, 'korime')
        lozinka_input = self.browser.find_element(By.NAME, 'lozinka')
        plozinka_input = self.browser.find_element(By.NAME, 'plozinka')
        pitanje_input = self.browser.find_element(By.NAME, 'pitanje')
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')

        ime_prezime_input.send_keys('Zubic Vila')
        korime_input.send_keys('zubicvila')
        lozinka_input.send_keys('zubicvila123')
        plozinka_input.send_keys('zubicvila123')
        pitanje_input.send_keys("Vila?")
        odgovor_input.send_keys('zubic')
        time.sleep(2)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        page_source = self.browser.page_source
        self.assertIn('Korisnik sa tim imenom već postoji!', page_source)
        time.sleep(3)

        print("TEST_REGISTRACIJA_POSTOJECE")
    
    def test_registracija_pravila(self):
        self.browser.get(f'{self.live_server_url}{reverse("registration")}')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Pravila igre')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Opis', page_source)
        time.sleep(1)

        print("TEST_REGISTRACIJA_PRAVILA")
    
    def test_registracija_pocetna(self):
        self.browser.get(f'{self.live_server_url}{reverse("registration")}')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Početna')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Igra dopunjavanja tekstova pesama', page_source)
        time.sleep(1)

        print("TEST_REGISTRACIJA_POCETNA")
    
    def test_registracija_uloguj_se(self):
        self.browser.get(f'{self.live_server_url}{reverse("registration")}')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Uloguj se')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Prijava', page_source)
        time.sleep(1)

        print("TEST_REGISTRACIJA_PRIJAVA")