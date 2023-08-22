from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.FORM_OF_BASKET), "basket is not empty"

    def should_text_of_empy_basket_is_present(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), \
            "text of empy basket is not present"
