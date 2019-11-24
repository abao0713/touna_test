from common.select_browser import BrowserEngine
from elements.robot_elements import robot
from logs.Log import MyLog
import unittest,time


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

    def test1_login(self):
        Robot = robot(self.driver)
        Robot.input_username('test01')
        Robot.input_password('Aa123456')
        Robot.submit()
        if Robot.login_success():
            Logger.info('登录成功，账户名为test01')
        else:
            Logger.info('登录失败')
    def test2_jump_set(self):
        Robot = robot(self.driver)
        Robot.entry_set()
        Robot.jump_set()
        time.sleep(3)
        Robot.jump_edit()


    def test3_logout(self):
        Robot = robot(self.driver)
        Robot.log_out()
        Logger.info('退出成功')


if __name__ == '__main__':
    unittest.main()