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
from selenium.webdriver.common.keys import Keys

class OporavakLozinkeSeleniumTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)  # Čekanje da se elementi učitaju

        # Kreiranje korisnika za testiranje
        Korisnik.objects.create(
            korisnicko_ime='korisnik22',
            sifra=make_password('korisnik123'),
            ime='Korisnik',
            prezime='2',
            tip='S',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka=make_password('Odgovor'),
            licni_poeni=10,
            rang_poeni=5
        )

    def test_oporavak_lozinke_uloguj_se(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')
        time.sleep(1)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Uloguj se')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        time.sleep(2)
        self.assertIn('Prijava', page_source)
        time.sleep(2)

        print("TEST_OPORAVAK_LOZINKE_ULOGUJ_SE")
    
    def test_oporavak_lozinke_pravila(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')
        time.sleep(1)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Pravila igre')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Opis', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_PRAVILA")

    def test_oporavak_lozinke_uloguj_se_q(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')
        # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Uloguj se')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        time.sleep(1)
        self.assertIn('Prijava', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_ULOGUJ_SE_Q")
    
    def test_oporavak_lozinke_pravila_q(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')
        # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Pravila igre')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Opis', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_PRAVILA_q")

    def test_oporavak_lozinke_uloguj_se_n(self):
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Uloguj se')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Prijava', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_ULOGUJ_SE_N")

    def test_oporavak_lozinke_pravila_n(self):
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Pravila igre')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Opis', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_PRAVILA_N")



    

    def test_oporavak_lozinke_pocetna_n(self):
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(2)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Početna')]"))
        ).click()

        time.sleep(2)
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Igra dopunjavanja tekstova pesama', page_source)

        print("TEST_OPORAVAK_LOZINKE_POCETNA_N")

    def test_oporavak_lozinke_pocetna_q(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Početna')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Igra dopunjavanja tekstova pesama', page_source)

        print("TEST_OPORAVAK_LOZINKE_POCETNA_Q")

    
    
    def test_oporavak_lozinke_pocetna(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')
        time.sleep(1)

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Početna')]"))
        ).click()
        
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Igra dopunjavanja tekstova pesama', page_source)

        print("TEST_OPORAVAK_LOZINKE_POCETNA")
    

    def tearDown(self):
        self.browser.quit()