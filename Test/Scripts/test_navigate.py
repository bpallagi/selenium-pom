import sys

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
from Src.PageObject.Pages.HomePage import BasicPage


class navigate(WebDriverSetup):

    def test_navigate(self):

        driver = self.driver
        self.driver.get("https://testpages.herokuapp.com/")
        self.driver.set_page_load_timeout(30)

        #for methods
        home = Home(driver)
        home.getBasic().click()

        basic = BasicPage(driver)
        sleep(5)
        basic.getIndex().click()
        sleep(5)


if __name__ == '__main__':
    unittest.main()