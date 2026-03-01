import allure

from SDETUI.config.config import LoginPageConf
from SDETUI.pages.base_page import BasePage
from SDETUI.pages.locators import LoginPageLocators as LP


class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def go_to_login_page(self) -> "LoginPage":
        self.open(LoginPageConf.URL)
        return self

    @allure.step("Авторизоваться")
    def login(self, user: str, pwd: str) -> "LoginPage":
        (
            self.clear_field(LP.USERNAME)
            .enter_text(LP.USERNAME, user)
            .clear_field(LP.PASSWORD)
            .enter_text(LP.PASSWORD, pwd)
            .enter_text(LP.USERNAME_DESCRIPTION, "Description")
            .wait_n_find_element(LP.LOGIN_BTN)
            .click()
        )
        return self

    @allure.step("Деавторизоваться")
    def logout(self) -> "LoginPage":
        self.find_n_click(LP.LOGOUT_BTN)
        return self

    @allure.step("Проверить наличие элементов логин/пароль/описание")
    def are_login_fields_present(self) -> bool:
        return (
            self.is_element_present(LP.USERNAME)
            and self.is_element_present(LP.PASSWORD)
            and self.is_element_present(LP.USERNAME_DESCRIPTION)
        )

    @allure.step("Проверить состояние кнопки Login")
    def is_login_enabled(self) -> bool:
        btn = self.wait_n_find_element(LP.LOGIN_BTN)
        return btn.is_enabled()

    @allure.step("Получить текст сообщения об успехе авторизации")
    def is_login_success_message(self) -> str:
        return self.get_text(LP.STATUS_MSG)

    @allure.step("Получить текст сообщения об ошибке авторизации")
    def is_login_error_message(self) -> str:
        return self.get_text(LP.ERROR_LOGIN_MSG)
