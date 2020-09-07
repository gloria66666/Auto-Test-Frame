# coding=utf-8

from TestFrame.Frame_1_0.config.config_parser import Config
from TestFrame.Frame_1_0.log.logger import Logger
from TestFrame.Frame_1_0.common.browser import Browser
from TestFrame.Frame_1_0.common.page import Page
import logging
import time
import unittest
import operator
import logging

# logger = Logger(logger="Mail126", level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger="Mail126", level=logging.INFO, r_mode=False).get_log()


class Mail126(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = Config('config.ini')

        # 读取 config 配置文件内容
        browser = config.get_value("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = 'http://www.126.com'
        logger.info("The test server url is %s" % url)
        cls.rd_book_path = config.get_value("Excel", "rd_book_path")
        logger.info("The test case file path is %s" % cls.rd_book_path)
        cls.rd_book_name = config.get_value("Excel", "rd_book_name")
        logger.info("The test case file name is %s" % cls.rd_book_name)
        cls.sheet_name = config.get_value("Excel", "sheet_name")
        logger.info("The test case sheet name is %s" % cls.sheet_name)
        cls.case_col = int(config.get_value("Excel", "case_col"))
        logger.info("The test case col is %s" % cls.case_col)
        cls.sleep_col = int(config.get_value("Excel", "sleep_col"))
        logger.info("The test case sleep col is %s" % cls.sleep_col)
        cls.assert_col = int(config.get_value("Excel", "assert_col"))
        logger.info("The test case assert col is %s" % cls.assert_col)

        cls.browser = Browser(browser, url)
        cls.driver = cls.browser.open_browser()  # 读取浏览器类型

    @classmethod
    def tearDownClass(cls):
        # logger.info('The browser will be close after 3 seconds.')
        # time.sleep(3)
        # cls.browser.quit_browser()
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mail_login1(self):
        try:
            driver = Page(Mail126.driver)
            # operator.methodcaller('function', para1, para2)(instances of the class)
            # operator.methodcaller('', , )()
            # frame = operator.methodcaller('find_element', 'x', '//*[@id="loginDiv"]/iframe')(driver)
            operator.methodcaller('switch_frame', 'x', '//*[@id="loginDiv"]/iframe')(driver)
            operator.methodcaller('clear', 'n', 'email')(driver)
            operator.methodcaller('send_keys', 'n', 'email', 'username')(driver)
            op = 'clear,n,password&send_keys,n,password,password'
            lst = op.split('&')
            logger.info(lst)
            for l in lst:
                para = l.split(',')
                logger.info(para)
                operator.methodcaller(*para)(driver)

            # list1 = ['click', 'i', 'dologin']
            # operator.methodcaller(*list1)(driver)
            operator.methodcaller('switch_to_default_content')(driver)
            try:
                assert '126网易免费邮' in driver.get_url_title()  # 调用页面对象继承基类中的获取页面标题方法
                operator.methodcaller('assertIn', '126网易免费邮', driver.get_url_title())(self)
                assert 'tab-2' in driver.get_attribute('i', 'loginBlock', 'class')
                logger.info("Test Pass")
            except Exception as e:
                logger.error("Test assert Fail:%s" % e)
        except Exception as e:
            logger.error("Test Fail:%s" % e)

    def test_mail_login2(self):
        try:
            browser = Browser('Firefox', 'http://baidu.com')
            self.driver = browser.open_browser()  # 读取浏览器类型
            driver = Page(self.driver)
            driver.send_keys('i', 'kw', 'su')
            driver.click('i', 'su')
            try:
                assert 'kw' in driver.get_attribute('i', 'kw', 'i')
                logger.info("Test Pass")
            except Exception as e:
                logger.error("Test assert Fail:%s" % e)
        except Exception as e:
            logger.error("Test Fail:%s" % e)
        finally:
            browser.quit_browser()


if __name__ == '__main__':
    unittest.main()
