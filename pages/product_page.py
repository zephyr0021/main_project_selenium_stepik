from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        add_cart_button = self.find_element_with_EC(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_cart_button.click()

    def should_right_title_product_in_cart(self):
        assert f"{self.get_text_from_element(*ProductPageLocators.PRODUCT_TITLE)} has been added to your basket." == \
               self.get_text_from_element(*ProductPageLocators.MODAL_PRODUCT_ADDED_TO_CART), \
            "wrong product title"

    def should_right_price_product_in_cart(self):
        assert f"Your basket total is now {self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)}" ==\
               self.get_text_from_element(*ProductPageLocators.MODAL_PRICE_OF_PRODUCT_IN_CART), \
            "wrong product price"
