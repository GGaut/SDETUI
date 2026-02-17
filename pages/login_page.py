import allure

from .base_page import BasePage
from .locators import LoginPageLocators as LP


class LoginPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    @allure.step("Открыть страницу авторизации")
    def go_to_login_page(self):
        self.open(self.URL)
        return self

    @allure.step("Авторизоваться")
    def login(self, user, pwd):
        (
            self.type(LP.USERNAME, user)
            .type(LP.PASSWORD, pwd)
            .type(LP.USERNAME_DESCRIPTION, "Description")
            .find(LP.LOGIN_BTN)
            .click()
        )
        return self

    @allure.step("Деавторизоваться")
    def logout(self):
        self.click(LP.LOGOUT_BTN)
        return self

    @allure.step("Проверить наличие элементов логин/пароль/описание")
    def are_login_fields_present(self):
        return (
            self.is_element_present(LP.USERNAME)
            and self.is_element_present(LP.PASSWORD)
            and self.is_element_present(LP.USERNAME_DESCRIPTION)
        )

    @allure.step("Проверить состояние кнопки Login")
    def is_login_enabled(self):
        btn = self.find(LP.LOGIN_BTN)
        return btn.is_enabled()

    @allure.step("Получить текст сообщения об успехе авторизации")
    def is_login_success_message(self):
        return self.get_text(LP.STATUS_MSG)

    @allure.step("Получить текст сообщения об ошибке авторизации")
    def is_login_error_message(self):
        return self.get_text(LP.ERROR_LOGIN_MSG)
