import allure
from config.config import JqueryPagesConf
from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage
from .locators import JqueryPagesLocators as JPL


class DNDPage(BasePage):
    @allure.step("Открыть страницу drag and drop")
    def go_to_dnd_page(self) -> "DNDPage":
        self.open(JqueryPagesConf.DROP_URL)
        return self

    @allure.step("Перетащить элемент из drag в drop")
    def drag_n_drop(self) -> "DNDPage":
        self.switch_to_frame(JPL.DND_IFRAME)
        drag = self.find_el(JPL.DRAGGABLE)
        drop = self.find_el(JPL.DROPPABLE)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        return self

    @allure.step("Получить текст drop элемента")
    def check_drop_text(self):
        text = self.get_text(JPL.DROP_TEXT)
        return text
