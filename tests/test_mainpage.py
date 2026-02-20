import random

import allure


@allure.feature("Главная страница")
@allure.story("Визуальное отображение главной страницы")
@allure.title("Проверка корректности главной страницы и данных в футере и хедере")
@allure.severity(allure.severity_level.NORMAL)
def test_mainpage(main_page):
    main_page.go_to_main_page()

    assert main_page.is_layout_correct()
    assert main_page.is_header_correct()

    current_footer_contacts = main_page.get_footer_contacts()
    target_footer_contacts = [
        "CDR Complex, 3rd Floor, Naya Bans Market, Sector 15, Noida, Near sec-16 Metro Station",
        "+91 97111-11-558",
        "+91 97111-91-558",
        "trainer@way2automation.com",
        "seleniumcoaching@gmail.com",
    ]
    for contact in target_footer_contacts:
        assert contact in current_footer_contacts, f"'{contact}' not in the footer"


@allure.feature("Главная страница")
@allure.story("Навигационное меню")
@allure.title("Проверка видимости липкого меню навигации")
@allure.severity(allure.severity_level.MINOR)
def test_sticky_menu(main_page):
    main_page.go_to_main_page()
    assert main_page.is_element_in_viewport(), (
        "The element stops being visible after scrolling the page."
    )


@allure.feature("Навигация")
@allure.story("Пожизненное членство")
@allure.title("Переход на страницу LIFETIME MEMBERSHIP CLUB")
@allure.severity(allure.severity_level.NORMAL)
def test_navigate_to_lifetime_membership(main_page):
    main_page.go_to_main_page()

    original_url = main_page.get_current_url()
    main_page.navigate_to_lifetime()
    main_page.wait.until(lambda driver: driver.current_url != original_url)
    new_url = main_page.get_current_url()
    assert "lifetime-membership-club" in new_url, (
        f"Not on lifetime membership page. Current URL: {new_url}"
    )

    page_title = main_page.get_changed_page_title()
    expected_title_content = "LIFETIME MEMBERSHIP CLUB"
    assert expected_title_content in page_title.upper(), (
        f"Expected '{expected_title_content}' in page title, got: {page_title}"
    )


