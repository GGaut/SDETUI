import time

import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BankingPageLocators as BPL


class BankingPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login"

    @allure.step("Открыть страницу меню банка")
    def go_to_banking_page(self):
        self.open(self.URL)
        return self

    # Sample form methods

    @allure.step("Перейти в меню Sample")
    def go_to_sample_tab(self):
        self.go_to_banking_page().click(BPL.BTN_SAMPLE_LOGIN)
        return self

    @allure.step("Выбрать хобби и получить самое длинное хобби")
    def calculate_longest_hobby_and_click(self):
        hobbies = self.find_all(BPL.HOBBIES)
        hobby_values = []
        for hobby in hobbies:
            value = hobby.get_attribute("value")
            if value == "Sports":
                hobby.click()
            hobby_values.append(value)
        self._longest_hobby = max(hobby_values, key=len)
        return self

    @allure.step("Заполнить sample форму")
    def fill_sample_form(self, firstname, lastname, email, password):
        (
            self.type(BPL.SMP_FIRST_NAME, firstname)
            .type(BPL.SMP_LAST_NAME, lastname)
            .type(BPL.SMP_EMAIL, email)
            .type(BPL.SMP_PASSWORD, password)
            .select_element(BPL.GENDER, "Other")
            .calculate_longest_hobby_and_click()
            .type(
                BPL.TEXTAREA,
                f"Самое длинное слово из предложенных хобби - {self._longest_hobby}",
            )
            .click(BPL.REGISTER)
        )
        return self

    @allure.step("Проверить сообщение об успехе заполнения Sample формы")
    def is_sample_success_msg(self):
        success_message = self.find(BPL.SMP_SUCCESS_MESSAGE)
        message = ""
        if success_message.value_of_css_property("display") == "block":
            message = success_message.text
        return message

    # Manager methods

    @allure.step("Перейти в меню менеджера банка")
    def go_to_manager_tab(self):
        self.go_to_banking_page().click(BPL.BTN_MANAGER_LOGIN)
        return self

    @allure.step("Добавить нового клиента")
    def add_new_customer(self, firstname, lastname, postcode):
        (
            self.click(BPL.BTN_ADD_CUST_MENU)
            .type(BPL.ADD_CUST_FORM_FIRST_N, firstname)
            .type(BPL.ADD_CUST_FORM_LAST_N, lastname)
            .type(BPL.ADD_CUST_FORM_PC, postcode)
            .click(BPL.ADD_CUST_FORM_BTN)
        )
        return self

    @allure.step("Активировать аккаунт клиента")
    def open_acc(self, firstname, lastname):
        (
            self.click(BPL.BTN_OPEN_ACC_MENU)
            .select_element(BPL.OP_CUST_FORM_USER_SELECT, f"{firstname} {lastname}")
            .select_element(BPL.OP_CUST_FORM_CURRENCY, "Dollar")
            .click(BPL.OP_CUST_FORM_PRCS_BTN)
        )
        return self

    # Customer methods

    @allure.step("Перейти в меню клиента")
    def go_to_customer_tab(self):
        self.go_to_banking_page().click(BPL.BTN_CUSTOMER_LOGIN)
        return self

    @allure.step("Авторизоваться как клиент")
    def login_as_customer(self, firstname, lastname):
        (
            self.select_element(
                BPL.OP_CUST_FORM_USER_SELECT, f"{firstname} {lastname}"
            ).click(BPL.LOGIN_BTN)
        )
        return self

    @allure.step("Проверить сообщение-приветсвие при авторизации")
    def get_welcome_msg(self):
        return self.get_text(BPL.WELCOME_MSG)

    @allure.step("Совершить транзакцию")
    def customer_deposit_withdraw(self, amount, action):
        if action == "deposit":
            (
                self.click(BPL.DEPOSIT_TAB)
                .type(BPL.AMOUNT_INP, amount)
                .click(BPL.SUBMIT_BTN)
            )
        elif action == "withdraw":
            (
                self.click(BPL.WITHDRAW_TAB)
                .type(BPL.AMOUNT_INP, amount)
                .click(BPL.SUBMIT_BTN)
            )
        time.sleep(1)
        return self

    @allure.step("Проверить сообщение об успехе/неуспехе транзакции")
    def deposit_withdraw_success_msg(self):
        try:
            msg = self.get_text(BPL.DEP_WTHDR_MSG)
            return msg
        except Exception:
            return False

    @allure.step("Проверить присутсвие транзакции в таблице")
    def is_transaction_present(self, amount):
        locator = (By.XPATH, f"//td[normalize-space()='{amount}']")
        is_trans_present = self.click(BPL.TRANS_TAB).is_element_present(locator)
        self.click(BPL.BACK_FROM_TRANS_TAB)
        return is_trans_present

    @allure.step("Получить баланс")
    def get_balance(self):
        balance = self.get_text(BPL.BALANCE).strip()
        return int(balance)

    @allure.step("Вычислить баланс по данным из таблицы")
    def calculate_balance_from_table(self):
        self.click(BPL.TRANS_TAB)
        rows = self.find_all(BPL.TRANS_ROWS)
        total = 0
        for row in rows:
            amount = int(row.find_element(By.XPATH, "./td[2]").text)
            type_t = row.find_element(By.XPATH, "./td[3]").text
            if type_t == "Credit":
                total += amount
            else:
                total -= amount
        self.click(BPL.BACK_FROM_TRANS_TAB)
        return total

    @allure.step("Очистить таблицу транзакций")
    def clear_transaction_list(self):
        self.click(BPL.TRANS_TAB).click(BPL.RESET_BTN)
        result = self.is_element_present(BPL.TRANS_ROWS)
        self.click(BPL.BACK_FROM_TRANS_TAB)
        return result

    @allure.step("Проверить присутствие клиента в таблице")
    def find_customer(self, firstname, lastname):
        self.click(BPL.BTN_SHOW_CUST_MENU)
        locator = (
            By.XPATH,
            f"//table//tbody/tr[td[contains(normalize-space(),'{firstname}')] and td[contains(normalize-space(),'{lastname}')]]",
        )
        return self.is_element_present(locator)

    @allure.step("Удалить пользователя")
    def delete_customer(self, name):
        self.click(BPL.BTN_SHOW_CUST_MENU).type(BPL.CUST_SEARCH_FIELD, name).click(
            BPL.CUST_DELETE_BTN
        ).clear_field(BPL.CUST_SEARCH_FIELD)
        return self
