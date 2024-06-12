# Autor: Jana Stanisavljević 2021/0381
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from django.core.management import call_command
from appblankspace.models import Korisnik
from django.contrib.auth.hashers import make_password


class PregledProfilaSeleniumTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.test_user = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra=make_password('korisnik1'),
            ime='Korisnik',
            prezime='1',
            tip='M',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            licni_poeni=100,
            rang_poeni=50
            )
        #call_command('collectstatic', interactive=False)

    def tearDown(self):
        self.browser.quit()


    def test_pregled_profila_selenium(self):
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

        # prelazak na 'Moj profil'
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Moj profil')]"))).click()
        self.assertIn('Pregled profila', self.browser.page_source)
