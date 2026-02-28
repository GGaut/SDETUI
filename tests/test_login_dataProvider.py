import allure
import pytest

test_data = [
    ("angular", "password", "You're logged in!!", "Success"),
    (
        "invalidUser",
        "password",
        "Username or password is incorrect",
        "Error",
    ),
    (
        "angular",
        "wrongPass",
        "Username or password is incorrect",
        "Error",
    ),
    ("", "", "", "Empty"),
]


@allure.feature("Авторизация")
@allure.story("Авторизация клиента")
@allure.title("Проверка полей и валидация входных данных")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("name, password, msg, descriptor", test_data)
def test_login_page(login_page, name, password, msg, descriptor):
    login_page.go_to_login_page()

    assert login_page.are_login_fields_present(), "Couldnt find login fields"
    if descriptor == "Success":
        sucs_msg = login_page.login(name, password).is_login_success_message()
        assert msg in sucs_msg, f"Expected {msg}, but got {sucs_msg}"
    elif descriptor == "Error":
        err_msg = login_page.login(name, password).is_login_error_message()
        assert msg in err_msg, f"Expected {msg}, but got {err_msg}"
    elif descriptor == "Empty":
        login_page.login(name, password)
        assert not login_page.is_login_enabled(), (
            "Login enabled with empty login fields"
        )
