# -*- coding: utf-8 -*-

from lee_selenium import Lee
import time
import re

class CheckMail(Lee):

    '''元素定位'''

    check_loc = ("css", ".tips>span:nth-child(1)")  # 查件s index 0
    input_bno_loc = ("css", ".van-field__control") #运单号 1

    # inputPhone_loc = ("css", ".sf-input") #收/寄件人电话号码后四位 2

    check_but_loc = ("css", ".query-btn") #点击查询按钮

    Bno_loc=("css",".order-number") #路由页面的运单号


    sispTime_loc=("css",".sf-timeline-item-datetime") #路由时间

    checkRecords_loc = ("css", ".cell.cell-with-link") #点击查件记录的运单号

    delBno_loc = ("css", ".delete-record") #删除查件记录

    cancel_btn_loc = ("css", ".cancel-btn")  # 取消删除

    confirm_btn_loc = ("css", ".comfirm-btn")  # 确定删除

    # back_loc=("class name","android.widget.ImageView")

    chechFreight_loc = ("css", "span.navLrig:nth-child(1)")  # 查询运费

    myMail_loc = ("css", "span.navLrig:nth-child(2)")  # 我的快件

    numbers_loc = ("xpath", "//*[@class='van-number-keyboard--default']/div/i[2]")  #数字键盘
    tel_but_loc = ("css", ".tel-btn")    #数字键盘确定按钮
    close_loc=("css",".sf-icon.icon-ic_close2x")

    checked_loc=("css",".van-toast--center>div")



    def check_(self):
        #点击查件
        self.click(self.check_loc)
        time.sleep(2)

    def inputBno(self,Bno):
        #输入运单号
        self.send_keys(self.input_bno_loc,Bno)
        time.sleep(2)

    def get_inputBno(self):

        '''获得运单号'''

        text = self.find_text_css(".order-number")
        a=re.search('(\d+)', text).group()
        return a

    def get_bnoTime(self):

        '''获得路由时间'''
        text=self.find_text_css(".sf-timeline-item-datetime")
        return text



    def check_to(self):
        #点击查询

        self.js_focus_element(self.check_but_loc)
        self.click(self.check_but_loc)
        time.sleep(2)

    def checkRecords(self):


        self.js_focus_elements_suji(self.checkRecords_loc)
        time.sleep(2)

    def delBno(self):

        time.sleep(2)
        self.click(self.delBno_loc)
        time.sleep(1)

    def cancel_btn(self):
        #取消删除
        self.click(self.cancel_btn_loc)

    def comfirm_btn(self):
        #确定删除
        self.click(self.confirm_btn_loc)
        time.sleep(1)



    def number(self):
        # sj = random.randint(0, 9)
        # self.clicks(self.numbers_loc,sj)
        self.click(self.numbers_loc)
        time.sleep(2)

    def tel_but(self):
        self.click(self.tel_but_loc)
        time.sleep(1)

    def close(self):
        self.click(self.close_loc)
        time.sleep(2)

    def checked(self):
        text = self.find_text_css(".van-toast--center>div")
        return text


    '''操作方法'''
    def check_pieces(self):

        self.check_()

        # self.inputBno("231702993089")
        #
        # self.check_to()



    def check_Records_pieces(self):

        # self.back()
        #
        # time.sleep(2)
        #
        # self.checkRecords()
        #
        #
        # self.check_to()
        #
        # self.back()
        #
        # self.delBno()
        #
        # self.comfirm_btn()

        self.inputBno("SF1000407892744")

        self.check_to()

        text=self.is_element_exist(".van-toast.van-toast--text.van-toast--middle")
        print("查件1", text)
        if text:
            print("运单号或联系电话不正确，或者当日查询次数过多")

        else:

            self.tel_but()

            text = self.is_element_exist(".van-toast.van-toast--text.van-toast--center")
            print("查件号码验证", text)
            if text:
                print("请输入手机号后四位")

            checked=self.checked()

            assert "请输入手机号后四位"==checked

            self.close()

    # def check_Records_pieces_01(self):
    #
    #     self.back()
    #
    #     time.sleep(2)
    #
    #     self.checkRecords()
    #
    #     self.check_to()
    #     text = self.is_element_exist(".van-toast.van-toast--text.van-toast--middle")
    #     print("查件", text)
    #     if text:
    #         print("运单号或联系电话不正确，或者当日查询次数过多")
    #
    #     else:
    #
    #
    #         self.back()
    #
    #         self.delBno()
    #
    #         self.comfirm_btn()
    #
    #         self.inputBno("231702993089")
    #
    #     self.check_to()
    #
    #     if text:
    #         print("运单号或联系电话不正确，或者当日查询次数过多")
    #
    #     else:
    #
    #
    #
    #         self.tel_but()
    #
    #         text = self.is_element_exist(".van-toast.van-toast--text.van-toast--center")
    #         print("查件号码验证", text)
    #         if text:
    #             print("请输入手机号后四位")
    #
    #         checked=self.checked()
    #
    #         assert "请输入手机号后四位"==checked
    #
    #         self.close()




