from config.config import Grid
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.ie.options import Options as IeOptions
from selenium.webdriver.ie.webdriver import WebDriver as IEWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class DriverFactory:
    def __init__(self, browser_name: str, use_grid: bool = False):
        self.browser_name = browser_name.lower()
        self.use_grid = use_grid
        if use_grid:
            self.grid_url = Grid.URL

    def get_driver(self):
        options = self._get_options()

        if self.browser_name in ("chrome", "firefox", "edge"):
            options.add_argument("--headless=new")

        if self.use_grid:
            return self._init_remote_driver(options)
        return self._init_local_driver(options)

    def _get_options(self):
        if self.browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            return options

        elif self.browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            return options

        elif self.browser_name == "edge":
            options = EdgeOptions()
            options.add_argument("--window-size=1920,1080")
            return options

        elif self.browser_name == "ie":
            options = IeOptions()
            options.ignore_zoom_level = True
            # Любой адрес в интернете, чтобы обойти protected mode
            options.initial_browser_url = "https://example.com"
            return options

        raise ValueError(f"Unsupported browser: {self.browser_name}")

    def _init_local_driver(self, options):
        if self.browser_name == "chrome":
            return ChromeWebDriver(options=options)

        elif self.browser_name == "firefox":
            return FirefoxWebDriver(options=options)

        elif self.browser_name == "edge":
            return EdgeWebDriver(options=options)

        elif self.browser_name == "ie":
            return IEWebDriver(options=options)

    def _init_remote_driver(self, options):
        try:
            return RemoteWebDriver(command_executor=self.grid_url, options=options)
        except Exception as e:
            raise RuntimeError(f"Could not connect to Selenium Grid. Error: {e}")
