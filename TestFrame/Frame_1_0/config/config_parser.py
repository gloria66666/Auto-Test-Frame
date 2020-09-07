# coding=utf-8

import configparser
import os
from TestFrame.Frame_1_0.log.logger import Logger
import logging


# logger = Logger(logger="Config", level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger="Config", level=logging.INFO, r_mode=False).get_log()


class Config(object):
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.file = file

    def get_value(self, section, option):
        try:
            if self._read_file():
                return self.config.get(section, option)
        except Exception as e:
            logger.error('get ini value:%s' % e)

    # def get_value(self, section, option):
    #     if self.has_option(section, option):
    #         if self.config.get(section, option):
    #             return self.config.get(section, option)
    #         else:
    #             print(f"value:{option}'s value doesn't exist")
    #             return None
    #     else:
    #         return None
    #
    # def has_option(self, section, option):
    #     option_list = None
    #     # cf.options(section)：得到section下所有的option，返回小写列表['url']
    #     # cf.items(option)：得到该section所有的键值对，返回小写列表[('url', 'http://www.baidu.com')]
    #     option_list = self.get_options(section)
    #     if option_list and str.lower(option) in option_list:
    #         return option
    #     else:
    #         if option_list:
    #             print(f"option:{option} doesn't exist")
    #         return None
    #
    # def get_options(self, section):
    #     if self.has_section(section):
    #         if self.config.options(section):
    #             return self.config.options(section)
    #         else:
    #             print('There are no options')
    #             return None
    #     else:
    #         return None
    #
    # def has_section(self, section):
    #     section_list = []
    #     section_list = self.get_sections()
    #     if section_list and section in section_list:
    #         return section
    #     else:
    #         if section_list:
    #             print(f"section:{section} doesn't exist")
    #         return None
    #
    # def get_sections(self):
    #     if self._read_file():
    #         if self.config.sections():
    #             return self.config.sections()
    #         else:
    #             print('There are no sections')
    #             return None
    #     else:
    #         return None

    def _read_file(self):
        # os.getcwd()同os.path.abspath('.')，返回当前工作目录I:\Python3\TestFrame\Frame_1_0\config
        os.chdir(os.path.dirname(os.path.abspath('.')) + '/config')

        if self.config.read(self.file): # 文件不存在不会抛出异常
            # 对于有BOM（如Windows下用记事本指定为utf-8）的文件，需要使用utf-8-sig
            return self.config.read(self.file, encoding='utf-8')
        else:
            logger.error(f"file:{self.file} dosen't exist")
            return None

