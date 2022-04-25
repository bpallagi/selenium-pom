#
#Custom Click action for testing
#
#Scroll to the element before every click action
#Scroll to the element with an offset possibility to ‘Y’ direction

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def custom_click(element, Y_coordinate=0):
    element.click()