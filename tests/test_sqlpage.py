import allure


@allure.feature("SQL упражнения")
@allure.story("Авторизация на сайте")
@allure.title("Проверка авторизации через форму на главной странице")
@allure.severity(allure.severity_level.CRITICAL)
def test_sql_login(sql_page):
    sql_page.go_to_sql_main_page().login_to_sql()
    assert sql_page.check_login(), "Failed to log in"


@allure.feature("JavaScriptExecutor функции")
@allure.story("Управление фокусом и проверка скролла")
@allure.title("Проверка функций фокуса и скролла")
@allure.severity(allure.severity_level.MINOR)
def test_jve_func(sql_page):
    login = sql_page.go_to_sql_main_page().find_and_focus_login()
    assert not sql_page.blur_element(login).check_focus(login), "Element still in focus"

    assert sql_page.has_vertical_scroll(), "There is no vertical scroll"
