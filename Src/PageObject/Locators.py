class Locator(object):
    login_username = "//input[@id='user-name']"
    login_password = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    product_backpack = "//button[@id='add-to-cart-sauce-labs-backpack']"
    product_redtshirt = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"
    cart_button = "//DIV[@class='app_logo']/../..//A[@class='shopping_cart_link']"
    product_dd_locator = "//DIV[@class='inventory_item_name'][text()='Sauce Labs Backpack']/../../..//BUTTON[@id='add-to-cart-sauce-labs-backpack']"