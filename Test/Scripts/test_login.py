import sys

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import LoginPage
from Src.TestBase.keywords import custom_click


class login(WebDriverSetup):

    def test_login(self):

        driver = self.driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_page_load_timeout(30)

        #for methods
        loginPage = LoginPage(driver)
        loginPage.getLoginUsername().send_keys("standard_user")
        sleep(5)
        loginPage.getLoginPassword().send_keys("secret_sauce")
        sleep(5)
        custom_click(loginPage.getLoginButton())
        sleep(10)


if __name__ == '__main__':
    unittest.main()