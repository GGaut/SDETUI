import allure

from SDETUI.config.config import JqueryPagesConf as JPC
from SDETUI.pages.base_page import BasePage
from SDETUI.pages.locators import JqueryPagesLocators as JPL


class AuthPage(BasePage):
    @allure.step("Открыть страницу с Basic Authentication")
    def go_to_auth_page(self) -> "AuthPage":
        self.open(JPC.AUTH_URL)
        return self

    @allure.step("Установить данные для аутентификации и нажать кнопку Display Image")
    def setup_auth_data_n_click_display(
        self, username: str, password: str
    ) -> "AuthPage":
        self.driver.network.add_auth_handler(username, password)
        self.find_n_click(JPL.DISPLAY_IMAGE_BUTTON)
        return self

    @allure.step("Проверить успешность аутентификации")
    def is_image_displayed(self) -> bool:
        return self.is_element_present(JPL.AUTHENTICATED_IMAGE)
