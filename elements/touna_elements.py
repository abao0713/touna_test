from common.base_page import *
import yaml
from selenium.webdriver.common.keys import Keys

dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
file_path = dir + '/config_file/touna.yaml'
print(file_path)
with open(file_path,'r',encoding="UTF-8") as file:

    try:
        yaml_data = yaml.load(file)
    except:
        print("open yaml is no")
print(yaml_data)

class touna(BasePage):
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open_login(self):
        self.login_url = yaml_data["login"]["login_url"]

        self.find_element(self.login_url).click()
    #输入账户类型
    def choose_type(self,logo):
        self.usertype_one = yaml_data["login"]["usertype_one"]
        self.usertype_second = yaml_data["login"]["usertype_second"]
        if logo == '1':
            self.find_element(self.usertype_second).click()
    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.username = yaml_data["login"]["username"]
        #self.find_element(self.username).send_keys(Keys.CONTROL,'a')
        #self.find_element(self.username).send_Keys(Keys.DELETE)
        self.find_element(self.username).click()
        self.find_element(self.username).clear()
        self.find_element(self.username).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.password = yaml_data["login"]["password"]
        #self.find_element(self.password).send_keys(Keys.CONTROL,'a')
        #self.find_element(self.password).send_Keys(Keys.DELETE)
        self.find_element(self.password).click()
        self.find_element(self.password).clear()
        self.find_element(self.password).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.button = yaml_data["login"]["button"]
        self.find_element(self.button).click()

    # 身份校验认证弹窗处理
    def alert_cancel(self):
        self.alert_cancel = yaml_data["login"]["alert_cancel"]
        return self.find_element(self.alert_cancel).click()


