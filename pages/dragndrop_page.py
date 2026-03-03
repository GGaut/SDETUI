import allure
from selenium.webdriver.common.action_chains import ActionChains

from SDETUI.config.config import JqueryPagesConf
from SDETUI.pages.base_page import BasePage
from SDETUI.pages.locators import JqueryPagesLocators as JPL


class DNDPage(BasePage):
    @allure.step("Открыть страницу drag and drop")
    def go_to_dnd_page(self) -> "DNDPage":
        self.open(JqueryPagesConf.DROP_URL)
        return self

    @allure.step("Перетащить элемент из drag в drop")
    def drag_n_drop(self) -> "DNDPage":
        self.switch_to_frame(JPL.DND_IFRAME)
        drag = self.wait_n_find_element(JPL.DRAGGABLE)
        drop = self.wait_n_find_element(JPL.DROPPABLE)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        return self

    @allure.step("Получить текст drop элемента")
    def check_drop_text(self) -> str:
        self.switch_to_frame(JPL.DND_IFRAME)
        text = self.get_text(JPL.DROP_TEXT)
        return text
