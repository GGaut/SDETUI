import os

import dotenv

dotenv.load_dotenv()


class SQLConf:
    URL = os.environ["BASE_SQL_URL"]
    LOGIN = os.environ["SQL_LOGIN"]
    NAME = os.environ["NAME"]
    PASSWORD = os.environ["SQL_PASSWORD"]
    DEST_FILE = os.environ["SQL_COOKIE_FILE"]


class LoginPageConf:
    URL = os.environ["LOGINPAGE_URL"]


class MainPageConf:
    URL = os.environ["MAINPAGE_URL"]


class BankingPageConf:
    URL = os.environ["BANKINGPAGE_URL"]
