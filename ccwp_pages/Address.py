# -*- coding: utf-8 -*-

from lee_selenium import Lee
import time
from selenium.webdriver.common.keys import Keys
import random
import re


class Address(Lee):

    '''元素定位'''

    # -------------
    # def __init__(self,driver):
    #     """启动浏览器参数化，默认启动谷歌"""
    #     self.driver=driver

    send_loc = ("css", ".tips")  # 预约寄件

    more_detail_loc = ("css", ".sf-collapse-item-custom-cell >span")  # 完善/收起包裹详情

    input_name_loc = ("css", ".sf-input-wrap>input")  # 姓名

    input_phone_loc = ("css", ".sf-input-wrap>input")  # 电话

    clink_city_loc = ("css", ".van-field__control:nth-child(1)")  # 城市

    choose_city_loc = ("css", "ul.sf-area-hot-city-content>li")  # 热门城市

    choose_area_loc = ("css", "div.county-column.sf-picker-wrap>div>ul>li")  # 选择县区

    confirm_loc = ("css", "div.sf-popup-footer>button")  # 点击确定

    detailed_addr_loc = ("css", ".detailsVal")  # 详细地址

    Address_entry_loc = ("css", ".van-cell__value>div>textarea")  # 详细地址录入

    add_but_loc = ("css", ".sf-address-btn")  # 详细地址录入的确定按钮

    preserve_addr_loc = ("css", ".van-checkbox__label>span")  # 保存到地址簿

    clear_message_loc = ("css", ".protocol-wrap>button")  # 清空当前信息

    clink_preserve_loc = ("css", ".sf-address-edit-btn")  # 保存按钮
    # -------------

    receiver_loc = ("class name", "sf-post-card-receiver-no-switch")  # 收件人地址

    receiver_addr_loc = ("css", ".sf-post-card-receiver>span")  # 收件人地址簿

    sender_addr_loc = ("css", ".sf-post-card-poster>span")  # 寄件人地址簿
    # -------
    new_address_loc = ("css", ".sf-address-list-check-address>button:nth-child(1)")  # 新建地址

    del_address_loc = ("xpath", "//*[@class='sf-address-item-editor']/span[2]")  # 删除地址

    cancel_btn_loc = ("xpath", "//*[@class='sf-message-footer']/button[1]")  # 取消删除


    comfirm_btn_loc = ("css", ".sf-message-footer > button.comfirm-btn")  # 确定删除

    edit_address_loc = ("css", ".sf-address-item-editor>span:nth-child(1)")  # 编辑地址


    choose_addr_loc = ("css", ".sf-address-item-details")  # 选择地址s

    sender_loc = ("class name", "sf-post-card-sender-no-switch")  # 寄件人地址




    cancel_default_loc = ("link text", "取消默认")  # 取消默认

    set_default_loc = ("link text", "设为默认")  # 设为默认s

    all_conf_loc = ("css", ".sf-popup-footer>button")  # 确定 （以下确定的定位元素共用这个）
    # ----------------------

    sender_nameNO_loc = ("css", ".name:nth-child(1)")  # 寄件人姓名

    sender_detailNO_loc = ("css", ".sf-post-card-details-address")  # 寄件人地址

    receiver_nameNO_loc = ("css", ".name:nth-child(2)")  # 收件人姓名

    receiver_detailNO_loc = ("css", ".sf-post-card-details-address")  # 收件人地址

    # sender_detailNO_loc=("css",".sf-post-card-sender-no-switch>label>span:nth-child(1)")  #寄件人地址
    #
    # receiver_nameNO_loc=("css",".sf-post-card-receiver-no-switch>label>span:nth-child(2)")  #收件人姓名
    #
    # receiver_detailNO_loc=("css",".sf-post-card-receiver-no-switch>label>span:nth-child(2)")  #收件人地址

    switch_addrNO_loc = ("css", ".icon-order_ic_sendend2x")  # 切换收寄件人地址

    # receiver_name_loc=("css",".sf-post-card-receiver-switch>label>span:nth-child(1)")  #寄件人姓名
    #
    # receiver_detail_loc=("css",".sf-post-card-receiver-switch>label>span:nth-child(1)")  #寄件人地址
    #
    sender_name_loc = ("css", ".sf-post-card-sender-switch>label>span:nth-child(2)")  # 收件人姓名
    #
    # sender_detail_loc=("css",".sf-post-card-sender-switch>label>span:nth-child(2)")  #收件人地址


    # ------

    input_smartWrite_loc= ("css", ".van-field__control")  #输入智能填写内容

    clear_loc=("css",".IntelligenceInput_bottom>span")  #清空智能填写

    smartWrite_loc= ("css",".IntelligenceInput_bottom_button")  #点击智能填写


    click_smartSearch_loc=("css",".sf-icon-select.icon-search") #点击智能搜索

    input_smartSearch_loc=("css",".van-field__control") #输入搜索内容

    cancel_smartSearch_loc=("css",".sf-search-btn")  # 取消智能搜索

    list_phone=("css",".phone")

    ok_loc=("css",".sf-message-footer")

    repeat_loc=("css",".sf-message")

    def send(self):
        '''点击预约寄件'''
        self.clicks(self.send_loc, 1)

    def more_detail(self):
        '''点击完善/收起包裹详情'''

        self.click(self.more_detail_loc)
        time.sleep(1)
        self.click(self.more_detail_loc)
        time.sleep(1)
        self.click(self.more_detail_loc)
        time.sleep(1)


    def sender(self):
        '''寄件人地址'''
        self.click(self.sender_loc)
        time.sleep(2)

    def receiver(self):
        '''收件人地址'''
        self.click(self.receiver_loc)

    def sender_addr(self):
        '''点击寄件人地址簿'''
        self.click(self.sender_addr_loc)
        time.sleep(2)

    def choose_addr(self):
        '''随机选择寄件地址'''
        elements = self.find_elements(self.choose_addr_loc)
        print("地址数量",len(elements))

        if len(elements) <1:

            self.new_addr()

            self.all_edit_addr()

        else:

            self.js_focus_elements_suji(self.choose_addr_loc)
            # self.clicks(self.choose_addr_loc,0)
            time.sleep(1)
            text = self.is_or_elements(self.repeat_loc)
            print("地址是否已经被选中",text)
            if text:
                self.click(self.ok_loc)
                time.sleep(1)
                self.js_focus_elements_suji(self.choose_addr_loc)
                time.sleep(2)



    def clink_searchAdd(self):

        elements = self.find_elements(self.choose_addr_loc)

        if len(elements) < 0:
            self.new_addr()

            self.all_edit_addr()
        else:
            self.js_focus_elements_suji(self.choose_addr_loc)
            time.sleep(1)
            text = self.is_or_elements(self.repeat_loc)
            print("地址是否已经被选中", text)
            if text:
                self.click(self.ok_loc)
                time.sleep(1)
                self.js_focus_elements_suji(self.choose_addr_loc)
                time.sleep(1)


    def receiver_addr(self):
        '''点击收件人地址簿'''
        self.click(self.receiver_addr_loc)
        time.sleep(2)

    def edit_addr(self):

        '''点击编辑地址'''
        lenght=len(self.find_elements(self.edit_address_loc))
        if lenght<=0:
            self.new_addr()
            self.all_edit_addr()

        else:

            self.js_focus_elements_suji(self.edit_address_loc)
            time.sleep(1)

    def new_addr(self):
        '''点击新建地址'''

        self.click(self.new_address_loc)
        time.sleep(1)

    def del_addr(self):
        '''删除地址'''

        lenght = len(self.find_elements(self.edit_address_loc))
        if lenght <= 0:
            self.new_addr()
            self.all_edit_addr()
        self.js_focus_elements_suji(self.del_address_loc)
        time.sleep(1)
        self.click(self.cancel_btn_loc)

        self.js_focus_elements_suji(self.del_address_loc)
        time.sleep(1)
        self.click(self.comfirm_btn_loc)

    def del_addr_com(self):

        lenght = len(self.find_elements(self.edit_address_loc))
        if lenght <= 0:
            self.new_addr()
            self.all_edit_addr()

        self.js_focus_elements_suji(self.del_address_loc)
        time.sleep(1)
        self.click(self.comfirm_btn_loc)
        # self.refresh()
        # time.sleep(2)

    '''新建地址'''

    def input_name(self):

        text = random.randint(0, 800)
        text_ = "测试订单%s" % text
        self.sends_keys(self.input_name_loc, 0, text_)


    def input_name2(self):

        text = random.randint(0, 800)

        self.sends_keys(self.input_name_loc, 0, "测试订单%s佩奇" % text)

    def input_phone(self):

        text = random.randint(100, 999)
        self.sends_keys(self.input_phone_loc, 1, '18825625%s' % text)

    def input_phone2(self):

        text = random.randint(100, 999)
        self.sends_keys(self.input_phone_loc, 1, '17756856%s' % text)

    def clink_city(self):

        self.click(self.clink_city_loc)
        time.sleep(3)

    def choose_city(self):
        '''随机选择热门城市'''
        # self.random_randint_datail(self.choose_city_loc)
        suji = self.random_randint(self.choose_city_loc)
        print("城市随机数-----", suji)
        self.js_focus_elements(self.choose_city_loc, suji)
        self.clicks(self.choose_city_loc, suji)
        time.sleep(4)

    def choose_area(self):

        suji = self.random_randint(self.choose_area_loc)
        print("县区随机数----", suji)
        # self.random_randint_datail(self.choose_area_loc)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.js_focus_elements(self.choose_area_loc, suji)
        self.clicks(self.choose_area_loc, suji)
        time.sleep(1)

    def confirm(self):
        '''确定'''

        self.click(self.confirm_loc)
        time.sleep(1)

    def detailed_addr(self):

        self.click(self.detailed_addr_loc)
        time.sleep(1)

        text = random.randint(100, 999)

        self.sends_keys(self.Address_entry_loc, 2, "%s-beautiful日照香炉生紫烟-遥看瀑布挂前窗" % text)
        time.sleep(2)

        self.click(self.add_but_loc)
        time.sleep(2)

    def detailed_addr2(self):

        self.click(self.detailed_addr_loc)
        time.sleep(1)

        text = random.randint(100, 999)
        self.sends_keys(self.Address_entry_loc, 2, "%s-lucky98796飞流直下三千尺-疑似银河落九天" % text)
        time.sleep(1)

        self.click(self.add_but_loc)
        time.sleep(2)

    def preserve_addr(self):
        # 保存到地址簿
        self.click(self.preserve_addr_loc)
        time.sleep(1)

    def clear_message(self):

        self.click(self.clear_message_loc)

    def clink_preserve(self):
        '''保存按钮'''
        self.click(self.clink_preserve_loc)
        time.sleep(1)

    def cancel_default(self):
        '''取消默认'''
        self.click(self.cancel_default_loc)

    def set_default(self):

        self.click(self.set_default_loc)

    def clink_sender_name(self):

        '''切换地址后，点击收件人地址'''
        self.click(self.sender_name_loc)





    def sender_nameNO(self):

        '''获得寄件人姓名'''


        text=self.find_text_css(".name:nth-child(1)")
        return text

    def sender_detailNO(self):

        '''获得寄件人地址'''


        text=self.find_text_xpath("//*[@class='sf-post-card-details-address'][1]")
        return text

    def receiver_nameNO(self):

        '''获得收件人姓名'''


        text = self.finds_text_css(".name",1)
        return text

    def receiver_detailNO(self):

        '''获得收件人地址'''


        text = self.finds_text_css(".sf-post-card-details-address",1)
        return text

    def switch_addrNO(self):
        '''点击切换收寄件人地址'''
        self.click(self.switch_addrNO_loc)
        time.sleep(2)
    def get_detailsVal(self):
        text = self.find_text_css(".detailsVal",)
        return text

    # def receiver_name(self):
    #
    #     '''获得寄件人姓名'''
    #     self.get_attribute(self.receiver_name_loc, "text")
    #
    # def receiver_detail(self):
    #
    #     '''获得寄件人地址'''
    #     self.get_attribute(self.receiver_detail_loc, "text")
    #
    # def sender_name(self):
    #
    #     '''获得收件人姓名'''
    #     self.get_attribute(self.sender_name_loc, "text")
    #
    # def sender_detail(self):
    #
    #     '''收件人地址'''
    #     self.get_attribute(self.sender_detail_loc, "text")


    def input_smartWrite(self):

        # 输入智能填写
        text = random.randint(100, 999)
        self.sends_keys(self.input_smartWrite_loc,1,"杨测试单，15855569%s ， 广东省深圳市南山区南山街道辅导书及附件飞机都是是坚实的覅大V机会的ujvci不会的空间吧是"%text)

        time.sleep(1)

    def clear_smartWrite(self):
        # 清空智能填写
        self.click(self.clear_loc)

    def clink_smartWrite(self):

        #点击智能填写
        self.click(self.smartWrite_loc)

    def get_smartWrite(self):

        # 获得默认的智能填写文案

        text=self.find_text_css(".van-field__control:nth-child(2)")

        return text.replace(' ', '')

    def click_smartSearch(self):

        self.click(self.click_smartSearch_loc)

    def input_smartSearch(self):


        elements=self.find_elements(self.list_phone)
        suiji = random.randint(1, len(elements) - 1)
        phone_list=self.finds_text_css(".phone",suiji)
        phone=re.search("(\d{3})", phone_list).group(1)

        self.send_keys(self.input_smartSearch_loc, phone)

        time.sleep(2)





    '''操作方法'''

    def all_edit_addr(self):

        #新增寄件人地址
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)

        self.input_name()

        self.input_phone()

        self.clink_city()

        self.choose_city()

        self.choose_city()

        self.choose_area()

        self.confirm()

        self.detailed_addr()

        self.clink_preserve()

    def all_edits_addr(self):

        # 新增寄件人地址
        time.sleep(1)

        self.input_name()

        self.input_phone()

        self.clink_city()

        self.choose_city()

        self.choose_city()

        self.choose_area()

        self.confirm()

        self.detailed_addr()

        self.preserve_addr()

        self.clink_preserve()

    def all_edit2_addr(self):

        # 编辑收件人地址

        self.input_name2()

        self.input_phone2()

        self.clink_city()

        self.choose_city()

        self.choose_area()

        self.confirm()

        self.detailed_addr2()

        self.clink_preserve()

    def all_edits2_addr(self):

        # 编辑收件人地址----编辑收件人地址的区别在于，带S是点击保存到地址簿
        # self.input_name2()

        # self.input_phone2()

        # self.clink_city()

        # self.choose_city()

        # self.choose_area()

        # self.confirm()

        # self.detailed_addr2()

        self.input_smartWrite()

        self.clear_smartWrite()

        # default=self.get_smartWrite()
        #
        # assert default=="粘贴如“深圳市南山区深圳大学张兰18236541236”的信息"

        self.input_smartWrite()

        self.clink_smartWrite()

        self.preserve_addr()

        self.clink_preserve()


    def new_sender(self):
        '''点击预约寄件-预约单'''
        # self.send()

        # time.sleep(2)

        '''点击寄件人地址簿'''
        self.sender_addr()

        self.click_smartSearch()

        self.input_smartSearch()

        #点击搜索出来的地址
        self.clink_searchAdd()

        time.sleep(1)

        self.sender_addr()
        time.sleep(2)

        '''删除地址'''
        self.del_addr()
        time.sleep(1)

        self.del_addr_com()
        time.sleep(1)
        '''返回寄件页面，刷新页面，点击寄件人地址蒲'''
        self.back()
        time.sleep(1)


        self.refresh()
        time.sleep(2)

        self.sender_addr()

        '''新建寄件人地址'''
        self.new_addr()

        self.all_edit_addr()

        '''编辑寄件人地址'''

        self.sender_addr()

        self.edit_addr()

        self.clear_message()


        self.all_edit_addr()
        time.sleep(1)

        '''点击收件人地址'''
        self.receiver()
        time.sleep(2)

        self.all_edit2_addr()
        time.sleep(1)

        '''编辑收件人地址--使用智能填写'''

        self.receiver()
        time.sleep(2)

        self.all_edits2_addr()
        time.sleep(1)

        self.more_detail()
        time.sleep(1)

    def book_sender(self):

        '''点击预约寄件-实时单'''
        self.send()


        '''点击寄件人地址簿删除地址'''
        self.sender_addr()

        '''删除地址'''
        self.del_addr()
        time.sleep(1)


        '''返回寄件页面，刷新页面，'''
        self.back()

        self.refresh()
        time.sleep(2)

        '''点击寄件人地址'''
        self.sender()

        self.all_edits_addr()
        time.sleep(2)


        '''点击收件人地址簿'''

        self.receiver_addr()

        self.choose_addr()

        # self.receiver_addr()

        # '''新建地址'''
        # self.new_addr()
        #
        # self.all_edit2_addr()
        '''编辑地址'''

        self.receiver_addr()

        self.edit_addr()

        self.clear_message()

        self.all_edit2_addr()

        '''切换收寄件地址'''

        self.switch_addrNO()

        self.more_detail()
