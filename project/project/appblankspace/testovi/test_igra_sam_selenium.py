import time
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By

class IgraSamSeleniumTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window
    

    def test_izbor_zanra_nijedan_selenium(self):
        self.browser.get(self.live_server_url + '/')
        dugme = self.browser.find_element(By.XPATH, '//button[text() = "Igraj sam"]')
        dugme.click()
        time.sleep(2)
        dugme = self.browser.find_element(By.XPATH, '//button[text() = "Normal"]')
        dugme.click()
        dugme = self.browser.find_element(By.XPATH, '//button[text() = "Dalje"]')
        dugme.click()
        poruka = self.browser.find_element(By.ID, 'porukagreska')
        self.assertEqual(poruka.text, 'Niste izabrali nijedan žanr')
    