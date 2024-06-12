# Autor: Jana Stanisavljević 2021/0381
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from django.core.management import call_command
from appblankspace.models import Korisnik
from django.contrib.auth.hashers import make_password


class UklanjanjeKorisnikaSeleniumTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.admin = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra=make_password('korisnik1'),
            ime='Korisnik',
            prezime='1',
            tip='A',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            )
        self.test_user = Korisnik.objects.create(
            korisnicko_ime='korisnik2',
            sifra=make_password('korisnik2'),
            ime='Korisnik',
            prezime='2',
            tip='S',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            licni_poeni=10,
            rang_poeni=5
            )
        #call_command('collectstatic', interactive=False)


    def tearDown(self):
        self.browser.quit()


    def test_uklanjanje_korisnika_odbij(self):
        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik1')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik1')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # prelazak na 'Ukloni korisnike'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Ukloni korisnike')]"))).click()
        
        # klik na 'Ukloni' i 'Cancel' kad iskoci alert
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Ukloni')]"))).click()
        alert = self.browser.switch_to.alert
        alert.dismiss()

        # Ukloni sa razmakom je za dugme
        self.assertIn('Ukloni ', self.browser.page_source)


    def test_uklanjanje_korisnika_prihvati(self):
        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik1')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik1')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # prelazak na 'Ukloni korisnike'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Ukloni korisnike')]"))).click()
        
        # klik na 'Ukloni' i 'Cancel' kad iskoci alert
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Ukloni')]"))).click()
        alert = self.browser.switch_to.alert
        alert.accept()

         # Ukloni sa razmakom je za dugme
        self.assertNotIn('Ukloni ', self.browser.page_source)


    def test_uklanjanje_korisnika_nema_korisnika(self):
        # brise korisnika
        korisnik=Korisnik.objects.filter(korisnicko_ime='korisnik2')
        korisnik.delete()

        # login
        self.browser.get(f'{self.live_server_url}/login/')
        username_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'korime'))
        )
        username_input.send_keys('korisnik1')
        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.NAME, 'loz'))
        )
        password_input.send_keys('korisnik1')
        self.browser.find_element(By.CLASS_NAME, 'submit').click()

        # prelazak na 'Ukloni korisnike'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Ukloni korisnike')]"))).click()
        
         # Ukloni sa razmakom je za dugme
        self.assertNotIn('Ukloni ', self.browser.page_source)
