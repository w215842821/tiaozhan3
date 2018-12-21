# -*- coding: utf-8 -*-

import sys
import csv

#处理命令行参数类
class Args(object):
    
    def __init__(self):
        #命令行参数列表，初始化
        self.args = sys.argv[1:]

    #获取命令参数后面的文件名,
    def _value_after_option(self, option):

        index = self.args.index(option)
        return self.args[index + 1]


    #定位配置文名件'-c'，为后面可读提供路径
    def config_path(self):
        return self._value_after_option('-c')
        
    #定位用户工资文名件'-d'，为后面可读提供路径
    def userdata_path(self):
        
        return self._value_after_option('-d')
        
    #定位税后工资文件名，为后面可读提供路径
    def  export_path(self):
        return self._value_after_option('-o')


    '''
    补充
    1.参数读取函数，并返回相应路径
    2.当参数格式出现错误，抛出异常
    '''

args = Args()

#配置文件类
class Config(object):
    
    def __init__(self):
        self.config = self._read_config()

    ＃配置文件读取内部函数
    def _read_config(self):
        config = {}
        with open(args.config_path) as f:
            for line in f.readlines():
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()

        return config

    def _get_config(self,key):
        
        return self.config[key]

    def soical_insurance_baseline_low(self):

        return _get_config('JiShuL')

    def soical_insurance_baseline_high(self):

        return _get_config('JiShuH')

    def soical_insurance_tatal_rate(self):

        return sum([
            _get_config('YangLao'),
            _get_config('YiLiao'),
            _get_config('ShiYe'),
            _get_config('GongShang'),
            _get_config('ShengYu')
            _get_config('GongJiJin')
            ])
        

        '''
        1.根据参数指定的配置文件路径，读取配置文件信息，并写入config字典中去
        2.使用strip()和split()对读取的配置文件去掉空格以及切分
        3.当格式出错时，抛出异常
        '''


#用户数据类，
class userData(object):
    """docstring for userData"""
    def __init__(self, arg):
        pass

    def _read_user_data(self):
        userdata = []
        with open(arg.userdata_path) as f:
            for line in f.readlines():
                employee_id, income_string = line.strip().split(',')
            userdata.append((employee_id, income_string))

        return userdata
        


#税后工资计算类
class IncomeTaxCaculator(object):
    
    def __init__(self):
        self.userdata = userdata
        


#执行
