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


class ShopPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.product_backpack = driver.find_element(By.XPATH,
                                                    Locator.product_backpack)
        self.product_bikelight = driver.find_element(By.XPATH,
                                                     Locator.product_backpack)
        self.product_redtshirt = driver.find_element(By.XPATH,
                                                     Locator.product_redtshirt)
        self.cart_button = driver.find_element(By.XPATH, Locator.cart_button)

    def getProduct_Backpack(self):
        return self.product_backpack

    def getProduct_RedTShirt(self):
        return self.product_redtshirt

    def getCart_Button(self):
        return self.cart_button


class ShopPage_DD(object):

    def __init__(self, driver, string):
        self.driver = driver
        self.product = driver.find_element(By.XPATH, string)

    def getProduct(self, string):
        return self.product