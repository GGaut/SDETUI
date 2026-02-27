import allure
import pytest


@allure.feature("Функции страниц")
@allure.story("Drag and drop")
@allure.title("Проверка функции drag and drop")
@allure.severity(allure.severity_level.NORMAL)
def test_drag_n_drop(dnd_page):
    text = dnd_page.go_to_dnd_page().drag_n_drop().check_drop_text()
    assert text == "Dropped!", f"Expected changed text 'Dropped!', but got {text}"


@allure.feature("Функции страниц")
@allure.story("Вкладки")
@allure.title("Проверка открытия трех вкладок")
@allure.severity(allure.severity_level.NORMAL)
def test_three_tabs(tabs_page):
    tabs_page.got_to_tabs_page().click_new_tab_link().click_link_on_second_tab()

    tabs_count = tabs_page.get_tabs_count()

    assert tabs_count == 3, f"Expected 3 tabs, but got {tabs_count}"


@allure.feature("Функции страниц")
@allure.story("Alert")
@allure.title("Проверка функций alert")
@allure.severity(allure.severity_level.NORMAL)
def test_alert(alert_page):
    text = "Ivan Ivanov"
    message = (
        alert_page.got_to_alert_page()
        .click_alert_btn()
        .fill_alert_txt(text)
        .check_message()
    )
    assert text in message, (
        f"Expected text '{text}' is not in the final message:'{message}'."
    )


@allure.feature("Функции страниц")
@allure.story("Basic Authentication")
@allure.title("Проверка функций Basic Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("driver", [True], indirect=True)
def test_basic_auth(auth_page):
    login = "httpwatch"
    pswd = "httpwatch"
    assert (
        auth_page.go_to_auth_page()
        .login_and_display_image(login, pswd)
        .is_image_displayed()
    ), "Authentication failed"
