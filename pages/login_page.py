from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/","Wrong login url"
        # assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def go_to_login_page(self):
         link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
         link.click()
        #  return LoginPage(browser=self.browser, url=self.browser.current_url) 
