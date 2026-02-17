import random


def test_mainpage(app):
    mainpage = app.main_page
    mainpage.go_to_main_page()
    assert mainpage.is_layout_correct()

    assert mainpage.is_header_correct()

    current_footer_contacts = mainpage.get_footer_contacts()
    target_footer_contacts = [
        "CDR Complex, 3rd Floor, Naya Bans Market, Sector 15, Noida, Near sec-16 Metro Station",
        "+91 97111-11-558",
        "+91 97111-91-558",
        "trainer@way2automation.com",
        "seleniumcoaching@gmail.com",
    ]
    for contact in target_footer_contacts:
        assert contact in current_footer_contacts, f"'{contact}' not in the footer"


def test_sticky_menu(app):
    mainpage = app.main_page
    mainpage.go_to_main_page()
    assert mainpage.is_element_in_viewport()


def test_navigate_to_lifetime_membership(app):
    mainpage = app.main_page
    mainpage.go_to_main_page()

    original_url = mainpage.get_current_url()
    mainpage.navigate_to_lifetime()
    mainpage.wait.until(lambda driver: driver.current_url != original_url)
    new_url = mainpage.get_current_url()
    assert "lifetime-membership-club" in new_url, (
        f"Not on lifetime membership page. Current URL: {new_url}"
    )

    page_title = mainpage.get_changed_page_title()
    expected_title_content = "LIFETIME MEMBERSHIP CLUB"
    assert expected_title_content in page_title.upper(), (
        f"Expected '{expected_title_content}' in page title, got: {page_title}"
    )


def test_login_page(app):
    loginpage = app.login_page
    loginpage.go_to_login_page()

    assert loginpage.are_login_fields_present(), "Couldnt find login fields"
    assert not loginpage.is_login_enabled(), "Login enabled with empty login fields"

    exp_err_msg = "Username or password is incorrect"
    exp_sucs_msg = "You're logged in!!"
    err_msg = loginpage.login("invalid", "invalid").is_login_error_message()
    sucs_msg = loginpage.login("angular", "password").is_login_success_message()
    assert exp_err_msg in err_msg, f"Expected {exp_err_msg}, but got {err_msg}"
    assert exp_sucs_msg in sucs_msg, f"Expected {exp_sucs_msg}, but got {sucs_msg}"


def test_banking_page(app):
    bankingpage = app.banking_page

    firstname, lastname, email, password, postcode = (
        "firstName",
        "lastName",
        "user@example.com",
        "password",
        "12345",
    )

    smpl_message = (
        bankingpage.go_to_sample_tab()
        .calculate_longest_hobby_and_click()
        .fill_sample_form(firstname, lastname, email, password)
        .is_sample_success_msg()
    )
    exp_smpl_message = "User registered successfully!"
    assert smpl_message == exp_smpl_message, (
        f"Expected {exp_smpl_message} message, but got {smpl_message}"
    )

    # Add and open customer account
    exp_add_cust_msg = "Customer added successfully"
    add_cust_msg = (
        bankingpage.go_to_manager_tab()
        .add_new_customer(firstname, lastname, postcode)
        .handle_alert()
    )
    assert exp_add_cust_msg in add_cust_msg, "Error in alert message."

    exp_op_cust_msg = "Account created successfully"
    op_cust_msg = bankingpage.open_acc(firstname, lastname).handle_alert()
    assert exp_op_cust_msg in op_cust_msg, "Error in alert message."

    # Log in Customer
    exp_w_msg = f"{firstname} {lastname}"
    welcome_msg = (
        bankingpage.go_to_customer_tab()
        .login_as_customer(firstname, lastname)
        .get_welcome_msg()
    )
    assert exp_w_msg in welcome_msg, "Wrong welcome message"

    # Deposit check
    exp_dep_scs_msg = "Deposit Successful"
    amount = 100321
    dep_scs_msg = bankingpage.customer_deposit_withdraw(
        amount, "deposit"
    ).deposit_withdraw_success_msg()
    assert exp_dep_scs_msg == dep_scs_msg, "Unexpected deposit success message state"
    assert bankingpage.is_transaction_present(amount), (
        "Table does not contain expected transaction"
    )
    dep_scs_msg = bankingpage.customer_deposit_withdraw(
        0, "deposit"
    ).deposit_withdraw_success_msg()
    assert exp_dep_scs_msg != dep_scs_msg, "Unexpected deposit message"
    assert not bankingpage.is_transaction_present(0), (
        "Table contain unexpected transaction"
    )

    # Withdraw check
    balance = bankingpage.get_balance()
    amount = random.randint(1, (balance - 1))
    exp_wthdr_scs_msg = "Transaction successful"
    wthdr_scs_msg = bankingpage.customer_deposit_withdraw(
        amount, "withdraw"
    ).deposit_withdraw_success_msg()
    assert exp_wthdr_scs_msg == wthdr_scs_msg, (
        "Unexpected withdraw success message state"
    )
    assert bankingpage.is_transaction_present(amount), (
        "Table does not contain expected transaction"
    )

    amount = 1000000
    exp_wthdr_scs_msg = (
        "Transaction Failed. You can not withdraw amount more than the balance."
    )
    wthdr_scs_msg = bankingpage.customer_deposit_withdraw(
        amount, "withdraw"
    ).deposit_withdraw_success_msg()
    assert exp_wthdr_scs_msg == wthdr_scs_msg, "Unexpected withdraw error message"
    assert not bankingpage.is_transaction_present(amount), (
        "Table contain unexpected transaction"
    )

    # Balance check
    balance = bankingpage.get_balance()
    calc_balance = bankingpage.calculate_balance_from_table()
    assert balance == calc_balance, "Balances doesn`t match"

    amount = balance
    exp_wthdr_scs_msg = "Transaction successful"
    wthdr_scs_msg = bankingpage.customer_deposit_withdraw(
        amount, "withdraw"
    ).deposit_withdraw_success_msg()
    assert exp_wthdr_scs_msg == wthdr_scs_msg, (
        "Unexpected withdraw success message state"
    )
    assert bankingpage.get_balance() == 0, "Balance is not 0"
    assert not bankingpage.clear_transaction_list(), "Transaction is not cleared"

    # Delete Customer

    assert bankingpage.go_to_manager_tab().find_customer(firstname, lastname), (
        "This customer is not in the table"
    )
    assert not bankingpage.delete_customer(firstname).find_customer(
        firstname, lastname
    ), "Customer still in the table"
