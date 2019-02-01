import os.path
from configparser import ConfigParser

from selenium import webdriver

from my_framework.log import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine():
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'
    firefox_driver = dir + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config_file.ini file, return the driver

    def open_browser(self, driver):
        config = ConfigParser()
        #file_path1 = os.path.dirname(os.getcwd()) + '/config_file/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config_file/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()
