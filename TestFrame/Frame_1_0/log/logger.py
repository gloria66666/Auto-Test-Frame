# coding=utf-8

import logging
import os.path
import time
from logging import handlers


class Logger(object):

    def get_log(self):
        return self.logger

    def __dir_exist(self, log_path):

        # 判断 logs 文件夹是否创建，未创建则进行创建
        is_exists = os.path.exists(log_path)
        if not is_exists:
            try:
                os.makedirs(log_path)
                return True
            except Exception as e:
                print("创建文件夹失败", e)
                return False
        else:
            return True

    # 初始化加载
    def __init__(self, logger, level, r_mode = True, when = 'D', count = 3):
        # 创建一个 logger 对象
        self.logger = logging.getLogger(logger) # logger 对象为被执行的对象类
        self.logger.setLevel(level) # 设置日志模式为调试模式

        # 创建一个 handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) # 设置日期格式
        log_path = os.path.dirname(os.getcwd()) + '\\logs\\'

        if not self.__dir_exist(log_path):
            return None

        if not r_mode:
            log_name = log_path + rq + '.log'
            # 按次记录日志
            fh = logging.FileHandler(log_name)
            fh.setLevel(level)

            # 创建一个 handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(level)

            # 定义 handler 输出格式
            formatter = logging.Formatter('%(asctime)s '
                                          '- %(name)s '
                                          '- %(filename)s->%(funcName)s[line:%(lineno)d] '
                                          '- %(levelname)s '
                                          '- %(message)s ')

            # formatter = logging.Formatter('''%(asctime)s
            #                               - %(name)s
            #                               - %(filename)s>%(funcName)s[line:%(lineno)d]
            #                               - %(levelname)s
            #                               - %(message)s ''')
            # 2020 - 08 - 17 11: 48:54, 629
            #         - Config
            #         - config_parser.py > value[line:19]
            #         - INFO
            #         - hello
            # 给 handler添加formatter
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger 添加 handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
        else:
            # 按天记录日志，若超过count，则会从最先创建的开始删除
            time_rotating_file_handler = handlers.TimedRotatingFileHandler(
                filename=log_path + 'all.log', when=when, backupCount=count
            )
            time_rotating_file_handler.setLevel(level)
            # 创建一个 handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(level)
            formatter = logging.Formatter('%(asctime)s '
                                          '- %(name)s '
                                          '- %(filename)s->%(funcName)s[line:%(lineno)d] '
                                          '- %(levelname)s '
                                          '- %(message)s ')
            time_rotating_file_handler.setFormatter(formatter)
            ch.setFormatter(formatter)
            self.logger.addHandler(time_rotating_file_handler)
            self.logger.addHandler(ch)