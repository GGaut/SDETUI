from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

    def open(self, url):
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(str(text))
        return self

    def get_text(self, locator):
        return self.find(locator).text

    def is_element_present(self, locator):
        try:
            self.find(locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def handle_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def select_element(self, locator, text):
        element = self.find(locator)
        Select(element).select_by_visible_text(text)
        return self

    def clear_field(self, locator):
        element = self.find(locator)
        element.clear()
        return self
