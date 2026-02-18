from selenium.webdriver.common.by import By


class MainPageLocators:
    # Base elements
    HEADER_CONTACTS = (
        By.CSS_SELECTOR,
        ".site-above-header-wrap, .header-contact, .contact-info",
    )
    NAV_BLOCK = (
        By.CSS_SELECTOR,
        "div[class*='ast-primary-header-bar'][class*='ast-primary-header']",
    )
    REG_BUTTON = (
        By.XPATH,
        "//a[contains(@href, 'lifetime-membership-club') and text()='Register Now']",
    )
    COURSE_LIST = (By.CSS_SELECTOR, "[data-id='5b4952c1']")
    FOOTER = (By.CSS_SELECTOR, "div[data-id='695441a0']")

    # Contacts in header
    PHONE = (
        By.XPATH,
        "//a[contains(@href, 'tel:+')]",
    )
    SKYPE = (
        By.XPATH,
        "//a[contains(@href, 'skype:') ]",
    )
    EMAIL = (By.XPATH, "//a[contains(@href, '@')]")
    MEDIA = (
        By.CSS_SELECTOR,
        "[data-section='section-hb-social-icons-1']",
    )

    # Slider
    CAROUSEL_CONT = (By.CSS_SELECTOR, "[data-id='50827c4']")
    SLIDER_NEXT = (
        By.CSS_SELECTOR,
        ".pp-slider-arrow.elementor-swiper-button-next.swiper-button-next-c50f9f0",
    )
    CAROUSEL_ORIG = (By.CSS_SELECTOR, "img[id='NjczOjE0Mw==-1']")
    CAROUSEL_NEXT = (By.CSS_SELECTOR, "id='NzAxOjEzMw==-1']")

    # Change page locators
    MENU_ALL_COURSES = (By.XPATH, "//span[text()='All Courses']")
    MENU_LIFETIME = (
        By.XPATH,
        "//a[@class='menu-link' and contains(@href, 'lifetime-membership-club')]",
    )
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.elementor-heading-title")

    # Contacts in footer
    FOOTER_CONTACTS = (
        By.XPATH,
        "//div[@data-id='695441a0']//span[contains(@class,'elementor-icon-list-text')]",
    )


class LoginPageLocators:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    USERNAME_DESCRIPTION = (By.ID, "formly_1_input_username_0")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[ng-click*='Auth.login']")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")
    STATUS_MSG = (By.XPATH, '//*[text()="You\'re logged in!!"]')
    ERROR_LOGIN_MSG = (By.CSS_SELECTOR, ".alert-danger")


class BankingPageLocators:
    # Roles
    BTN_SAMPLE_LOGIN = (By.LINK_TEXT, "Sample Form")
    BTN_MANAGER_LOGIN = (By.XPATH, "//button[text()='Bank Manager Login']")
    BTN_CUSTOMER_LOGIN = (By.XPATH, "//button[text()='Customer Login']")

    # Sample
    SMP_FIRST_NAME = (By.ID, "firstName")
    SMP_LAST_NAME = (By.ID, "lastName")
    SMP_EMAIL = (By.ID, "email")
    SMP_PASSWORD = (By.ID, "password")
    HOBBIES = (
        By.XPATH,
        "//label[text()='Hobbies']/../div//label/input[@type='checkbox']",
    )
    GENDER = (By.ID, "gender")
    TEXTAREA = (By.ID, "about")
    REGISTER = (By.XPATH, "//button[text()='Register']")
    SMP_SUCCESS_MESSAGE = (By.ID, "successMessage")
    SMP_ERROR_MESSAGE = (By.ID, "errorMessage")

    # Manager
    BTN_ADD_CUST_MENU = (
        By.XPATH,
        "//button[contains(@ng-click, 'addCust') and contains(text(), 'Add Customer')]",
    )
    BTN_OPEN_ACC_MENU = (By.CSS_SELECTOR, "button[ng-click='openAccount()']")
    BTN_SHOW_CUST_MENU = (By.CSS_SELECTOR, "button[ng-click='showCust()']")

    # Add customer form
    ADD_CUST_FORM_FIRST_N = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    ADD_CUST_FORM_LAST_N = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    ADD_CUST_FORM_PC = (By.CSS_SELECTOR, "input[placeholder='Post Code']")
    ADD_CUST_FORM_BTN = (
        By.XPATH,
        "//button[contains(@type, 'submit') and contains(text(), 'Add Customer')]",
    )
    # Open customer form
    OP_CUST_FORM_USER_SELECT = (By.ID, "userSelect")
    OP_CUST_FORM_CURRENCY = (By.ID, "currency")
    OP_CUST_FORM_PRCS_BTN = (By.XPATH, "//button[text()='Process']")

    # Customer list form
    CUST_DELETE_BTN = (By.XPATH, "//button[text()='Delete']")
    CUST_SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Search Customer']")

    # Customer
    WELCOME_MSG = (By.XPATH, "//strong[contains(text(), 'Welcome')]")
    DEP_WTHDR_MSG = (By.CSS_SELECTOR, "span.error.ng-binding[ng-show='message']")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")
    DEPOSIT_TAB = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
    WITHDRAW_TAB = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")
    TRANS_TAB = (By.CSS_SELECTOR, "button[ng-click='transactions()']")
    BACK_FROM_TRANS_TAB = (By.CSS_SELECTOR, "button[ng-click='back()']")
    BALANCE = (By.XPATH, "//div[@ng-hide='noAccount']//strong[2]")

    AMOUNT_INP = (By.CSS_SELECTOR, "input[placeholder='amount']")
    SUBMIT_BTN = (By.XPATH, "//button[text()='Deposit' or text()='Withdraw']")

    #
    TRANS_ROWS = (By.XPATH, "//table/tbody/tr")
    RESET_BTN = (By.CSS_SELECTOR, "button[ng-click='reset()']")
    BACK_BTN = (By.CSS_SELECTOR, "button[ng-click='back()']")
    SCROLL_R_BTN = (By.CSS_SELECTOR, "button[ng-click='scrollRight()']")
