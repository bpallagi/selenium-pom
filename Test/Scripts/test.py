import sys
import csv
import time

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.by import By
from Src.PageObject.Pages.HomePage import LoginPage
from Src.PageObject.Pages.HomePage import ShopPage
from Src.PageObject.Pages.HomePage import ShopPage_DD
from ddt import ddt, data, unpack


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


@ddt
class shopping(WebDriverSetup):

    def custom_click(driver, element, Y_coordinate=0):
        scrshot_name = int(round(time.time() * 1000))
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (driver.execute_script('return window.innerHeight') /
                     2) + driver.execute_script('return window.pageYOffset')
        scroll_y_by = desired_y - current_y + Y_coordinate
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        element.click()
        driver.get_screenshot_as_file("Test/TestSuite/screenshots/" +
                                      str(scrshot_name) + ".png")

    @data(*get_data('Test\Scripts\products.csv'))
    @unpack
    def test_login(self, item, price, xpath, username, password):
        scrshot_name = int(round(time.time() * 1000))
        driver = self.driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_page_load_timeout(30)

        try:

            loginPage = LoginPage(driver)
            shopping.custom_click(driver, loginPage.getLoginUsername(), 1)
            loginPage.getLoginUsername().send_keys(username)
            sleep(3)
            shopping.custom_click(driver, loginPage.getLoginPassword(), 1)
            loginPage.getLoginPassword().send_keys(password)
            sleep(3)
            shopping.custom_click(driver, loginPage.getLoginButton(), 1)
            sleep(3)
            loginPage.driver.get_screenshot_as_file(
                "Test/TestSuite/screenshots/" + str(scrshot_name) + ".png")

            shopPage = ShopPage(driver)

            shopping.custom_click(driver, shopPage.getProduct_Backpack(), 1)
            sleep(3)
            shopping.custom_click(driver, shopPage.getProduct_RedTShirt(), 1)
            sleep(3)
            shopping.custom_click(driver, shopPage.getCart_Button(), 1)
            loginPage.driver.get_screenshot_as_file(
                "Test/TestSuite/screenshots/" + str(scrshot_name) + ".png")
            sleep(10)

        except Exception as error:
            print(str(error) + "ERROR")
            loginPage.driver.get_screenshot_as_file(
                "Test/TestSuite/screenshots/" + "ERROR" + str(scrshot_name) +
                ".png")


if __name__ == '__main__':
    unittest.main()