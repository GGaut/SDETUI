from selenium.webdriver.common.action_chains import ActionChains

from .base_page import BasePage
from .locators import MainPageLocators as MPL


class MainPage(BasePage):
    URL = "https://www.way2automation.com"

    def go_to_main_page(self):
        self.open(self.URL)
        return self

    def check_slider(self):
        """Слайдер не работает ни в одном браузере, это просто заглушка с предположением как должна србабатываь логика."""
        slider_content = self.find(MPL.CAROUSEL_CONT)
        next = slider_content.find_element(*MPL.CAROUSEL_NEXT)
        self.click(MPL.SLIDER_NEXT)
        orig = slider_content.find_element(*MPL.CAROUSEL_ORIG)
        return orig == next

    def navigate_to_lifetime(self):
        try:
            ActionChains(self.driver).move_to_element(
                self.find(MPL.MENU_ALL_COURSES)
            ).perform()
            self.click(MPL.MENU_LIFETIME)
            return self
        except Exception as e:
            print(f"Error navigating to lifetime membership: {e}")
            raise

    def get_current_url(self):
        return self.driver.current_url

    def get_changed_page_title(self):
        return self.get_text(MPL.PAGE_TITLE)

    def is_header_correct(self):
        header_element = self.find(MPL.HEADER_CONTACTS)

        phone_present = len(header_element.find_elements(*MPL.PHONE)) > 0
        skype_present = len(header_element.find_elements(*MPL.SKYPE)) > 0
        email_present = len(header_element.find_elements(*MPL.EMAIL)) > 0
        media_present = len(header_element.find_elements(*MPL.MEDIA)) > 0

        return phone_present and skype_present and email_present and media_present

    def get_footer_contacts(self):
        ActionChains(self.driver).move_to_element(self.find(MPL.FOOTER)).perform()

        elements = self.find_all(MPL.FOOTER_CONTACTS)
        raw_texts = [el.text.strip() for el in elements]

        cleaned = []
        for txt in raw_texts:
            parts = [p.strip() for p in txt.splitlines()]
            if parts:
                cleaned.append(parts[-1])
        return cleaned

    def is_layout_correct(self):
        return (
            self.is_element_present(MPL.HEADER_CONTACTS)
            and self.is_element_present(MPL.NAV_BLOCK)
            and self.is_element_present(MPL.FOOTER)
            and self.is_element_present(MPL.REG_BUTTON)
            and self.is_element_present(MPL.COURSE_LIST)
        )

    def is_element_in_viewport(self):
        nav_menu = self.find(MPL.NAV_BLOCK)
        ActionChains(self.driver).move_to_element(self.find(MPL.FOOTER)).perform()
        rect = self.driver.execute_script(
            "return arguments[0].getBoundingClientRect();", nav_menu
        )

        viewport_height = self.driver.execute_script("return window.innerHeight;")
        viewport_width = self.driver.execute_script("return window.innerWidth;")

        return (
            rect["top"] >= 0
            and rect["left"] >= 0
            and rect["bottom"] <= viewport_height
            and rect["right"] <= viewport_width
        )
