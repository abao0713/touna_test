from common.select_browser import BrowserEngine
from elements.touna_elements import touna
import unittest
import time

class Test_login(unittest.TestCase):
    def setUp(self):
        """
        初始化浏览器
        :return:
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
    def tearDown(self):
        """
        测试结束后关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_login(self):
        Touna=touna(self.driver)
        Touna.open_login()
        time.sleep(3)
        Touna.choose_type(0)
        Touna.input_username("15270239931")
        Touna.input_password("a305634841")
        Touna.click_submit()
        Touna.alert_cancel()


if __name__ == "__main__":
    unittest.main()







