# coding=utf-8
import os.path
import time

from selenium.common.exceptions import NoSuchElementException
from logs.Log import MyLog


log = MyLog.get_log(logger="BasePage")
Logger = log.get_logger()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

        # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作

    def forward(self):
        self.driver.forward()
        Logger.info("Click forward on current page.")

        # 浏览器后退操作

    def back(self):
        self.driver.back()
        Logger.info("Click back on current page.")

        # 隐式等待

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        Logger.info("wait for %d seconds." % seconds)

        # 点击关闭当前窗口

    def close(self):
        try:
            self.driver.close()
            Logger.info("Closing and quit the browser.")
        except NameError as e:
            Logger.error("Failed to quit the browser with %s" % e)

            # 保存图片

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        proDir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        file_path = os.path.join(proDir, "my_report\\report_picture")
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            Logger.info("Had take screenshot and save to folder : /report_picture")
        except NameError as e:
            Logger.error("Failed to take report_picture! %s" % e)
            self.get_windows_img()

            # 定位元素方法

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                Logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                Logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                Logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                Logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

        # 输入

    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            Logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            Logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

            # 清除文本框

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            Logger.info("Clear text in input box before typing.")
        except NameError as e:
            Logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

            # 点击元素

    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            Logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            Logger.error("Failed to click the element with %s" % e)

            # 或者网页标题
    def send_key(self,selector,str):
        el = self.find_element(selector)
        try:
            el.send_keys(str)
            Logger.info("The string \' %s \' was send." % el.text)
        except NameError as e:
            Logger.error("Failed to send the string with %s" % e)

    def get_page_title(self):
        Logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        Logger.info("Sleep for %d seconds" % seconds)

if __name__ == '__main__':
    b="xpath=>.//*[@class='el-button el-button--primary el-button--mini']/span[text()='导入案件']"
    a = BasePage(object)
    a.get_windows_img()