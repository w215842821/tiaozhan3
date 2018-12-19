# -*- coding: utf-8 -*-

import sys
import csv

#处理命令行参数类
class Args(object):

    def __init__(self):
        self.args = sys.argv[1:]

    '''
    补充
    1.参数读取函数，并返回相应路径
    2.当参数格式出现错误，抛出异常
    '''

#配置文件类
class Config(object):
    
    def __init__(self):
        self.config = self._read_config()

    ＃配置文件读取内部函数
    def _read_config(self):
        config = {}

        '''
        1.根据参数指定的配置文件路径，读取配置文件信息，并写入config字典中去
        2.使用strip()和split()对读取的配置文件去掉空格以及切分
        3.当格式出错时，抛出异常
        '''


#用户数据类，

#税后工资计算类

#执行
