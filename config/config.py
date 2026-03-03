import os

import dotenv

dotenv.load_dotenv()


class Grid:
    URL = os.environ["GRID_URL"]


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


class JqueryPagesConf:
    DROP_URL = os.environ["DROPPABLE_URL"]
    TABS_URL = os.environ["TABS_URL"]
    ALERT_URL = os.environ["ALERT_URL"]
    AUTH_URL = os.environ["AUTH_URL"]
