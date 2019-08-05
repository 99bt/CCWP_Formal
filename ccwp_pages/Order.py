# -*- coding: utf-8 -*-

from lee_selenium import Lee
import time
from selenium.webdriver.common.keys import Keys
import random
import re
# from CCWP_New.ccwp_pages.Advance_Mail import AdvanceMail




class Order(Lee):

    '''元素定位'''

    receipt_loc=("css",".sf-icon.icon-my_sf_send_to.sf-icon-custom-color") #我收的

    mailing_loc=("css",".sf-icon.icon-my_sf_send_for.sf-icon-custom-color") #我寄的

    orders_list_loc=("css",".sf-my-exp-tab") #寄/收/订单列表

    cancel_order_loc=("css",".sf-order-cancel") #取消订单/重新下单

    cancel_btn_loc = ("xpath", "//*[@class='sf-message-footer']/button[1]")  # 取消删除

    comfirm_btn_loc = ("css", ".sf-message-footer > button.comfirm-btn")  # 确定删除

    del_orders_loc=("css",".sf-order-delete") #删除订单

    orders_type_loc=("css",".cell-extra") #订单状态

    orders_no_loc=("css","//*[@class='cell-title'][1]") #订单号

    orders_detail_loc=("css",".order-wrapper") #订单详情

    more_loc = ("css", ".sf-icon")  # 查看/收起详情

    names=("css",".name")#寄件人名字
    address=("css","")



    def more(self):
        '''查看/收起更多详情'''
        self.click(self.more_loc)

    def date_time(self):

        '''获得预约上门时间2'''
        self.find_text_css(".date")
        text1 = self.find_text_css(".date")
        self.find_text_css(".time")

        text2 = self.find_text_css(".time")

        return text1.replace(' ', '')+text2.replace(' ', '')

    def sender_name2(self):

        '''获得寄件人姓名2'''

        text = self.find_text_css(".name:nth-child(1)")
        return text

    def sender_detail2(self):

        '''获得寄件人地址2'''

        text = self.finds_text_css(".address",0)
        return text.replace(' ', '')

    def receiver_name2(self):

        '''获得收件人姓名2'''

        text = self.finds_text_css(".name",1)
        return text

    def receiver_detail2(self):

        '''获得收件人地址2'''

        text = self.finds_text_css(".address",1)
        return text.replace(' ', '')

    def order_no(self):

        '''获得订单号2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(1)>span:nth-child(2)")
        return text

    def goods(self):

        '''获得物品类型2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(3)>span:nth-child(2)")
        return text

    def insure_text(self):

        '''获得保价2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(4)>span:nth-child(2)")
        return text

    def pay(self):

        '''获得支付方式2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(5)>span:nth-child(2)")
        return text

    def remarks(self):

        '''获得备注2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(6)>span:nth-child(2)")
        return text





    def receipt(self):

        self.click(self.receipt_loc)

        time.sleep(2)

    def mailing(self):

        self.click(self.mailing_loc)

        time.sleep(3)

    def orders_order(self):

        self.clicks(self.orders_list_loc,2)
        time.sleep(3)

    def cancel_order(self):

        self.clicks(self.cancel_order_loc,0)
        time.sleep(1)


    def cancel_btn(self):
        #取消 取消订单
        self.click(self.cancel_btn_loc)

    def comfirm_btn(self):
        #确定 取消订单

        self.click(self.comfirm_btn_loc)
        time.sleep(1)

    def del_orders(self):

        self.clicks(self.del_orders_loc,0)

        time.sleep(2)

    def order_details(self):

        self.clicks(self.orders_detail_loc,0)
        time.sleep(2)


    def get_orderNo(self):
        text=self.find_text_xpath("//*[@class='cell-title'][1]")
        print(text)
        return re.search('(\w+\d+)', text).group()




    '''操作方法'''

    def Operation_order_1(self):

        self.receipt()

        self.orders_order()

    def Operation_order_2(self):


        self.order_details()

        self.more()

        time.sleep(1)
    def Operation_order_3(self):

        self.back()

        self.del_orders()

        self.comfirm_btn()

        self.back()

        time.sleep(2)






























