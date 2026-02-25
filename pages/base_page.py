from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 5)

    def open(self, url: str) -> "BasePage":
        self.driver.get(url)
        return self

    def find_el(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all_el(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_n_click(self, locator: tuple[str, str]) -> "BasePage":
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def enter_text(self, locator: tuple[str, str], text: str) -> "BasePage":
        element = self.find_el(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.find_el(locator).text

    def is_element_present(self, locator: tuple[str, str]) -> bool:
        try:
            self.find_el(locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def handle_alert(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def select_element(self, locator: tuple[str, str], text: str) -> "BasePage":
        element = self.find_el(locator)
        Select(element).select_by_visible_text(text)
        return self

    def clear_field(self, locator: tuple[str, str]) -> "BasePage":
        element = self.find_el(locator)
        element.clear()
        return self
