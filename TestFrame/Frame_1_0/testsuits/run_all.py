# !/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import os
import time
from TestFrame.Frame_1_0.testsuits.baidutest import BaiduTest
from TestFrame.Frame_1_0.testsuits.mail126test import Mail126
from TestFrame.Frame_1_0.common.HTMLTestRunner import HTMLTestRunner
from TestFrame.Frame_1_0.log.logger import Logger
import logging

# logger = Logger(logger='run_all', level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger='run_all', level=logging.INFO, r_mode=False).get_log()

# unittest suite 批量添加测试用例，逐个进行执行
# suite = unittest.TestSuite()
# suite.addTest(BaiduTest('test_baidu_signin'))
# suite.addTest(Mail126('test_mail_login2'))

# 添加一个类文件下的所有测试用例
suite = unittest.TestSuite()
testlst = [BaiduTest, Mail126]
for test in testlst:
    suite.addTest(unittest.makeSuite(test))
# 如果添加多个测试类文件，那么将变量对象设置为数组，然后添加到数组中，最后进行循环遍历

# 测试报告 title
title = 'xxx项目测试报告'
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/testreport/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLreport.html"

isExists = os.path.exists(report_path)
if not isExists:
    try:
        os.makedirs(report_path)
    except Exception as e:
        ("创建文件夹失败", e)

if __name__ == '__main__':
    # open(HtmlFile) 创建 html 测试报告
    with open(HtmlFile, "wb") as report:
        runner = HTMLTestRunner(stream=report,
                                title=title,
                                description='测试结果',
                                verbosity=2)
        runner.run(suite)
    # print(suite)
    # for i in suite:
    #     print(i)
    #     runner.run(i)

