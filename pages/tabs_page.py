from enum import IntEnum

import allure

from SDETUI.config.config import JqueryPagesConf
from SDETUI.pages.base_page import BasePage
from SDETUI.pages.locators import JqueryPagesLocators as JPL


class TabsNumber(IntEnum):
    FIRST = 0
    SECOND = 1


class TabsPage(BasePage):
    @allure.step("Открыть страницу Tabs")
    def go_to_tabs_page(self) -> "TabsPage":
        self.open(JqueryPagesConf.TABS_URL)
        return self

    @allure.step("Нажать на ссылку во фрейме и открыть новую вкладку")
    def click_new_tab_link(self):
        self.switch_to_frame(JPL.TABS_BTN_FRAME)
        self.find_n_click(JPL.TAB_LINK)
        self.driver.switch_to.default_content()
        return self

    @allure.step("Нажать на ссылку на новой вкладке")
    def click_link_on_second_tab(self):
        self.switch_to_window(TabsNumber.SECOND)
        self.find_n_click(JPL.TAB_LINK)
        return self