@allure.feature("Авторизация")
@allure.story("Авторизация клиента")
@allure.title("Проверка полей и возможности авторизации клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_page(login_page):
    login_page.go_to_login_page()

    assert login_page.are_login_fields_present(), "Couldnt find login fields"
    assert not login_page.is_login_enabled(), "Login enabled with empty login fields"

    exp_err_msg = "Username or password is incorrect"
    exp_sucs_msg = "You're logged in!!"
    err_msg = login_page.login("invalid", "invalid").is_login_error_message()
    sucs_msg = login_page.login("angular", "password").is_login_success_message()
    assert exp_err_msg in err_msg, f"Expected {exp_err_msg}, but got {err_msg}"
    assert exp_sucs_msg in sucs_msg, f"Expected {exp_sucs_msg}, but got {sucs_msg}"


@allure.feature("Банковские операции")
@allure.story("Регистрация Sample")
@allure.title("Проверка регистрации через Sample форму")
@allure.severity(allure.severity_level.NORMAL)
def test_sample_form_registration(banking_page, banking_test_data):
    data = banking_test_data

    smpl_message = (
        banking_page.go_to_sample_tab()
        .fill_sample_form(
            data["firstname"], data["lastname"], data["email"], data["password"]
        )
        .is_sample_success_msg()
    )
    exp_smpl_message = "User registered successfully!"
    assert smpl_message == exp_smpl_message, (
        f"Expected {exp_smpl_message} message, but got {smpl_message}"
    )


@allure.feature("Банковские операции")
@allure.story("Управление клиентами")
@allure.title("Проверка создания и открытия аккаунта клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_customer_account(banking_page, banking_test_data):
    data = banking_test_data
    exp_add_cust_msg = "Customer added successfully"
    add_cust_msg = (
        banking_page.go_to_manager_tab()
        .add_new_customer(data["firstname"], data["lastname"], data["postcode"])
        .handle_alert()
    )
    assert exp_add_cust_msg in add_cust_msg, "Error in alert message."

    exp_op_cust_msg = "Account created successfully"
    op_cust_msg = banking_page.open_acc(
        data["firstname"], data["lastname"]
    ).handle_alert()
    assert exp_op_cust_msg in op_cust_msg, "Error in alert message."


@allure.feature("Банковские операции")
@allure.story("Авторизация клиента в банке")
@allure.title("Проверка логина клиента в банковской системе")
@allure.severity(allure.severity_level.CRITICAL)
def test_customer_login(banking_page_prepared, banking_test_data):
    banking_page = banking_page_prepared
    data = banking_test_data

    exp_w_msg = f"{data['firstname']} {data['lastname']}"
    welcome_msg = banking_page.get_welcome_msg()
    assert exp_w_msg in welcome_msg, "Wrong welcome message"


@allure.feature("Банковские операции")
@allure.story("Депозиты")
@allure.title("Проверка функции депозита")
@allure.severity(allure.severity_level.CRITICAL)
def test_deposit_transaction(banking_page_prepared):
    banking_page = banking_page_prepared
    exp_dep_scs_msg = "Deposit Successful"
    amount = 100321

    dep_scs_msg = banking_page.customer_deposit_withdraw(
        amount, "deposit"
    ).deposit_withdraw_success_msg()
    assert exp_dep_scs_msg == dep_scs_msg, "Unexpected deposit success message state"
    assert banking_page.is_transaction_present(amount), (
        "Table does not contain expected transaction"
    )

    dep_scs_msg = banking_page.customer_deposit_withdraw(
        0, "deposit"
    ).deposit_withdraw_success_msg()
    assert exp_dep_scs_msg != dep_scs_msg, "Unexpected deposit message"
    assert not banking_page.is_transaction_present(0), (
        "Table contain unexpected transaction"
    )


@allure.feature("Банковские операции")
@allure.story("Снятие средств")
@allure.title("Проверка функции снятия средств")
@allure.severity(allure.severity_level.CRITICAL)
def test_withdraw_transaction(banking_page_with_deposit):
    banking_page = banking_page_with_deposit
    balance = banking_page.get_balance()
    amount = random.randint(1, (balance - 1))
    exp_wthdr_scs_msg = "Transaction successful"

    wthdr_scs_msg = banking_page.customer_deposit_withdraw(
        amount, "withdraw"
    ).deposit_withdraw_success_msg()
    assert exp_wthdr_scs_msg == wthdr_scs_msg, (
        "Unexpected withdraw success message state"
    )
    assert banking_page.is_transaction_present(amount), (
        "Table does not contain expected transaction"
    )

    amount = 1000000
    exp_wthdr_scs_msg = (
        "Transaction Failed. You can not withdraw amount more than the balance."
    )

    wthdr_scs_msg = banking_page.customer_deposit_withdraw(
        amount, "withdraw"
    ).deposit_withdraw_success_msg()
    assert exp_wthdr_scs_msg == wthdr_scs_msg, "Unexpected withdraw error message"
    assert not banking_page.is_transaction_present(amount), (
        "Table contain unexpected transaction"
    )


@allure.feature("Банковские операции")
@allure.story("Проверка баланса")
@allure.title("Проверка расчета баланса по таблице транзакций")
@allure.severity(allure.severity_level.CRITICAL)
def test_balance_calculation(banking_page_with_deposit):
    banking_page = banking_page_with_deposit
    initial_balance = banking_page.get_balance()
    calc_balance = banking_page.calculate_balance_from_table()

    assert initial_balance == calc_balance, "Balances doesn't match"

    amount = initial_balance
    exp_wthdr_scs_msg = "Transaction successful"

    wthdr_scs_msg = banking_page.customer_deposit_withdraw(
        amount, "withdraw"
    ).deposit_withdraw_success_msg()
    assert exp_wthdr_scs_msg == wthdr_scs_msg, (
        "Unexpected withdraw success message state"
    )
    assert banking_page.get_balance() == 0, "Balance is not 0"


@allure.feature("Банковские операции")
@allure.story("Управление счетом")
@allure.title("Проверка зачистки таблицы транзакций")
@allure.severity(allure.severity_level.CRITICAL)
def test_clear_transaction_list(banking_page_with_deposit):
    banking_page = banking_page_with_deposit

    result = banking_page.clear_transaction_list()
    assert not result, "Transaction is not cleared"


@allure.feature("Банковские операции")
@allure.story("Управление клиентами")
@allure.title("Проверка удаления клиента из системы")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_customer_account(banking_page_prepared, banking_test_data):
    banking_page = banking_page_prepared
    data = banking_test_data

    assert banking_page.go_to_manager_tab().find_customer(
        data["firstname"], data["lastname"]
    ), "This customer is not in the table"
    assert not banking_page.delete_customer(data["firstname"]).find_customer(
        data["firstname"], data["lastname"]
    ), "Customer still in the table"
