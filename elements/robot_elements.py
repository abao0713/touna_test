from common.base_page import *
from selenium.webdriver.common.action_chains import  ActionChains
import yaml
from selenium.webdriver.common.keys import Keys
from logs.Log import MyLog
from common.comsrc import *



#log = MyLog.get_log(logger="robot")
#Logger = log.get_logger()
dir = os.path.dirname(os.path.abspath(__file__)) # 注意相对路径获取方法
dir_base = os.path.dirname(dir)
file_path = (dir_base + '/config_file/robot.yaml').replace("\\","/")
print(file_path)
log = MyLog.get_log(logger="robot")
Logger = log.get_logger()
with open(file_path,'r',encoding="UTF-8") as file:

    try:
        yaml_data = yaml.load(file)
    except Exception as e:
        print(e)
print(yaml_data)

class robot(BasePage):
    def element_verify(fun):
        def element(*args, **kwargs):
            try:
                fun(*args, **kwargs)
            except Exception as e:
                print('Error element: %s' % fun.__name__)
                print(kwargs)
                print(traceback.format_exc())
                Logger.info(e)
        return element

    def input_username(self,username):
        """
        登录用户名输入
        :param username:入参值
        :return:
        """
        self.username = yaml_data['login']['username']
        a = self.username
        self.find_element(self.username).click()
        self.find_element(self.username).clear()
        self.find_element(self.username).send_keys(username)
        Logger.info("The test username is: %s" % self.username)
        return a
    def input_password(self,password):
        """
        登录密码输入
        :param password: 入参指定密码
        :return:
        """
        self.password = yaml_data["login"]["password"]
        # self.find_element(self.password).send_keys(Keys.CONTROL,'a')
        # self.find_element(self.password).send_Keys(Keys.DELETE)
        self.find_element(self.password).click()
        self.find_element(self.password).clear()
        self.find_element(self.password).send_keys(password)
        Logger.info("The password is: %s" % self.password)
    def submit(self):
        """
        登录
        :return:
        """
        self.button = yaml_data['login']['button']
        self.find_element(self.button).click()
    def login_success(self):
        """
        登录成功验证模块
        :return:
        """
        self.login_success = yaml_data['login']['login_success']
        a=self.find_element(self.login_success).text
        if a == '欢迎使用智能语音管理系统':
            return True
        else:
            return False
    def log_out(self):
        """
        注销操作
        :return:
        """
        self.move = yaml_data['logout']['move']
        self.logout = yaml_data['logout']['logout']
        botton = self.find_element(self.move)
        ActionChains(self.driver).move_to_element(botton).perform()
        self.find_element(self.logout).click()
    @element_verify
    def entry_set(self):
        """
        进入到设置模块
        :return:
        """
        self.entry = yaml_data['set']['entry']
        self.find_element(self.entry).click()
    def call_set(self):
        self.call = yaml_data['set']['call']
        self.find_element(self.call_set()).click()




    def call_edit(self):
        """

        :return:
        """
        self.call_edit = yaml_data['set']['call_edit']

        elements = self.find_elements(self.call_edit)
        for element in elements:
            element.click()


