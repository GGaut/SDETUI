import pytest
from factory.page_factory import PageFactory
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.quit()


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
