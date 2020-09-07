# coding=utf-8

import os
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from TestFrame.Frame_1_0.log.logger import Logger
import logging
from selenium.webdriver.common.by import By

# logger = Logger(logger='Page', level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger='Page', level=logging.INFO, r_mode=False).get_log()


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def __dir_exist(self, file_path):

        # 判断 screenshots 文件夹是否创建，未创建则进行创建
        is_exists = os.path.exists(file_path)
        # 判断文件夹是否存在，如果不存在则创建。
        if not is_exists:
            try:
                os.makedirs(file_path)
                return True
            except Exception as e:
                logger.error('创建文件夹失败 %s' % e)
                return False
        else:
            return True

    # 保存图片
    def get_windows_img(self, name='', fail=True):
        file_path = os.path.dirname(os.getcwd()) + '\\screenshots\\'
        if not self.__dir_exist(file_path):
            return None
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        if fail:
            screen_name = file_path + rq + '_F_' + name + '.png'
        else:
            screen_name = file_path + rq + '_S_' + name + '.png'
        logger.info('This screenshot will be save:%s' % screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(r'Take the screenshot and save to folder: \screenshots')
            return True
        except NameError as e:
            logger.error('Failed to take one screenshot!: %s' % e)
            self.get_windows_img('getwinimg')

    def refind(self, by=By.ID, value=''):
        ele = None
        attempts = 0
        while attempts < 3:
            try:
                ele = self.driver.find_element(by, value)
                break
            except StaleElementReferenceException:
                time.sleep(1)
            attempts += 1
        return ele

    # find_element_**  by:元素定位方法  value:元素位置
    def find_element(self, by='i', value=''):
        """
        定位元素
        :param  by:定位方法
                value:元素位置
        :return:element:定位成功后找到的元素
        """
        element = None

        if by == 'i' or by == 'id':
            try:
                element = self.refind(By.ID, value)
                # element = self.driver.find_element_by_id(value)  # id 定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))  # 并不是每个元素都存在 text 属性
            except NoSuchElementException as e:
                logger.error('[id 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 'n' or by == 'name':
            try:
                element = self.refind(By.NAME, value)
                # element = self.driver.find_element_by_name(value)  # name 名称定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[name 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 'c' or by == 'class_name':
            try:
                element = self.refind(By.CLASS_NAME, value)
                # element = self.driver.find_element_by_class_name(value)  # class 类名称定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[class_name 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 'l' or by == 'link_text':
            try:
                element = self.refind(By.LINK_TEXT, value)
                # element = self.driver.find_element_by_link_text(value)  # 文本超链接定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[link 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 'p' or by == 'partial_link_text':
            try:
                element = self.refind(By.PARTIAL_LINK_TEXT, value)
                # element = self.driver.find_element_by_partial_link_text(value)  # 部分文本超链接定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[partial link 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 't' or by == 'tag_name':
            try:
                element = self.refind(By.TAG_NAME, value)
                # element = self.driver.find_element_by_tag_name(value)  # tag 定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[tag 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 'x' or by == 'xpath':
            try:
                element = self.refind(By.XPATH, value)
                # element = self.driver.find_element_by_xpath(value)  # xpath 定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[xpath 定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        elif by == 's' or by == 'css_selector':
            try:
                element = self.refind(By.CSS_SELECTOR, value)
                # element = self.driver.find_element_by_css_selector(value)  # css 定位
                if element:
                    logger.info('Found the element: \' %s \' successfully! '
                                'by: %s value:%s' % (element.text, by, value))
            except NoSuchElementException as e:
                logger.error('[css selector定位方式]NoSuchElementException:%s' % e)
                self.get_windows_img('find_' + by + '_' + value)
        else:
            logger.error('Please enter a valid type of targeting elements.')
            raise NameError('Please enter a valid type of targeting elements.')

        return element

    # Text input 文本框输入
    def send_keys(self, by, value, text):
        ele = self.find_element(by, value)  # 获取元素位置信息
        if not ele:
            return None
        try:
            ele.clear()  # 文本框清空
            ele.send_keys(text)  # 输入文本信息
            logger.info('Inputted \' %s \' in the inputBox' % text)
            return True
        except NameError as e:
            logger.error('Failed to input \' %s \' in the inputBox: %s' % (text, e))
            self.get_windows_img('sendkey_' + by + '_' + value + '_' + text)

    # Text clear 文本框清空 value:元素位置
    def clear(self, by, value):
        ele = self.find_element(by, value)  # 获取元素位置信息
        if not ele:
            return None
        try:
            ele.clear()
            logger.info('Clear the text in the inputBox [ %s ]' % value)
            return True
        except NameError as e:
            logger.error('Failed to clear the inputBox [ %s ]: %s' % (value, e))
            self.get_windows_img('clear_' + by + '_' + value)

    # Text click 点击事件 value:元素位置
    def click(self, by, value):
        ele = self.find_element(by, value)  # 获取元素位置信息
        if not ele:
            return None
        try:
            ele.click()
            logger.info('The element [ %s ] was clicked' % value)
            return True
        except NameError as e:
            logger.error('Failed to click the element [ %s ]: %s' % (value, e))
            self.get_windows_img('click_' + by + '_' + value)

    def get_attribute(self, by, value, attr):
        ele = self.find_element(by, value)  # 获取元素位置信息
        if not ele:
            return None
        try:
            attr_value = ele.get_attribute(attr)
            logger.info('The attr_value for the element [ %s ] was gained:%s' % (value, attr_value))
            return attr_value
        except NameError as e:
            logger.error('Failed to get the attr_value for the element [ %s ]: %s' % (value, e))
            self.get_windows_img('getattr_' + by + '_' + value + '_' + attr)

    def execute_script(self, js=''):
        try:
            logger.info('Script will be execute: %s' % js)
            return self.driver.execute_script(js)
        except Exception as e:
            logger.error('Failed to execute script [ %s ]: %s' % (js, e))
            self.get_windows_img('execute_script_' + js)

    def set_window_size(self, n, m):
        try:
            logger.info('Window will be set: %s*%s' % (n, m))
            # 分辨率 宽*高
            return self.driver.set_window_size(int(n), int(m))
        except Exception as e:
            logger.error('Failed to set the window size %s*%s: %s' % (n, m, e))
            self.get_windows_img('setwinsize' + n + '_' + m)

    # def get_window_size(self):
    def get_window_size(self, win_size_dict):
        try:
            logger.info('Current window size is %s' % self.driver.get_window_size())
            tmp_dict = self.driver.get_window_size()
            win_size_dict['width'] = tmp_dict['width']
            win_size_dict['height'] = tmp_dict['height']
            # 分辨率 宽*高
            return self.driver.get_window_size()
        except Exception as e:
            logger.error('Failed to get the window size: %s' % e)
            self.get_windows_img('getwinsize')

    def maximize_window(self):
        try:
            logger.info('Window will be maximized')
            return self.driver.maximize_window()
        except Exception as e:
            logger.error('Failed to maximize the window: %s' % e)
            self.get_windows_img('maximize_window')

    def back(self):
        try:
            logger.info('Window will be back')
            return self.driver.back()
        except Exception as e:
            logger.error('Failed to back: %s' % e)
            self.get_windows_img('back')

    def forward(self):
        try:
            logger.info('Window will be forward')
            return self.driver.forward()
        except Exception as e:
            logger.error('Failed to forward: %s' % e)
            self.get_windows_img('forward')

    def refresh(self):
        try:
            logger.info('Window will be refreshed')
            return self.driver.refresh()
        except Exception as e:
            logger.error('Failed to refresh: %s' % e)
            self.get_windows_img('refresh')

    def close(self):
        try:
            logger.info('Window will be closed')
            return self.driver.close()
        except Exception as e:
            logger.error('Failed to close the window: %s' % e)
            self.get_windows_img('close')

    def current_url(self):
        try:
            logger.info('Current page url is %s' % self.driver.current_url)
            return self.driver.current_url
        except Exception as e:
            logger.error('Failed to get page url: %s' % e)
            self.get_windows_img('geturl')

    # get_url_title 获取网页标题
    def get_url_title(self):
        try:
            logger.info('Current page title is %s' % self.driver.title)
            return self.driver.title
        except Exception as e:
            logger.error('Failed to get page title: %s' % e)
            self.get_windows_img('gettitle')

    def switch_to_frame(self, value):
        try:
            logger.info('[switch_to_frame]Current frame will be %s' % value)
            return self.driver.switch_to.frame(value)
        except Exception as e:
            logger.error('Failed to switch to the frame %s: %s' % (value, e))

    def switch_frame(self, by='i', value=''):
        try:
            logger.info('[switch_frame]Current frame will be %s' % value)
            frame = self.find_element(by, value)
            return self.switch_to_frame(frame)
        except Exception as e:
            logger.error('Failed to switch to the frame %s: %s' % (value, e))

    def switch_to_default_content(self):
        try:
            logger.info('Current frame will be default content')
            return self.driver.switch_to.default_content()
        except Exception as e:
            logger.error('Failed to switch to the default frame: %s' % e)

    def switch_to_parent_frame(self):
        try:
            logger.info('Current frame will be parent frame')
            return self.driver.switch_to.parent_frame()
        except Exception as e:
            logger.error('Failed to switch to the parent frame: %s' % e)

    def current_window_handle(self, handle_list=None):
        try:
            if handle_list is None:
                handle_list = []
                handle_list.append(0)
            handle_list[0] = self.driver.current_window_handle
            logger.info('Get the current window handle:%s' % self.driver.current_window_handle)
            return handle_list[0]
        except Exception as e:
            logger.error('Failed to get the current window handle: %s' % e)

    def window_handles(self):
        try:
            logger.info('Get all window handles:%s' % self.driver.window_handles)
            return self.driver.window_handles
        except Exception as e:
            logger.error('Failed to get all window handles: %s' % e)

    def switch_to_window(self, handle):
        try:
            logger.info('Switch to the window: %s' % handle)
            return self.driver.switch_to.window(handle)
        except Exception as e:
            logger.error('Failed to switch to the window %s: %s' % (handle, e))
            self.get_windows_img('handle_' + handle)

    def switch_window(self, handle_list):
        try:
            if handle_list[0] != 0:
                handles = self.window_handles()
                for h in handles:
                    logger.info('The original window handle:%s' % str(handle_list[0]))
                    logger.info('The current window handle:%s' % h)
                    if h != str(handle_list[0]):
                        self.switch_to_window(h)
                        logger.info('跳转到目的窗口')
            else:
                logger.error('The original window handle:%s' % str(handle_list[0]))
        except Exception as e:
            logger.error('Failed to switch to the window %s: %s' % (handle_list, e))
            self.get_windows_img('handle_' + handle_list)
