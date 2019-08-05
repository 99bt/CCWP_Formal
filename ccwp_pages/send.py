# -*- coding: utf-8 -*-
from lee_selenium import Lee
import time
from selenium.webdriver.common.keys import Keys
import random
import re


class send_Mail(Lee):
    '''寄件元素定位'''

    account = ("css", ".phone>span:nth-child(2)")  # 判断账号是否存在

    # send_loc=("class name","tips") #预约寄件

    send_loc = ("css", ".tips")  # 预约寄件
    sender_addr_loc = ("css", ".sf-post-card-poster>span")  # 寄件人地址簿

    '''操作方法'''

    def send(self):
        '''点击预约寄件'''
        self.clicks(self.send_loc,1)

    def sender_addr(self):
        '''点击寄件人地址簿'''
        self.click(self.sender_addr_loc)