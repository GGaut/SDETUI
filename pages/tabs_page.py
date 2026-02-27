import allure
from config.config import JqueryPagesConf

from .base_page import BasePage
from .locators import JqueryPagesLocators as JPL


class TabsPage(BasePage):
    @allure.step("Открыть страницу Tabs")
    def got_to_tabs_page(self) -> "TabsPage":
        self.open(JqueryPagesConf.TABS_URL)
        return self

    @allure.step("Нажать на ссылку во фрейме")
    def click_new_tab_link(self):
        self.switch_to_frame(JPL.TABS_BTN_FRAME)
        self.find_n_click(JPL.TAB_LINK)
        self.driver.switch_to.default_content()
        return self

    @allure.step("Нажать на ссылку на новой вкладке")
    def click_link_on_second_tab(self):
        self.switch_to_window(1)
        self.find_n_click(JPL.TAB_LINK)
        return self
