#!/usr/bin/env python3

import sys
import csv
from collections import namedtuple

Item = namedtuple(
    'Item',
    ['start_point', 'tax_rate', 'quick_sub']
)

START_POINT = 3500

ITEM_TABLE = [
    Item(80000, 0.45, 13505),
    Item(55000, 0.35, 5505),
    Item(35000, 0.30, 2755),
    Item(9000, 0.25, 1005),
    Item(4500, 0.2, 555),
    Item(1500, 0.1, 105),
    Item(0, 0.03, 0)
]

class Args:
    def __init__(self):
        if len(sys.argv) <2:
            print('Parameter Error27')
            exit(1)
        self.args=sys.argv[1:]

    def get_path(self,option):
        try:
            index=self.args.index(option)
            return self.args[index+1]
        except(ValueError,IndexError):
            print('Parameter Error36') 
            exit(1)       
    
    @property
    def get_config_path(self):
        return self.get_path('-c')
    
    @property
    def get_userdata_path(self):
        return self.get_path('-d')
    
    @property
    def get_gongzi_path(self):
        return self.get_path('-o')

args=Args()

class Config:
    def __init__(self):
        self.config=self._read_config()

    def _read_config(self):
        config={}
        with open(args.get_config_path) as f:
            for line in f.readlines():
                key,value=line.strip().split('=')
                try:
                    config[key.strip()]=float(value)
                except ValueError:
                    print('Parameter Error65')
                    exit(1)
        return config
        
    def _get_config_value(self,key):
        try:
            return self.config[key]
        except KeyError:
            print('Parameter Error73')
            exit(1)

    @property
    def get_Hvalue(self):
        return self._get_config_value('JiShuH')
    
    @property
    def get_Lvalue(self):
        return self._get_config_value('JiShuL')

    @property
    def get_totalrate(self):
        return sum([self._get_config_value('YangLao'),
                    self._get_config_value('YiLiao'),
                    self._get_config_value('ShiYe'),
                    self._get_config_value('GongShang'),
                    self._get_config_value('ShengYu'),
                    self._get_config_value('GongJiJin')]) 

config=Config()



class UserData:
    
    def __init__(self):
        self.userdata=self._read_userdata()
    
    def _read_userdata(self):
        userdata=[] 
        with open(args.get_userdata_path) as f:
            for line in f.readlines():
                user,gongzistr= line.strip().split(',')
                try:
                    gongzi=int(gongzistr)
                except ValueError:
                    print('Paremater Error110')
                    exit()
                userdata.append((user,gongzi))
        return userdata
    def __iter__(self):
        return iter(self.userdata)    
    
ud = UserData()
class Calculate:
    
    @staticmethod
    def calc_baoxian(money):
        if money < config.get_Lvalue:
            return config.get_Lvalue*config.get_totalrate
        if money > config.get_Hvalue:
            return config.get_Hvalue*config.get_totalrate
        else:
            return money*config.get_totalrate
    @classmethod
    def calc_tax_daoshoumoney(cls,money):
        daoshoumoney=money-cls.calc_baoxian(money)
        tax_part=daoshoumoney-START_POINT
        if tax_part <=0:
            return '0.00','{:.2f}'.format(daoshoumoney)
        for x in ITEM_TABLE:
            if tax_part > x.start_point:
                tax=tax_part*x.tax_rate-x.quick_sub
                return '{:.2f}'.format(tax),'{:.2f}'.format(daoshoumoney-tax)
    
    def export_info(self):
        result=[]
        for user,money in ud.userdata:
            data=[user,money]
            tax,daoshoumoney=self.calc_tax_daoshoumoney(money)
            baoxian='{:.2f}'.format(self.calc_baoxian(money))
            data+=[baoxian,tax,daoshoumoney]
            result.append(data)
        return result

    def export(self):
        with open(args.get_gongzi_path,'w') as f:
            w=csv.writer(f)
            w.writerows(self.export_info())

if __name__=='__main__':
    c=Calculate()
    c.export()

