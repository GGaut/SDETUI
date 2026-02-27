from pages.alert_page import AlertPage
from pages.auth_page import AuthPage
from pages.banking_page import BankingPage
from pages.dragndrop_page import DNDPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sql_page import SQLPage
from pages.tabs_page import TabsPage


class PageFactory:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.banking_page = BankingPage(driver)
        self.sql_page = SQLPage(driver)
        self.dnd_page = DNDPage(driver)
        self.tabs_page = TabsPage(driver)
        self.alert_page = AlertPage(driver)
        self.auth_page = AuthPage(driver)
