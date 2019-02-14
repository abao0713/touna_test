from common.base_page import *
import yaml
from selenium.webdriver.common.keys import Keys
from logs.Log import MyLog



log = MyLog.get_log(logger="robot")
Logger = log.get_logger()
dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
file_path = dir + '/config_file/robot.yaml'
print(file_path)
with open(file_path,'r',encoding="UTF-8") as file:

    try:
        yaml_data = yaml.load(file)
    except:
        print("open yaml is no")
print(yaml_data)

class robot(BasePage):
    def open_login(self):
