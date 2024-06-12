# Autor: Andrija Tomić 2021/0489
import time
from django.test import TestCase, Client
from django.urls import reverse
from appblankspace.models import Korisnik,Zanr,Predlaze_Pesmu,Izvodjac,Predlaze_Izvodjaca
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.hashers import make_password
from django.test import LiveServerTestCase
 
class PredlogIzvodjacaOdbijenSeleniumTest(LiveServerTestCase):
 
    def setUp(self):
        # Kreiramo nekoliko korisnika za testiranje rang liste - ukupno 6
        
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.client = Client()
        Korisnik.objects.create(
            korisnicko_ime='korisnik22',
            sifra=make_password('korisnik22'),
            ime='Korisnik',
            prezime='2',
            tip='M',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor',
            licni_poeni=10,
            rang_poeni=5
        )
        
        Zanr.objects.create(
            id='3',
            naziv='Narodna'
        )
        self.za_brisanje = Korisnik.objects.create(
            korisnicko_ime='korisnik1',
            sifra='korisnik1',
            ime='Korisnik',
            prezime='1',
            tip='B',
            pitanje_lozinka='Primer pitanja?',
            odgovor_lozinka='Odgovor'
        )

        self.za_odbijanje=Predlaze_Izvodjaca.objects.create(
            
            ime_izvodjaca='Taylor',
            kor_id=self.za_brisanje.id,
            zan_id='3'
        )
        Predlaze_Izvodjaca.objects.create(
            
            ime_izvodjaca='Harry',
            kor_id=self.za_brisanje.id,
            zan_id='3'
        )
        Predlaze_Izvodjaca.objects.create(
            
            ime_izvodjaca='Gaga',
            kor_id=self.za_brisanje.id,
            zan_id='3'
        )
 
    def tearDown(self):
        self.browser.quit()
   
    def test_predlog_izvodjaca_odbijen(self):

        
        # login
        self.browser.get(f'{self.live_server_url}/predlozi_izvodjaca/')
        
        self.browser.find_element(By.NAME, self.za_odbijanje.ime_izvodjaca).click()

        alert = self.browser.switch_to.alert
        alert.accept()

        time.sleep(2)

        self.assertFalse(Predlaze_Izvodjaca.objects.filter(id=self.za_odbijanje.id).exists())


        

        
       

        
