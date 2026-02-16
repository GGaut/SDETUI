from .base_page import BasePage
from .locators import LoginPageLocators as LP


class LoginPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    def go_to_login_page(self):
        self.open(self.URL)
        return self

    def login(self, user, pwd):
        (
            self.type(LP.USERNAME, user)
            .type(LP.PASSWORD, pwd)
            .type(LP.USERNAME_DESCRIPTION, "Description")
            .find(LP.LOGIN_BTN)
            .click()
        )
        return self

    def logout(self):
        self.click(LP.LOGOUT_BTN)
        return self

    def are_login_fields_present(self):
        return (
            self.is_element_present(LP.USERNAME)
            and self.is_element_present(LP.PASSWORD)
            and self.is_element_present(LP.USERNAME_DESCRIPTION)
        )

    def is_login_enabled(self):
        btn = self.find(LP.LOGIN_BTN)
        return btn.is_enabled()

    def is_login_success_message(self):
        return self.get_text(LP.STATUS_MSG)

    def is_login_error_message(self):
        return self.get_text(LP.ERROR_LOGIN_MSG)
