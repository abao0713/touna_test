from common.select_browser import BrowserEngine
from elements.touna_elements import touna
from common.base_page import *

class login(BasePage):
    def test_login(self):
        touna.open_login()
        touna.choose_type(1)
        touna.input_username()
        touna.input_password()
        touna.click_submit()
        touna.alert_cancel()


if __name__ == "__main__":
    a=login()
    a.test_login()







