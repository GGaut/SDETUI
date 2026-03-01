from SDETUI.pages.alert_page import AlertPage
from SDETUI.pages.auth_page import AuthPage
from SDETUI.pages.banking_page import BankingPage
from SDETUI.pages.dragndrop_page import DNDPage
from SDETUI.pages.login_page import LoginPage
from SDETUI.pages.main_page import MainPage
from SDETUI.pages.sql_page import SQLPage
from SDETUI.pages.tabs_page import TabsPage


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
