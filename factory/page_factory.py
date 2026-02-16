from pages.banking_page import BankingPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class PageFactory:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.banking_page = BankingPage(driver)
