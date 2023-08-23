from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url

        assert "login" in get_url, "invalid url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not present"

    def register_new_user(self, email, password):
        input_email = self.find_element_with_EC(*LoginPageLocators.REGISTER_INPUT_EMAIL)
        input_email.send_keys(email)
        input_pass = self.find_element_with_EC(*LoginPageLocators.REGISTER_INPUT_PASS)
        input_pass.send_keys(password)
        input_pass_confirm = self.find_element_with_EC(*LoginPageLocators.REGISTER_INPUT_PASS_CONFIRM)
        input_pass_confirm.send_keys(password)
        button_register = self.find_element_with_EC(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()
