from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MODAL_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner")
    MODAL_PRICE_OF_PRODUCT_IN_CART = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p")
