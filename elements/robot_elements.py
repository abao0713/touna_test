from common.base_page import *
import yaml
from selenium.webdriver.common.keys import Keys
from logs.Log import MyLog



log = MyLog.get_log(logger="robot")
Logger = log.get_logger()
dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
file_path = (dir + '/touna_test/config_file/robot.yaml').replace("\\","/")
print(file_path)
with open(file_path,'r',encoding="UTF-8") as file:

    try:
        yaml_data = yaml.load(file)
    except Exception as e:
        print(e)
print(yaml_data)

class robot(BasePage):
    def input_username(self,username):
        self.username = yaml_data['login']['username']
        a = self.username
        self.find_element(self.username).click()
        self.find_element(self.username).clear()
        self.find_element(self.username).send_keys(username)
        Logger.info("The test username is: %s" % self.username)
        return a
    def input_password(self,password):
        self.password = yaml_data["login"]["password"]
        # self.find_element(self.password).send_keys(Keys.CONTROL,'a')
        # self.find_element(self.password).send_Keys(Keys.DELETE)
        self.find_element(self.password).click()
        self.find_element(self.password).clear()
        self.find_element(self.password).send_keys(password)
        Logger.info("The password is: %s" % self.password)
    def submit(self):
        self.button = yaml_data['login']['button']
        self.find_element(self.button).click()
    def login_success(self):
        self.login_success = yaml_data['login']['login_success']
        a=self.find_element(self.login_success).text()
        if a == input_username(self,username):
            return True
        else:
            return False