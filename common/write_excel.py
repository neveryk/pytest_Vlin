import re
import xlwt
import xlrd
import os
from xlutils.copy import copy
import random
import datetime
class Write_Datas():
    def get_data(self,account):
        data_list=[["对方行名","对方户名","对方账号","交易流水号","交易日期","交易时间","贷方金额","备注"]]
        Account_name='建行'
        today=20211029
        Serial_number=random.randint(1000000000000000,9999999999999999999)
        time=101506
        money=100000
        data=[Account_name,Account_name,account,Serial_number,today,time,money]
        data_list.append(data)
        return data_list
    def write_excel_xls(self,xls_name, sheet_name, value):
        index=len(value)
        wook=xlwt.Workbook()
        sheet=wook.add_sheet(sheet_name) #创建表单sheet
        for i in range(0,index):
            for j in range(0,len(value[i])):
                sheet.write(i,j,value[i][j])
        wook.save(xls_name)

wri=Write_Datas()
