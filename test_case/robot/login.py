from common.select_browser import BrowserEngine
from elements.robot_elements import robot
from logs.Log import MyLog
import unittest


log = MyLog.get_log(logger="Login")
Logger = log.get_logger()
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        初始化浏览器
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        """
        测试结束后关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_login(self):
        Robot = robot(self.driver)
        Robot.input_username('aybj')
        Robot.input_password('Aa123456')
        Robot.submit()
        if Robot.login_success():
            Logger.info('登录成功，账户名为aybj')
        else:
            Logger.info('登录失败')
    def test_logout(self):
        Robot = robot(self.driver)
        Robot.log_out()


if __name__ == '__main__':
    unittest.main()
