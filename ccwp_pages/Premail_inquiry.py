# -*- coding: utf-8 -*-

from lee_selenium import Lee
import time
from selenium.webdriver.common.keys import Keys
import random
import re



class Premail(Lee):

    '''元素定位'''




    inquiry_loc = ("css", ".tips")

    froms_loc=("css",".copy-order")  #寄出0/往1城市


    goods_loc=("css",".cell-extra")  #物品重量和寄件时间


    checkBut_loc=("css",".sf-query-btn>button") #查询按钮/预约寄件


    query_results_loc=("css",".sf-send-before-query-res-content")

    choose_city_loc = ("css", "ul.sf-area-hot-city-content>li")  # 热门城市

    choose_area_loc = ("css", "div.county-column.sf-picker-wrap>div>ul>li")  # 选择县区

    confirm_loc = ("css", "div.sf-popup-footer>button")  # 点击确定



    def __init__(self,driver,addr,email):
        # super(self).__init__(addr,email)
        self.addr = addr
        self.driver = driver
        self.email=email



    def inquiry(self):
        '''点击寄前查询'''
        self.clicks(self.inquiry_loc, 2)

    def froms(self):
        # 点击寄往城市

        self.clicks(self.froms_loc,0)
        time.sleep(1)

        self.addr.choose_city()
        self.addr.choose_area()
        self.addr.confirm()

    def to(self):
        #点击寄出城市
        self.clicks(self.froms_loc,1)
        time.sleep(1)

        self.addr.choose_city()
        self.addr.choose_area()
        self.addr.confirm()

    def item_weight(self):
        #点击物品重量
        self.clicks(self.goods_loc,2)
        time.sleep(1)
        self.email.choose_type()
        self.email.input_name1()
        self.email.input_weight()
        self.email.all_conf()


    def time(self):

        #点击寄件时间
        self.clicks(self.goods_loc,3)
        time.sleep(1)

        self.email.choose_DD2()
        self.email.all_conf()

    def check(self):
        #点击查询按钮
        self.click(self.checkBut_loc)


    def query_results(self):

        #查询结果

        results=self.is_element_exist(".sf-send-before-query-res-content")
        return results

    def send(self):

        self.js_focus_elements(self.checkBut_loc,1)
        self.clicks(self.checkBut_loc,1)



    '''测试用例'''

    def case_01(self):

        self.inquiry()

        self.froms()

        self.to()

        self.item_weight()

        self.time()

        self.check()

        time.sleep(2)

    def case_02(self):

        self.send()

        time.sleep(2)