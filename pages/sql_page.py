import json
import os

import allure
from config.config import SQLConf
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators import SQLPageLocators as SPL


class SQLPage(BasePage):
    @allure.step("Перейти на главную страницу")
    def go_to_sql_main_page(self) -> "SQLPage":
        self.open(SQLConf.URL)
        return self

    @allure.step("Сохранить куки")
    def save_cookies(self) -> "SQLPage":
        with open(SQLConf.DEST_FILE, "w") as f:
            json.dump(self.driver.get_cookies(), f)
        return self

    @allure.step("Загрузить куки")
    def load_cookies(self) -> "SQLPage":
        with open(SQLConf.DEST_FILE, "r") as f:
            saved_cookies = json.load(f)
            self.driver.delete_all_cookies()

            for cookie in saved_cookies:
                self.driver.add_cookie(cookie)
        return self

    @allure.step("Авторизоваться")
    def login_to_sql(self) -> "SQLPage":
        if os.path.exists(SQLConf.DEST_FILE):
            self.load_cookies()
            self.driver.refresh()
        else:
            (
                self.enter_text(SPL.LOGIN, SQLConf.LOGIN)
                .enter_text(SPL.PASSWORD, SQLConf.PASSWORD)
                .find_n_click(SPL.SUBMIT)
            )
            self.save_cookies()

        return self

    @allure.step("Проверить авторизацию")
    def check_login(self) -> bool:
        return self.is_element_present(
            (By.XPATH, f"//*[contains(text(), {SQLConf.NAME})]")
        )

    @allure.step("Найти и сфокусироваться на элементе Логина")
    def find_and_focus_login(self) -> "WebElement":
        search_input = self.find_el(SPL.LOGIN)
        search_input.click()
        return search_input

    @allure.step("Убрать фокус с элемента")
    def blur_element(self, element: WebElement) -> "SQLPage":
        self.driver.execute_script("arguments[0].blur();", element)
        return self

    @allure.step("Проверить наличие фокуса на элементе")
    def check_focus(self, element: WebElement) -> bool:
        is_focused = self.driver.execute_script(
            "return document.activeElement === arguments[0];", element
        )
        return is_focused

    @allure.step("Проверить наличие вертикального скролла")
    def has_vertical_scroll(self) -> bool:
        script = "return document.documentElement.scrollHeight > window.innerHeight;"
        return self.driver.execute_script(script)
