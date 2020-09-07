# coding=utf-8

import time
import json
import xlrd
import os
from xlutils.copy import copy
from TestFrame.Frame_1_0.log.logger import Logger
import logging

# logger = Logger(logger='Excel', level = logging.INFO, when = 'H', count = 4).get_log()
logger = Logger(logger='Excel', level=logging.INFO, r_mode=False).get_log()


class Excel(object):
    def __init__(self, path, name, format_info=True, sheet_name=None, sheet_idx=None, load_time = 10):
        # formatting_info 参数表示保留原数据的样式(如原表格的标黄单元格, 加粗字体等信息的保留)
        self.rd_book = self.open(path, name, format_info=format_info)
        self.wt_book = self.copy(self.rd_book)
        self.path = path + '\\测试结果'
        load_t = 0
        # sheet的索引从0开始
        idx = None
        try:
            if sheet_name:
                while not self.rd_book.sheet_loaded(sheet_name):
                    if load_t < load_time:
                        time.sleep(1)
                        load_t += 1
                        logger.info('Wait %sS for the file to load' % load_t)
                    else:
                        logger.error('Waiting for the file to load has timed out %sS' % load_t)
                        break
                if self.rd_book.sheet_loaded(sheet_name):
                    self.rd_sheet = self.sheet_by_name(self.rd_book, sheet_name)
                    self.nrows = self.rd_sheet.nrows
                    self.ncols = self.rd_sheet.ncols
                    idx = 0
                    for name in self.sheet_names(self.rd_book):
                        if name == sheet_name:
                            break
                        else:
                            idx += 1
            elif sheet_idx:
                while not self.rd_book.sheet_loaded(int(sheet_idx)):
                    if load_t < load_time:
                        time.sleep(1)
                        load_t += 1
                        logger.info('Wait %sS for the file to load' % load_t)
                    else:
                        logger.error('Waiting for the file to load has timed out %sS' % load_t)
                        break
                if self.rd_book.sheet_loaded(int(sheet_idx)):
                    self.rd_sheet = self.sheet_by_index(self.rd_book, sheet_idx)
                    self.nrows = self.rd_sheet.nrows
                    self.ncols = self.rd_sheet.ncols
                    idx = int(sheet_idx)
            else:
                logger.error('Missing parameters: sheet_name or sheet_idx')
                raise TypeError('Missing parameters: sheet_name or sheet_idx')
            if idx != None:
                self.wt_sheet_idx = idx
                self.wt_sheet = self.get_sheet(self.wt_sheet_idx)
            else:
                logger.error('A fault in parameters: sheet_name or sheet_idx')
                raise NameError('A fault in parameters: sheet_name or sheet_idx')
        except Exception as e:
            logger.error('Excel_init:%s' % e)

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

    def open(self, path, name, format_info=True):
        try:
            # 文件夹名、文件名、sheet名、单元格包含中文不需要.decode('utf-8')
            # path = path.decode('utf-8')
            # name = name.decode('utf-8')
            logger.info('Excel file [%s] will be open' % os.path.join(path, name))
            # formatting_info=True 是用来保存Excel原格式(如原表格的标黄单元格, 加粗字体等信息的保留)
            # 文件必须是xls
            return xlrd.open_workbook(os.path.join(path, name), formatting_info=format_info)
        except Exception as e:
            logger.error('Failed to open the excel file [%s] : %s' % (os.path.join(path, name), e))

    def copy(self, book):
        try:
            logger.info('Excel file will be copy')
            return copy(book)
        except Exception as e:
            logger.error('Failed to copy the excel file : %s' % e)

    def sheet_by_name(self, book, name):
        try:
            # name = name.decode('utf-8')
            logger.info('Get the sheet : [%s]' % name)
            return book.sheet_by_name(name)
        except Exception as e:
            logger.error('Failed to get the sheet [%s]: %s' % (name, e))

    def sheet_by_index(self, book, idx):
        try:
            logger.info('Get the sheet : [%s]' % idx)
            return book.sheet_by_index(int(idx))
        except Exception as e:
            logger.error('Failed to get the sheet [%s]: %s' % (idx, e))

    def sheet_names_str(self, book):
        try:
            logger.info('[sheet_names_str]Get all sheet names (string)')
            # encoding="utf-8"，用utf8来encode中文
            # json.dumps 序列化时对中文默认使用的ascii编码，想输出真正的中文需要指定ensure_ascii=False
            # 避免输出中文乱码
            return json.dumps(book.sheet_names(),encoding='utf-8',ensure_ascii=False)
        except Exception as e:
            logger.error('Failed to get all sheet names (string): %s' % e)

    def sheet_names(self, book):
        try:
            logger.info('[sheet_names]Get all sheet names (dict)')
            return book.sheet_names()
        except Exception as e:
            logger.error('Failed to get all sheet names (dict): %s' % e)

    def cell_value(self, row, col):
        try:
            # 常用单元格中的数据类型
            # 0 empty, 1 string（text, 2 number, 3 date, 4 boolean, 5 error，6 blank
            logger.info('The cell_type: %s' % self.rd_sheet.cell_type(int(row), int(col)))
            logger.info('Get this cell_value: [%s]row-[%s]col' % (row, col))
            return self.rd_sheet.cell_value(int(row), int(col))
        except Exception as e:
            logger.error('Failed to get the cell_value [%s]row-[%s]col: %s' % (row, col, e))

    def get_sheet(self, idx):
        try:
            logger.info('Get the wt_book\'s sheet: [%s]' % idx)
            return self.wt_book.get_sheet(int(idx))
        except Exception as e:
            logger.error('Failed to get the wt_book\'s sheet [%s]: %s' % (idx, e))

    def write(self, row, col, value):
        try:
            logger.info('Write to the wt_book\'s sheet [%s]: '
                        '[%s]row-[%s]col=[%s]' % (self.wt_sheet_idx, row, col, value))
            return self.wt_sheet.write(int(row), int(col), value)
        except Exception as e:
            logger.error('Failed to write to the wt_book\'s sheet [%s]: '
                         '[%s]row-[%s]col=[%s]: %s' % (self.wt_sheet_idx, row, col, value, e))

    def save(self):
        try:
            logger.info('Save the wt_book: [%s]' % self.wt_sheet_idx)
            if self.__dir_exist(self.path):
                rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
                file_name = rq + '的测试结果.xls'
                return self.wt_book.save(os.path.join(self.path, file_name))
        except Exception as e:
            logger.error('Failed to save the wt_book[%s]: %s' % (self.wt_sheet_idx, e))


