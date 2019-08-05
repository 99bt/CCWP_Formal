# -*- coding: utf-8 -*-

from selenium import webdriver
import sys, os

# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import unittest
from my_log import Log
import time
from ccwp_pages.Advance_Mail import AdvanceMail
from ccwp_pages.open_ import Desired
from lee_selenium import Lee
from ccwp_pages.Check_Mail import CheckMail
from ccwp_pages.Order import Order
from ccwp_pages.Address import Address
from dysms_python import sms_send
from ccwp_pages.Premail_inquiry import Premail

logger = Log()
phone_numbers = ["13006626613"]#"18938071147"

ATP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nowTime = time.strftime("%Y%m%d.%H.%M.%S")
screenshot=os.path.join(ATP_PATH,"ccwp_screenshot\%s.jpg"%nowTime)


class ccwp_test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        logger.info("-------------------启动浏览器-----------------")

        cls.driver = webdriver.Chrome()

        cls.driver_n = Lee(cls.driver)
        cls.Mail = AdvanceMail(cls.driver)
        cls.Check = CheckMail(cls.driver)
        cls.Order = Order(cls.driver)
        cls.Address=Address(cls.driver)
        cls.premail = Premail(cls.driver, cls.Address, cls.Mail)

        # cookies_url = "https://ccwp.sit.sf-express.com/service/alipay/dev/addSessionUserInfo?secrect=4ff55935385bd16e6daa76ddb1fa38fa&alipayUserid=2088332844928946&channel=1"
        cookies_url = "https://fuwu.sf-express.com/service/alipay/dev/addSessionUserInfo?secrect=4ff55935385bd16e6daa76ddb1fa38fa&alipayUserid=2088812320547835&channel=1"
        cls.driver.get(cookies_url)

        # login_url = 'https://ccwp.sit.sf-express.com/pageV5/#'
        login_url = "https://fuwu.sf-express.com/pageV5/#/"

        cls.driver.execute_script('window.open("%s");' % login_url)
        cls.driver.switch_to.window(cls.driver.window_handles[-1])
        cls.driver.set_window_size(500, 950)

    @classmethod
    def tearDownClass(cls):
        logger.info("--------------------关闭浏览器--------------------")
        cls.driver.quit()

    # @unittest.skip('暂时跳过用例的测试')
    def test01_Editaddress(self):

        try:

            logger.info("--------------寄前查询---------------------")
            self.premail.case_01()
            result = self.premail.query_results
            # result =self.driver_n.is_element_exist(".sf-send-before-query-res-content")

            self.assertTrue(result)

            self.premail.case_02()

            logger.info("--------------进入地址簿---------------------")
            logger.info("-------------增删改地址---------------------")

            self.Address.new_sender()

            receiver_name = self.Address.receiver_nameNO()
            receiver_detail = self.Address.receiver_detailNO()

            self.assertEqual(receiver_name, "杨测试单")
            self.assertEqual(receiver_detail, "广东省深圳市南山区南山街道辅导书及附件飞机都是是坚实的覅大V机会的ujvci不会的空间吧是")

        except Exception as e:
            logger.critical("----------增删改地址执行异常--------异常原因:%s" % e)


            t = self.driver.get_screenshot_as_file(screenshot)
            print("异常截图结果：", t)

            for i in phone_numbers:
                templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【增删改地址】","Other": "系统异常情况！！！"}
                sms_send.send_sms(str(i), str(templateparam))

    # @unittest.skip('暂时跳过用例的测试')
    def test02_sendOrder(self):
        try:
            '''收/寄件地址断言内容'''
            sender_nameNO = self.Address.sender_nameNO()
            sender_detailNO = self.Address.sender_detailNO()
            receiver_nameNO = self.Address.receiver_nameNO()
            receiver_detailNO = self.Address.receiver_detailNO()

            '''用例'''
            self.Mail.time_long()

            get_time = self.Mail.get_time_long()

            self.Mail.type()

            get_type = self.Mail.get_type()

            self.Mail.payway()

            get_payway = self.Mail.get_payway()

            self.Mail.insur()

            get_insurance = self.Mail.get_insurance()

            self.Mail.all_remarks()

            get_remarks = self.Mail.get_remarks()

            self.Mail.express()

            self.Mail.order()
            time.sleep(2)

            '''完善包裹断言内容'''
            logger.info("-------------预约单*下单成功页面-断言--------------------")
            date_time = self.Mail.date_time()
            sender_name2 = self.Mail.sender_name2()
            sender_detail2 = self.Mail.sender_detail2()
            receiver_name2 = self.Mail.receiver_name2()
            receiver_detail2 = self.Mail.receiver_detail2()

            order_no = self.Mail.order_no()
            goods = self.Mail.goods()
            insure_text = self.Mail.insure_text()
            pay = self.Mail.pay()
            remarks = self.Mail.remarks()

            self.assertEqual(date_time, get_time)
            self.assertEqual(sender_name2, sender_nameNO)
            self.assertEqual(sender_detail2, sender_detailNO)
            self.assertEqual(receiver_name2, receiver_nameNO)
            self.assertEqual(receiver_detail2, receiver_detailNO)
            self.assertIn(goods, get_type)
            self.assertEqual(goods, get_type)
            self.assertEqual(pay, get_payway)
            self.assertEqual(insure_text, get_insurance)
            # self.assertEqual(remarks, get_remarks)

        except Exception as e:
            logger.critical("----------预约单*下单执行异常--------异常原因:%s" % e)


            t = self.driver.get_screenshot_as_file(screenshot)
            print("异常截图结果：", t)

            for i in phone_numbers:
                templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【预约寄件执行】","Other": "系统异常情况！！！"}
                sms_send.send_sms(str(i), str(templateparam))

    # @unittest.skip('暂时跳过用例的测试')
    def test03_PerfectOrder(self):

        try:
            logger.info("-------------完善订单---------------------")
            self.Mail.packages()

            get_type2 = self.Mail.get_type2()
            get_payway2 = self.Mail.get_payway2()
            get_insurance2 = self.Mail.get_insurance2()
            get_remarks2 = self.Mail.get_remarks2()

            self.Mail.back_more()

            logger.info("-------------完善订单成功***页面跳转到预约成功页面***断言---------------------")
            goods_ = self.Mail.goods()
            insure_text_ = self.Mail.insure_text()
            pay_ = self.Mail.pay()
            remarks_ = self.Mail.remarks()

            self.assertEqual(goods_, get_type2)
            self.assertEqual(pay_, get_payway2)
            self.assertEqual(insure_text_, get_insurance2)
            self.assertEqual(remarks_, get_remarks2)

        except Exception as e:
            logger.critical("----------完善订单执行异常--------异常原因:%s" % e)

            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file(screenshot)
            # for i in phone_numbers:
            #     templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【完善订单信息执行】","Other": "系统异常情况！！！"}
            #     sms_send.send_sms(str(i), str(templateparam))

    # @unittest.skip('暂时跳过用例的测试')
    def test04_cencelOrder(self):
        try:
            logger.info("-------------取消订单---------------------")

            self.Mail.cancel_no()

            time.sleep(1)

            self.Mail.cancel_yes()

            logger.info("-------------订单取消成功-跳转到预约寄件页面---------------------")
            account = self.Mail.account
            self.assertTrue(account)

            time.sleep(2)

        except Exception as e:
            logger.critical("----------取消订单执行异常--------异常原因:%s" % e)

            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file(screenshot)

            for i in phone_numbers:
                templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【取消订单执行】","Other": "系统异常情况！！！"}
                sms_send.send_sms(str(i), str(templateparam))

    # @unittest.skip('暂时跳过用例的测试')
    def test05_delOrder(self):
        try:
            logger.info("-----------------我的列表***删除订单------------------")

            self.Order.Operation_order_1()

            list_orderNo = self.Order.get_orderNo()

            # self.assertEqual(order_no, list_orderNo)

            self.Order.Operation_order_2()

            # sender_name2 = self.Mail.sender_name2()
            # sender_detail2 = self.Mail.sender_detail2()
            # receiver_name2 = self.Mail.receiver_name2()
            # receiver_detail2 = self.Mail.receiver_detail2()

            # goods_ = self.Mail.goods()
            # insure_text_ = self.Mail.insure_text()
            # pay_ = self.Mail.pay()
            # remarks_ = self.Mail.remarks()

            datail_orderNo = self.Order.order_no()

            self.assertEqual(list_orderNo, datail_orderNo)

            self.Order.Operation_order_3()

            logger.info("-----------------我的列表***删除订单成功------------------")

        except Exception as e:
            logger.critical("------------删除订单执行异常--------异常原因:%s" % e)

            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file(screenshot)

            # for i in phone_numbers:
            #     templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【删除订单执行】","Other": "系统异常情况！！！"}
            #     sms_send.send_sms(str(i), str(templateparam))

    # @unittest.skip('暂时跳过用例的测试')
    def test06_checkPieces(self):
        try:

            logger.info("-----------------查件-----------------")
            self.Check.check_pieces()


            text=self.Check.is_element_exist(".van-toast.van-toast--text.van-toast--middle")
            print("查件", text)
            if text:
                print("运单号或联系电话不正确，或者当日查询次数过多")

            else:
                # self.assertEqual(self.Check.get_inputBno(),"231702993089")#803351784837
                # self.assertTrue(self.Check.get_bnoTime())
                self.Check.check_Records_pieces()


            # self.Check.check_Records_pieces()



            logger.info("-----------------查件成功----断言成功-------------")

        except Exception as e:
            logger.critical("------------查件执行异常--------异常原因:%s" % e)

            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file(screenshot)

            # for i in phone_numbers:
            #     templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【查件执行】","Other": "系统异常情况！！！"}
            #     sms_send.send_sms(str(i),str(templateparam))
            #
