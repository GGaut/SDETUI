import allure
from config.config import JqueryPagesConf as JPC

from .base_page import BasePage
from .locators import JqueryPagesLocators as JPL


class AuthPage(BasePage):
    @allure.step("Открыть страницу с Basic Authentication")
    def go_to_auth_page(self) -> "AuthPage":
        self.open(JPC.AUTH_URL)
        return self

    @allure.step("Установить данные для авторизации и нажать кнопку")
    def login_and_display_image(self, username, password) -> "AuthPage":
        self.driver.network.add_auth_handler(username, password)
        self.find_n_click(JPL.DISPLAY_IMAGE_BUTTON)
        return self

    @allure.step("Проверить успешность аутентификации")
    def is_image_displayed(self) -> bool:
        return self.is_element_present(JPL.AUTHENTICATED_IMAGE)
