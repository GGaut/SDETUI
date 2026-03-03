import allure
import pytest
from selenium.common.exceptions import WebDriverException

from SDETUI.factory.driver_factory import DriverFactory
from SDETUI.factory.page_factory import PageFactory


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser (chrome, firefox, edge, ie)",
    )
    parser.addoption("--local", action="store_true", help="Local run")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    is_local = request.config.getoption("--local")
    enable_bidi = getattr(request, "param", False)

    factory = DriverFactory(
        browser_name=browser, use_grid=not is_local, enable_bidi=enable_bidi
    )
    driver_instance = factory.get_driver()

    if driver_instance is None:
        pytest.fail("Couldn`t create WebDriver")
    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    return PageFactory(driver).main_page


@pytest.fixture(scope="function")
def login_page(driver):
    return PageFactory(driver).login_page


@pytest.fixture(scope="function")
def banking_page(driver):
    return PageFactory(driver).banking_page


@pytest.fixture(scope="function")
def sql_page(driver):
    return PageFactory(driver).sql_page


@pytest.fixture(scope="function")
def dnd_page(driver):
    return PageFactory(driver).dnd_page


@pytest.fixture(scope="function")
def tabs_page(driver):
    return PageFactory(driver).tabs_page


@pytest.fixture(scope="function")
def alert_page(driver):
    return PageFactory(driver).alert_page


@pytest.fixture(scope="function")
def auth_page(driver):
    return PageFactory(driver).auth_page


@pytest.fixture(scope="function")
def banking_test_data():
    return {
        "firstname": "firstName",
        "lastname": "lastName",
        "email": "user@example.com",
        "password": "password",
        "postcode": "12345",
    }


@pytest.fixture(scope="function")
def banking_page_prepared(banking_page, banking_test_data):
    data = banking_test_data
    banking_page.go_to_manager_tab().add_new_customer(
        data["firstname"], data["lastname"], data["postcode"]
    ).handle_alert()
    banking_page.open_acc(data["firstname"], data["lastname"]).handle_alert()
    banking_page.go_to_customer_tab().login_as_customer(
        data["firstname"], data["lastname"]
    )

    return banking_page


@pytest.fixture(scope="function")
def banking_page_with_deposit(banking_page_prepared):
    banking_page = banking_page_prepared
    deposit_amount = 100321
    banking_page.customer_deposit_withdraw(deposit_amount, "deposit")
    return banking_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")

        if driver_fixture:
            try:
                screenshot = driver_fixture.get_screenshot_as_png()

                allure.attach(
                    screenshot,
                    name=f"screenshot_{item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )
            except WebDriverException as e:
                print(f"Не удалось сделать скриншот: {e}")
