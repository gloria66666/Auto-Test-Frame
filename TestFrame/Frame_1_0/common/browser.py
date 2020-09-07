# coding=utf-8

from TestFrame.Frame_1_0.log.logger import Logger
from selenium import webdriver
import logging

# logger = Logger(logger='BrowserEngine', level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger='Browser', level=logging.INFO, r_mode=False).get_log()


# 浏览器引擎类
class Browser(object):

    def __init__(self, browser, url):
        self.browser = browser.strip()
        self.url = url
        try:
            if browser == 'Firefox':
                self.driver = webdriver.Firefox()
                logger.info('Starting firefox browser')
            elif self.browser == 'Chrome':
                self.driver = webdriver.Chrome()
                logger.info('Starting Chorme browser')
            elif self.browser == 'IE':
                self.driver = webdriver.Ie()
                logger.info('Starting IE browser')
            else:
                self.driver = webdriver.Firefox()
                logger.info('[default]Starting Firefox browser')
        except Exception as e:
            logger.error('Browser_init:%s' % e)

    # 打开浏览器，访问 url 地址
    def open_browser(self):
        try:
            self.driver.get(self.url) # 访问 url 地址
            logger.info('Open url %s' % self.url)
            self. driver.implicitly_wait(10)
            logger.info('Set implicitly wait 10 seconds')
            return self.driver
        except Exception as e:
            logger.error('open_browser:%s' % e)

    def close_browser(self):
        try:
            logger.info('Now, close the browser.')
            # 关闭当前tab，只有一个tab则关闭浏览器窗口
            self.driver.close()
        except Exception as e:
            logger.error('close_browser:%s' % e)

    def quit_browser(self):
        try:
            logger.info('Now, quit the browser.')
            # 退出驱动且关闭所关联的所有窗口
            self.driver.quit()
        except Exception as e:
            logger.error('quit_browser:%s' % e)
