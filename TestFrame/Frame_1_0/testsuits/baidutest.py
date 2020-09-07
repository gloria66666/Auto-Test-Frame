# coding=utf-8

from TestFrame.Frame_1_0.config.config_parser import Config
from TestFrame.Frame_1_0.log.logger import Logger
from TestFrame.Frame_1_0.common.browser import Browser
from TestFrame.Frame_1_0.common.page import Page
from TestFrame.Frame_1_0.common.excel import Excel
import time
import unittest
import operator
import logging

# logger = Logger(logger="Baidutest", level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger="Baidutest", level=logging.INFO, r_mode=False).get_log()

ori_win_handle_lst = [0]
win_size_dict = {'width': 0, 'height': 0}


def execute(excl, instance, start_row, end_row, s,
            case_col=None, sleep_col=None, assert_col=None, sleep_bool=True, assert_bool=True):
    try:
        logger.info('Execute the case from the rd_book\'s sheet [%s]: '
                    '[%s]row-[%s]row' % (excl.wt_sheet_idx, start_row, end_row))
        for i in range(int(start_row), int(end_row) + 1):
            case_cell = excl.cell_value(i, case_col).strip()
            case_lst = case_cell.split('&')
            logger.info('case_lst:%s' % case_lst)
            if sleep_bool:
                sleep_cell = excl.cell_value(i, int(sleep_col)).strip()
                sleep_lst = sleep_cell.split(',')
                logger.info('sleep time list:%s' % sleep_lst)
                sleep_lst = list(map(int, sleep_lst))
                x = 0
            for l in case_lst:
                para = l.split(',')
                logger.info('para:%s' % para)
                if para[0] == 'current_window_handle' or para[0] == 'switch_window':
                    para[1] = eval('ori_win_handle_lst')
                if para[0] == 'get_window_size':
                    para[1] = eval('win_size_dict')
                operator.methodcaller(*para)(instance)
                if sleep_bool and x < len(sleep_lst):
                    if sleep_lst[x] != 0:
                        logger.info('It will sleep %sS' % sleep_lst[x])
                        logger.info(time.time())
                        time.sleep(sleep_lst[x])
                        logger.info(time.time())
                    x += 1
            if assert_bool:
                try:
                    assert_cell = excl.cell_value(i, int(assert_col)).strip()
                    assert_lst = assert_cell.split('&')
                    logger.info('assert_lst:%s' % assert_lst)
                    for l in assert_lst:
                        para = l.split(':')
                        result = para[len(para) - 1]
                        logger.info('result:%s' % result)
                        val = para[0]
                        logger.info('para[0]:%s' % para[0])
                        val = val.split(',')
                        if 'width' in result:
                            result = eval('win_size_dict[\'width\']')
                            val[1] = int(val[1])
                        elif 'height' in result:
                            result = eval('win_size_dict[\'height\']')
                            val[1] = int(val[1])
                        else:
                            result = result.split(',')
                            result = operator.methodcaller(*result)(instance)
                            logger.info('func result:%s' % result)
                        operator.methodcaller(*val, result)(s)
                    excl.write(i, int(assert_col)+1, 'Pass')
                except Exception as e:
                    logger.error('Test assert Fail:%s' % e)
                    excl.write(i, int(assert_col) + 1, 'Fail')
    except Exception as e:
        logger.error('Test Fail:%s' % e)


class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Config('config.ini')

        # 读取 config 配置文件内容
        cls.browser = cls.config.get_value("browserType", "browserName")
        logger.info("You had select %s browser." % cls.browser)
        # cls.url = cls.config.get_value("testServer", "URL")
        # logger.info("The test server url is %s" % cls.url)
        cls.rd_book_path = cls.config.get_value("Excel", "rd_book_path")
        logger.info("The test case file path is %s" % cls.rd_book_path)
        cls.rd_book_name = cls.config.get_value("Excel", "rd_book_name")
        logger.info("The test case file name is %s" % cls.rd_book_name)
        cls.sheet_name = cls.config.get_value("Excel", "sheet_name")
        logger.info("The test case sheet name is %s" % cls.sheet_name)
        cls.case_col = int(cls.config.get_value("Excel", "case_col"))
        logger.info("The test case col is %s" % cls.case_col)
        cls.sleep_col = int(cls.config.get_value("Excel", "sleep_col"))
        logger.info("The test case sleep col is %s" % cls.sleep_col)
        cls.assert_col = int(cls.config.get_value("Excel", "assert_col"))
        logger.info("The test case assert col is %s" % cls.assert_col)

        # 若有一个用例driver.close后续用例会报错
        # cls.browser = Browser(browser, url)
        # cls.driver = cls.browser.open_browser()  # 读取浏览器类型

    @classmethod
    def tearDownClass(cls):
        # logger.info('The browser will be close after 3 seconds.')
        # time.sleep(3)
        # cls.browser.quit_browser()
        pass

    def setUp(self):
        self.browser = Browser(BaiduTest.browser, 'https://www.weibo.com/')
        self.driver = self.browser.open_browser()
        self.excl = Excel(BaiduTest.rd_book_path, BaiduTest.rd_book_name, sheet_name=BaiduTest.sheet_name)

    def tearDown(self):
        # self.browser.quit_browser()
        pass

    def test_baidu_signin(self):
        try:
            driver = Page(self.driver)

            execute(self.excl, driver, 1, 2, self,
                    case_col=BaiduTest.case_col, sleep_col=BaiduTest.sleep_col, assert_col=BaiduTest.assert_col,
                    sleep_bool=True, assert_bool=True)
            self.dirver.quit()
            self.browser = Browser(BaiduTest.browser, 'https://www.iziqian.com/')
            self.driver = self.browser.open_browser()
            driver = Page(self.driver)

            execute(self.excl, driver, 3, 3, self,
                              case_col=1, sleep_col=2, assert_col=3, sleep_bool=False, assert_bool=False)
        except Exception as e:
            logger.error("Test Fail:%s" % e)
        finally:
            self.browser.quit_browser()
            self.excl.save()


if __name__ == '__main__':
    unittest.main()
