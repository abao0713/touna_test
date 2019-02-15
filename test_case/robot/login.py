from common.select_browser import BrowserEngine
from elements.robot_elements import robot
from logs.Log import MyLog



log = MyLog.get_log(logger="Login")
Logger = log.get_logger()
class Login():
    def __init__(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
    def login(self):
        Robot = robot(self.driver)
        Robot.input_username('aybj')
        Robot.input_username('Aa123456')
        Robot.submit()
        if Robot.login_success():
            Logger.info('登录成功，账户名为aybj')
        else:
            Logger.info('登录失败')