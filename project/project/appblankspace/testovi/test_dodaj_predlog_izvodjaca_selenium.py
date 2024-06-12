# Autor: Andrija Tomić 2021/0489
import time
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik,Zanr,Predlaze_Izvodjaca
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.hashers import make_password
from django.test import LiveServerTestCase
 
class PredlogIzvodjacaSeleniumTest(LiveServerTestCase):
 
    def setUp(self):
        # Kreiramo nekoliko korisnika za testiranje rang liste - ukupno 6
        
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

        Zanr.objects.create(
            id='1',
            naziv='Pop Strani'
        )

        Zanr.objects.create(
            id='2',
            naziv='Pop Domaci'
        )
        Zanr.objects.create(
            id='3',
            naziv='Narodna'
        )

        Zanr.objects.create(
            id='4',
            naziv='Folk'
        )
        Zanr.objects.create(
            id='5',
            naziv='Rep'
        )
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

        #time.sleep(5)


        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Predloži izvođača')]"))).click()
        
        zanr_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='radio'][value='3']"))
        )

        zanr_input.click()

        password_input = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'ime'))
        )
        password_input.send_keys('andrija')

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Predloži')]"))).click()


        self.assertTrue(Predlaze_Izvodjaca.objects.filter(ime_izvodjaca='andrija').exists())

        
        #time.sleep(20)

        
