import allure

from SDETUI.config.config import JqueryPagesConf as JPC
from SDETUI.pages.base_page import BasePage
from SDETUI.pages.locators import JqueryPagesLocators as JPL


class AlertPage(BasePage):
    @allure.step("Открыть страницу с алертом")
    def go_to_alert_page(self) -> "AlertPage":
        self.open(JPC.ALERT_URL)
        return self

    @allure.step("Нажать на кнопку алерта")
    def click_alert_btn(self) -> "AlertPage":
        (
            self.find_n_click(JPL.INPUT_ALERT_BTN)
            .switch_to_frame(JPL.ALRT_IFRAME)
            .find_n_click(JPL.ALRT_BTN)
        )
        return self

    @allure.step("Ввести текст в поле алерта")
    def fill_alert_txt(self, text) -> "AlertPage":
        self.input_alert(text)
        return self

    @allure.step("Проверить сообщение")
    def check_message(self) -> str:
        message = self.get_text(JPL.ALRT_AFTERMESSAGE)
        return message
