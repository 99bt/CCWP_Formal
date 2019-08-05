# -*- coding: utf-8 -*-
from  dysms_python.aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkcore.client import AcsClient
import uuid,time
from aliyunsdkcore.profile import region_provider
from  dysms_python import const

# 短信业务调用接口示例，版本号：v20170525
# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(const.ACCESS_KEY_ID, const.ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)

def send_sms(phone_numbers, template_param=None,sign_name="顺丰大当家",template_code = "SMS_101325007"): #SMS_162736646
    # business_id = uuid.uuid1()

    # sign_name = "顺丰大当家"                           #短信签名名称,不可更改
    # template_code = "SMS_101325007"                   #短信模板ID,不可更改
    smsRequest = SendSmsRequest.SendSmsRequest()
    smsRequest.set_TemplateCode(template_code)     # 申请的短信模板编码,必填
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)     # 短信模板变量参数
    smsRequest.set_OutId(uuid.uuid1()) #    # 设置业务请求流水号，必填
    smsRequest.set_SignName(sign_name)     # 短信签名   # smsRequest.set_method(MT.POST)     # 数据提交方式 	# 数据提交格式   # smsRequest.set_accept_format(FT.JSON)
    smsRequest.set_PhoneNumbers(phone_numbers)     # 短信发送的号码列表，必填
    smsResponse = acs_client.do_action_with_exception(smsRequest)     # 调用短信发送接口，返回json
    return smsResponse     # TODO 业务处理

if __name__ == '__main__':

    phone_numbers = "13048911650"    # ("13048911650","122333xxxxx")
    templateparam = {"time":str(time.strftime ("%Y-%m-%d %H:%M:%S")),"business":"查询自己的会员信息","Other":"系统查看！！！"}
    #短信模板变量对应的实际值，JSON格式 # 系统时间   # business 描述业务   Other可以描述异常链接，快速查看   #  支持对多个手机号码发送短信，手机号码之间以英文逗号（,）分隔
    sms = send_sms(phone_numbers,str(templateparam))
    print(sms) #设置业务请求流水号  短信发送的号码列表   (短信签名  申请的短信模板编码   短信模板变量参数)不要动变量名称和变量除template_param 变量
    phone_numbers = ["13006626613", "18928405232"]
    for i in phone_numbers:
        templateparam = {"time": str(time.strftime("%Y-%m-%d %H:%M:%S")), "business": "【删除订单执行】", "Other": "系统异常情况！！！"}
        sms = send_sms(str(i), str(templateparam))
        print(sms)
   
    
    

