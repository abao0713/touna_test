import os
import unittest
from logs.Log import MyLog
from common import readConfig as readConfig
from common import HTMLTestRunner
from common.configEmail import MyEmail
from BeautifulReport import BeautifulReport


localReadConfig = readConfig.ReadConfig()


class AllTest:
    def __init__(self):
        global log, Logger, resultPath, on_off,report_path
        log = MyLog.get_log(logger="AllTest")
        Logger = log.get_logger()
        report_path = log.get_report_path()
        #resultPath = log.get_result_path()
        on_off = localReadConfig.get_email("on_off")
        self.caseListFile = os.path.join(readConfig.proDir, "config_file\\testlist.ini")
        #accept file test
        self.caseFile = os.path.join(readConfig.proDir, "test_case")

        print(self.caseFile)

        # self.caseFile = None
        self.caseList = []
        self.email = MyEmail.get_email()

    def set_case_list(self):
        """
        set case list
        :return:
        """
        try:

            fb = open(self.caseListFile)
            for value in fb.readlines():
                data = str(value)
                if data != '' and not data.startswith("#"):
                    self.caseList.append(data.replace("\n", ""))
            fb.close()

        except:
            Logger.info("the testlist.ini file is lose")
        return self.caseList

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        if self.set_case_list() == None:
            Logger.info("this testlist,s file is none")
        else:
            self.set_case_list()

        test_suite = unittest.TestSuite()
        suite_module = []


        for case in self.caseList:
            #case_name = case.split("/")[-1]
            #print(self.caseFile + '\\product')

            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case + '.py', top_level_dir=None)
            suite_module.append(discover)


        if len(suite_module) > 0:
            #print(suite_module)
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)

        else:
            Logger.info("not test case find")
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                Logger.info("********TEST START********")
                #fp = open(resultPath, 'wb+')
                """
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description',verbosity=2)
                runner.run(suit)
                """
                result = BeautifulReport(suit)
                result.report(filename='touna_test_report', description='touna', log_path=report_path)
            else:
                Logger.info("Have no case to test.")
        except Exception as ex:
            Logger.error(str(ex))
        finally:
            Logger.info("*********TEST END*********")
            #fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
            elif on_off == 'off':
                Logger.info("Doesn't send report email to developer.")
            else:
                Logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()
