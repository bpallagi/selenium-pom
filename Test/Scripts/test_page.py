import sys

sys.path.append(sys.path[0] + "/...")
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest
from selenium import webdriver
from time import sleep


class page(WebDriverSetup):

    def test_page(self):
        driver = self.driver
        self.driver.get("https://testpages.herokuapp.com/")
        self.driver.set_page_load_timeout(30)

        web_page_title = "Selenium Test Pages"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        # for methods
        chill = sleep(2)
        home = Home(driver)
        chill
        home.getSearchText().find_element


if __name__ == '__main__':
    unittest.main()