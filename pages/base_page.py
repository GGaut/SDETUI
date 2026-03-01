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

    def wait_n_find_element(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_n_find_all_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_n_click(self, locator: tuple[str, str]) -> "BasePage":
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def enter_text(self, locator: tuple[str, str], text: str) -> "BasePage":
        element = self.wait_n_find_element(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.wait_n_find_element(locator).text

    def is_element_present(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait_n_find_element(locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def handle_alert(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def input_alert(self, text: str) -> "BasePage":
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
        alert.accept()
        return self

    def select_element(self, locator: tuple[str, str], text: str) -> "BasePage":
        element = self.wait_n_find_element(locator)
        Select(element).select_by_visible_text(text)
        return self

    def clear_field(self, locator: tuple[str, str]) -> "BasePage":
        element = self.wait_n_find_element(locator)
        element.clear()
        return self

    def switch_to_frame(self, locator: tuple[str, str]):
        self.driver.switch_to.default_content()
        iframe = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.switch_to.frame(iframe)
        return self

    def switch_to_window(self, window_index: int):
        current_handle = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > window_index)
        for handle in self.driver.window_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break
        return self

    def get_tabs_count(self) -> int:
        return len(self.driver.window_handles)
