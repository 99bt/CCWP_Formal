# -*- coding: utf-8 -*-
from lee_selenium import Lee
import time
from selenium.webdriver.common.keys import Keys
import random
import re



class AdvanceMail(Lee):
    '''元素定位'''


    '''寄件元素定位'''

    account = ("css", ".phone>span:nth-child(2)")  # 判断账号是否存在

    # send_loc=("class name","tips") #预约寄件

    send_loc = ("css", ".tips")  # 预约寄件

    more_detail_loc = ("css", ".sf-collapse-item-custom-cell >span")  # 完善/收起包裹详情

    clink_time_loc = ("css", ".cell-extra:nth-child(1)")  # 点击预约取件时间

    choose_DD1_loc = ("css", ".sf-date-wrap>button:nth-child(1)")  # 今天
    choose_DD2_loc = ("css", ".sf-date-wrap>button:nth-child(2)")  # 明天
    choose_DD3_loc = ("css", ".sf-date-wrap>button:nth-child(3)")  # 后天

    choose_HHs_loc = ("css", ".sf-picker-column-item")  # 选择时间段s


    all_conf_loc = ("css", ".sf-popup-footer>button")  # 确定 （以下确定的定位元素共用这个）

    # ------------------

    clink_type_loc = ("css", ".cell-extra")  # 点击物品类型

    choose_types_loc = ("css", ".sf-checkbox-label-tab")  # 选择包裹类型

    input_name1_loc = ("css", ".van-field__control")  # 输入其他物品名称

    input_weight_loc = ("css", ".sf-stepper>label>input")  # 输入重量

    more_number_loc = ("css", ".sf-stepper>button")  # 添加重量

    less_number_loc = ("css", ".sf-stepper>button")  # 减少重量

    # -------------------------

    clink_payway_loc = ("xpath", "//*[@class='cell-group']/div[2]")  # 点击支付方式

    choose_pays_loc = ("css", ".sf-radio-label")  # 选择支付类型
    # -------------------------
    clink_insurance_loc = ("css", ".cell.cell-with-link")  # 点击保价

    input_insurance_loc = ("css", ".sf-price-protection-content>label>input")  # 输入保价费用

    insurance_amount_loc = ("css", ".cell-extra:nth-child(4)")  # 保价金额

    # -------------------------

    clink_remarks_loc = ("css", ".leave-msg.cell.cell-with-link")  # 点击留言

    choose_remarks_loc = ("css", ".sf-checkbox-label-tab")  # 选择留言类型

    input_remarks_loc = ("css", ".sf-input-wrap>textarea")  # 输入留言内容

    # clink_express_loc = ("css", ".cell-extra")  # 点击顺丰服务

    choose_express_loc = ("css", ".sf-price-freight")  # 选择顺丰类型

    # close_express_loc = ("css", ".sf-icon.icon-ic_close2x") #关闭顺丰类型



    express_amount_loc = ("css", ".cell-extra:nth-child(6)")  # 快递金额

    agree_item_loc = ("css", ".sf-popup-footer>button:nth-child(2)")  # 同意条款

    all_amount_loc = ("css", ".price-wrap")  # 总金额

    order_now_loc = ("css", ".sf-exp-reservation-comfirm-btn>span")  # 立即下单
    # ".sf-exp-reservation-comfirm-btn>span:nth-child(1)"


    cancel_btn_loc = ("xpath", "//*[@class='sf-message-footer']/button[1]")  # 取消删除


    comfirm_btn_loc = ("css", ".sf-message-footer > button.comfirm-btn")  # 确定删除

    '''预约成功页面'''

    date_time_loc = ("css", ".date")  # 预约上门时间

    receiver_name2_loc = ("css", ".name:nth-child(1)")  # 寄件人姓名

    receiver_detail2_loc = ("css", ".address:nth-child(1)")  # 寄件人地址

    sender_name2_loc = ("css", ".name:nth-child(2)")  # 收件人姓名

    sender_detail2_loc = ("css", ".address:nth-child(2)")  # 收件人地址

    more_loc = ("css", ".sf-icon")  # 查看/收起详情

    order_no_loc = ("css", ".sf-collapse-item-content>ul>li:nth-child(1)>span:nth-child(2)")  # 订单号

    goods_loc = ("css", ".sf-collapse-item-content>ul>li:nth-child(3)>span:nth-child(2)")  # 物品类型

    isure_loc = ("css", ".sf-collapse-item-content>ul>li:nth-child(4)>span:nth-child(2)")  # 保价

    pay_loc = ("css", ".sf-collapse-item-content>ul>li:nth-child(5)>span:nth-child(2)")  # 支付方式

    remarks_loc = ("css", ".sf-collapse-item-content>ul>li:nth-child(6)>span:nth-child(2)")  # 备注

    less_loc = ("css", ".sf-collapse-item-icon-rotate")  # 收起详情

    cancel_order_loc = ("css", ".sf-footer-btn>button:nth-child(1)")  # 取消订单

    cancels_reason_loc = ("css", ".sf-radio")  # 取消原因

    cancel_sub_loc = ("css", ".sf-order-cancel-content-wrap>button")  # 提交

    no_cancel_btn_loc = ("css", ".cancel-btn")  # 不取消订单

    confirm_btn_loc = ("css", ".comfirm-btn")  # 确定取消订单

    package_loc = ("css", ".sf-footer-btn>button:nth-child(2)")  # 完善包裹信息/返回首页

    # ------------------

    clink_type2_loc = ("css", ".cell-extra:nth-child(1)")  # 点击物品类型

    clink_payway2_loc = ("css", ".cell-extra:nth-child(2)")  # 点击支付方式

    clink_insurance2_loc = ("css", ".cell-extra:nth-child(3)")  # 点击保价

    clink_remarks2_loc = ("css", ".cell-extra:nth-child(4)")  # 点击留言

    package_conf_loc = ("css", ".sf-improve-exp-info>button")  # 确定

    activity_loc=("css",".activity>div")#是否参与活动

    activity_no_loc=("css",".close-btn")#不参与

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

    def more_detail_(self):
        self.click(self.more_detail_loc)
        time.sleep(1)

    def clink_time(self):
        '''点击预约取件时间'''
        self.click(self.clink_time_loc)
        time.sleep(2)

    def choose_DD1(self):
        self.click(self.choose_DD1_loc)
        time.sleep(1)

    def choose_DD2(self):
        self.click(self.choose_DD2_loc)
        time.sleep(1)

    def choose_DD3(self):
        self.click(self.choose_DD3_loc)
        time.sleep(1)

    def choose_HHs(self):

        # self.js_focus_elements_suji(self.choose_HHs_loc)
        # time.sleep(1)
        suji = self.random_randint(self.choose_HHs_loc)
        print("时间随机数----", suji)
        # self.random_randint_datail(self.choose_area_loc)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.js_focus_elements(self.choose_HHs_loc, suji)
        self.clicks(self.choose_HHs_loc, suji)
        time.sleep(1)

    def all_conf(self):
        '''确定按钮'''
        self.click(self.all_conf_loc)
        time.sleep(3)
    # ------------------

    def clink_type(self):
        '''点击物品类型'''
        self.clicks(self.clink_type_loc, 1)
        time.sleep(2)

    def choose_type(self):

        self.random_randint_datail(self.choose_types_loc)
        time.sleep(1)

    def input_name1(self):

        text = random.randint(0, 500)
        self.send_keys(self.input_name1_loc, "我寄的是棉花%s" % text)

    def input_weight(self):

        text = random.randint(1, 130)
        self.send_keys(self.input_weight_loc, text)
        time.sleep(1)

    def more_number(self):

        self.clicks(self.more_number_loc, 1)
        time.sleep(1)

    def less_number(self):

        self.clicks(self.less_number_loc, 0)
        time.sleep(1)

    def clink_payway(self):
        '''点击支付方式'''

        self.click(self.clink_payway_loc)
        time.sleep(1)

    def choose_pays(self):

        self.random_randint_datail(self.choose_pays_loc)
        time.sleep(1)

    def clink_insurance(self):

        '''点击保价'''

        self.clicks(self.clink_insurance_loc, 3)

    def input_insur(self):

        text = random.randint(1, 500000)
        self.send_keys(self.input_insurance_loc, text)
        time.sleep(1)

    def clink_remarks(self):
        '''点击留言'''
        self.click(self.clink_remarks_loc)
        time.sleep(1)

    def choose_remarks(self):
        self.random_randint_datail(self.choose_remarks_loc)
        time.sleep(1)

    def input_remarks(self):
        text = random.randint(100, 500)
        self.send_keys(self.input_remarks_loc, "要来一个吴彦祖呀%s" % text)
        time.sleep(2)

    # def clink_express(self):
    #     ''' 点击顺丰服务'''
    #
    #     self.clicks(self.clink_express_loc, 5)
    #     time.sleep(2)
    #
    # def close_express(self):
    #     # 关闭顺丰类型
    #     self.click(self.close_express_loc)
    #     time.sleep(2)

    def choose_express(self):

        elements = self.find_elements(self.choose_express_loc)
        suji = random.randint(1, len(elements) - 1)
        print("产品类型随机数-----", suji)
        self.js_focus_elements(self.choose_express_loc, suji)
        self.clicks(self.choose_express_loc, suji)
        time.sleep(2)


    def express_amount(self):
        '''获得快递金额'''

        text = self.finds_text_css(".cell-extra",5)
        return text

    def get_time(self):
        '''获得一小时内的时间'''

        text=self.find_text_css(".cell-extra:nth-child(1)")
        t = re.search("(.+)", text).group(0)
        return t.replace('~','-').replace(' ','')

    def get_time_long(self):
        '''获得预约时间'''

        text=self.find_text_css(".cell-extra:nth-child(1)")
        t = re.search("天(.+)", text).group(1)
        return t.replace('~','-').replace(' ','')

    def get_type(self):
        '''获得物品类型'''

        text = self.finds_text_css(".cell-extra",1)
        # text = self.find_text_css(".cell-extra:nth-child(2)")
        print("完善1",text.replace(' ',''))
        return text.replace(' ','')

    def get_payway(self):
        '''获得支付方式'''

        text=self.finds_text_css(".cell-extra",2)
        return text

    def get_insurance(self):
        '''获得保价'''

        text=self.finds_text_css(".cell-extra",3)
        return text



    def get_remarks(self):
        '''获得留言'''

        text=self.finds_text_css(".cell-extra",4)
        return text.replace(' ','')

    def money(self):
        '''获取支付金额'''
        # express = self.express_amount()
        # insurance = self.get_insurance()
        #

        #
        #

    def agree_item(self):

        self.click(self.agree_item_loc)

    def get_amount(self):
        '''获得总金额'''

        self.find_text_css(".price-wrap")
        text = self.find_text_css(".price-wrap")
        print("总金额：", text)

    def order_now(self):
        '''立即下单'''
        time.sleep(1)
        self.js_focus_element(self.order_now_loc)

        self.click(self.order_now_loc)
        time.sleep(1)

        text = self.is_element_exist(".sf-message")
        print("1-是否为高峰管控订单", text)

        text_agree = self.is_element_exist(".sf-popup")
        print("是否不同意协议", text_agree)



        if text:
            self.comfirm_btn()

        elif text_agree:


            '''同意条款'''
            self.agree_item()
            time.sleep(2)
            self.click(self.order_now_loc)
            time.sleep(2)
            text_h = self.is_element_exist(".sf-message")
            print("2-是否为高峰管控订单", text)
            if text_h:
                self.comfirm_btn()



        time.sleep(5)



    '''预约成功页面'''

    def more(self):
        '''查看/收起更多详情'''
        self.click(self.more_loc)

    def date_time(self):

        '''获得预约上门时间2'''

        # self.find_text_css(".time")

        text = self.find_text_css(".time")
        t=re.search("天(.+)", text).group(1)
        return t.replace('~','-').replace(' ','')

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
        print("物品类型2",text.replace(' ',''))
        return text.replace(' ','')

    def insure_text(self):

        '''获得保价2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(4)>span:nth-child(2)")
        return text

    def pay(self):

        '''获得支付方式2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(5)>span:nth-child(2)")
        return text

    def remarks(self):

        '''获得留言2'''

        text = self.find_text_css(".sf-collapse-item-content>ul>li:nth-child(6)>span:nth-child(2)")
        return text.replace(' ','')

    def cancel_order(self):
        '''取消订单'''
        self.click(self.cancel_order_loc)

    def cancel_reason(self):

        self.random_randint_datail(self.cancels_reason_loc)
        time.sleep(1)
    def cancel_sub(self):

        self.click(self.cancel_sub_loc)
        time.sleep(2)

    def cancel_btn(self):

        self.click(self.cancel_btn_loc)

    def comfirm_btn(self):

        self.click(self.comfirm_btn_loc)
        time.sleep(1)

    def package(self):

        self.click(self.package_loc)


    '''完善包裹信息页面'''

    def clink_type2(self):
        '''点击物品类型2'''
        self.clicks(self.clink_type_loc, 0)
        time.sleep(2)

    def clink_payway2(self):
        '''点击支付方式2'''
        self.click(self.clink_payway_loc)
        time.sleep(2)

    def clink_insurance2(self):
        '''点击保价2'''
        self.clicks(self.clink_insurance_loc, 2)
        time.sleep(2)

    def clink_remarks2(self):
        '''点击留言2'''
        self.click(self.clink_remarks_loc)
        time.sleep(2)

    def package_conf(self):
        '''点击确定2'''
        self.click(self.package_conf_loc)
        time.sleep(2)

    def get_type2(self):

        '''获得物品类型2'''

        text = self.finds_text_css(".cell-extra",0)
        print("完善1", text.replace(' ', ''))
        return text.replace(' ', '')

    def get_payway2(self):

        '''获得支付方式2'''

        text = self.finds_text_css(".cell-extra",1)
        return text

    def get_insurance2(self):

        '''获得保价2'''

        text = self.finds_text_css(".cell-extra",2)
        return text

    def get_remarks2(self):

        '''获得留言2'''

        text = self.finds_text_css(".cell-extra",3)
        return text.replace(' ', '')



    '''操作方法'''

    def LoginCase(self, ):

        self.get_activity()
        self.next()
        self.more1()
        # 获取当前app的contexts
        contexts = self.driver.contexts
        print("切换前", contexts)
        # 切换到webview
        self.switch_webview()
        new = self.driver.current_context
        print("获取当前环境", new)
        p = self.driver.page_source
        print(p)
        with open(r'F:\testScript\appium-master\CCWP_New\ccwp_page_source\source1.html', 'wb') as f:
            f.write(p.encode('utf-8'))
        time.sleep(2)



    '''操作方法'''


    def LoginCase1(self, ):

        self.get_activity()

        # 获取当前app的contexts
        contexts = self.driver.contexts
        print(contexts)
        # 切换到webview
        self.switch_webview()
        time.sleep(2)

    def time_long(self):
        '''点击预约取件时间(预约单)'''
        self.clink_time()

        self.choose_DD1()

        self.choose_DD2()

        self.choose_DD3()

        # self.choose_HHs()
        time.sleep(1)

        self.all_conf()

        text = self.is_element_exist(".van-toast.van-toast--text.van-toast--middle")
        print("是否不在预约时间内", text)
        if text:
            self.choose_DD2()

            self.all_conf()

    def time(self):
        '''点击预约取件时间(实时单)'''
        self.clink_time()

        self.all_conf()

        text=self.is_element_exist(".van-toast.van-toast--text.van-toast--middle")
        print("是否不在实时单的预约时间内",text)
        if text:
            self.choose_DD2()

            self.all_conf()


    def type(self):
        '''点击物品类型'''

        self.clink_type()
        time.sleep(6)

        self.choose_type()

        self.choose_type()

        self.input_name1()


        self.input_weight()

        self.all_conf()
        time.sleep(8)

    def payway(self):

        self.clink_payway()

        self.choose_pays()

    def insur(self):

        self.clink_insurance()

        self.input_insur()

        self.all_conf()


    def all_remarks(self):

        self.clink_remarks()
        time.sleep(3)

        self.choose_remarks()

        self.choose_remarks()

        self.input_remarks()

        self.all_conf()
        time.sleep(5)

        self.more_detail_()



    def express(self):

        ''' 点击顺丰服务'''

        # self.clink_express()
        # time.sleep(5)

        self.choose_express()


        text = self.is_element_exist(".van-toast.van-toast--text.van-toast--middle")
        print("是否不在服务有效期内", text)
        if text:
            # self.close_express()

            self.clink_time()

            self.choose_DD2()

            time.sleep(1)

            self.all_conf()

            # self.clink_express()
            # time.sleep(5)
            #
            # self.choose_express()

        time.sleep(5)

    def order(self):

        '''同意条款'''

        # self.agree_item()
        '''立即下单'''

        self.order_now()

        activity = self.is_displayed(self.activity_loc)
        print("活动是否存在：",activity)
        if activity:
            self.click(self.activity_no_loc)

        self.more_detail_()
        time.sleep(2)





    def cancel_yes(self):
        '''取消订单-是'''
        self.cancel_order()

        self.cancel_reason()

        self.cancel_sub()

        self.comfirm_btn()

        time.sleep(1)
        self.back()

    def cancel_no(self):
        '''取消订单-否'''
        self.cancel_order()

        self.cancel_reason()

        self.cancel_sub()

        self.cancel_btn()

        self.back()
        time.sleep(1)

    def type2(self):
        '''点击物品类型'''

        self.clink_type2()

        self.choose_type()

        self.choose_type()

        self.input_name1()

        self.input_weight()

        self.all_conf()

    def payway2(self):

        '''点击支付方式'''
        self.clink_payway2()

        self.choose_pays()

    def insur2(self):

        self.clink_insurance2()

        self.input_insur()

        self.all_conf()
        time.sleep(1)

    def all_remarks2(self):

        self.clink_remarks2()

        self.choose_remarks()

        self.choose_remarks()

        self.input_remarks()

        self.all_conf()



    def packages(self):

        self.package()

        time.sleep(1)

        self.type2()

        self.payway2()

        self.insur2()

        self.all_remarks2()

        time.sleep(1)

    def back_more(self):

        self.package_conf()

        self.more_detail_()

        # time.sleep(2)

        # self.js_focus_element(self.more_detail_loc)
        #
        # self.more_detail_()













































