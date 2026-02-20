import allure


@allure.feature("SQL упражнения")
@allure.story("Авторизация на сайте")
@allure.title("Проверка авторизации через форму на главной странице")
@allure.severity(allure.severity_level.CRITICAL)
def test_sql_login(sql_page):
    sql_page.go_to_sql_main_page().login_to_sql()
    assert sql_page.check_login()
