import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.search_text = driver.find_element(By.XPATH, Locator.search_text)
        self.basic_web_page = driver.find_element(By.XPATH,
                                                  Locator.basic_web_page)

    def getSearchText(self):
        return self.search_text

    def getBasic(self):
        return self.basic_web_page


class BasicPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.index = driver.find_element(By.XPATH, Locator.index)

    def getIndex(self):
        return self.index