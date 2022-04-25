import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_username = driver.find_element(By.XPATH,
                                                  Locator.login_username)
        self.login_password = driver.find_element(By.XPATH,
                                                  Locator.login_password)
        self.login_button = driver.find_element(By.XPATH, Locator.login_button)

    def getLoginUsername(self):
        return self.login_username

    def getLoginPassword(self):
        return self.login_password

    def getLoginButton(self):
        return self.login_button


class BasicPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.index = driver.find_element(By.XPATH, Locator.index)

    def getIndex(self):
        return self.index