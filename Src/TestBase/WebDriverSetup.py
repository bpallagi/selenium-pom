import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3


class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome(r'Src\TestBase\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(800, 600)

    #    self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()