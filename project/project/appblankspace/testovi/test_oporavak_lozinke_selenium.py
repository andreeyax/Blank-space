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

    def test_oporavak_lozinke_correct(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(0.5)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(0.5)

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")


        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('novaLozinka123')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('novaLozinka123')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Ulogovani ste kao', page_source)

        print("TEST_OPORAVAK_LOZINKE_CORRECT")

    def test_oporavak_lozinke_bar_1_broj(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")


        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('novaLozinka')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('novaLozinka')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na potvrdu o uspešno postavljenoj lozinci
        page_source = self.browser.page_source
        self.assertIn('Lozinka mora imati bar jedan broj!', page_source)

        print("TEST_OPORAVAK_LOZINKE_BAR_1_BROJ")
    
    def test_oporavak_lozinke_lozinke_nisu_iste(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")


        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('novaLozinka')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('novaLozinka12')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na potvrdu o uspešno postavljenoj lozinci
        page_source = self.browser.page_source
        self.assertIn('Lozinke se ne poklapaju!', page_source)

        print("TEST_OPORAVAK_LOZINKE_LOZINKE_NISU_ISTE")

    def test_oporavak_lozinke_lozinke_bar_1_slovo(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('123')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('123')

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na potvrdu o uspešno postavljenoj lozinci
        page_source = self.browser.page_source
        self.assertIn('Lozinka mora imati bar jedno slovo!', page_source)

        print("TEST_OPORAVAK_LOZINKE_BAR_1_SLOVO")
    
    def test_oporavak_lozinke_lozinke_duza_od_5(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('123as')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('123as')
        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na potvrdu o uspešno postavljenoj lozinci
        page_source = self.browser.page_source
        self.assertIn('Lozinka mora biti duza od 5 karaktera!', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_DUZE_OD_5")

    def test_oporavak_lozinke_lozinke_lozinka_je_4(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('12as')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('12as')
        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na potvrdu o uspešno postavljenoj lozinci
        page_source = self.browser.page_source
        self.assertIn('Lozinka mora biti duza od 5 karaktera!', page_source)
        time.sleep(1)

        print("TEST_OPORAVAK_LOZINKE_LOZINKA_JE_4")

    def test_oporavak_lozinke_lozinke_lozinka_je_6(self):
        # Otvaranje stranice za oporavak lozinke
        self.browser.get(self.live_server_url + '/forgotpass')

       # Unos korisničkog imena
        korisnicko_ime_input = self.browser.find_element(By.NAME, 'korime')
        korisnicko_ime_input.send_keys('korisnik22')

        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        # Čekanje na pojavljivanje polja za odgovor na sigurnosno pitanje
        odgovor_input = self.browser.find_element(By.NAME, 'odgovor')
        self.assertTrue(odgovor_input.is_displayed())

        if odgovor_input.is_enabled() and odgovor_input.is_displayed():
            odgovor_input.send_keys('Odgovor')
        else:
            print("Polje za unos nije omogućeno ili vidljivo.")

        time.sleep(1)

        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        time.sleep(1)

        # Čekanje na pojavljivanje polja za postavljanje nove lozinke
        nova_lozinka_input = self.browser.find_element(By.NAME, 'lozinka1')
        self.assertTrue(nova_lozinka_input.is_displayed())

        # Unos nove lozinke
        nova_lozinka_input.send_keys('123asb')
        nova_lozinka_potvrda_input = self.browser.find_element(By.NAME, 'lozinka2')
        nova_lozinka_potvrda_input.send_keys('123asb')
        time.sleep(1)

        # Klik na dugme za slanje
        submit_button = self.browser.find_element(By.CLASS_NAME, 'submit')
        submit_button.click()

        
        time.sleep(1)
        # Provera da li smo se vratili na pocetnu
        page_source = self.browser.page_source
        self.assertIn('Ulogovani ste kao', page_source)

        print("TEST_OPORAVAK_LOZINKE_LOZINKA_JE_6")


        

    def tearDown(self):
        self.browser.quit()