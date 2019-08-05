# encoding: utf-8


# import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import * #导入所有异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
from selenium import webdriver
import random
import time

'''
基于原生的selenium框架做了二次封装

'''


# def browser():
#     driver = Firefox()
#     return driver

class Lee(object):

    def __init__(self,driver):
        """启动浏览器参数化，默认启动谷歌"""
        self.driver=driver
        # self.driver_=webdriver.Chrome()

    # def open(self,url,t='',timeout=10):
    #     '''
    #     使用get打开url后，最大化窗口，判断title符合预期
    #
    #     '''
    #
    #     self.browser.get(url)
    #     # self.driver.maximize_window()
    #     try:
    #         WebDriverWait(self.driver,timeout,1).until(EC.title_contains(t))
    #     except TimeoutError:
    #         print("open%s title error"%url)
    #     except Exception as msg:
    #         print("Error:%s"%msg)

    def find_element(self,locator,timeout=15):
        '''定位元素，参数locator是元祖类型'''
        element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator,timeout=15):
        '''定位一组元素'''
        elements=WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    # def find_elements(self, loc, timrout=10, ):
    #     elements = WebDriverWait(self.driver, timrout, 1).until(lambda x: x.find_elements(*loc))
    #     return elements

    def find_text_xpath(self,loc):
        '''获取元素文本xpath'''
        text=self.driver.find_element_by_xpath(loc).text
        return text

    def find_text_css(self,loc):
        '''获取元素文本css'''
        text=self.driver.find_element_by_css_selector(loc).text
        return text

    def finds_text_css(self,loc,n):
        '''获取元素文本'''
        text = self.driver.find_elements_by_css_selector(loc)[n].text
        return text


    '''自定义随机数'''

    def random_choose(self,loc,x,y):
        elements = self.find_elements(loc)
        # self.driver.execute_script("arguments[0].scrollIntoView();", target)
        sj=random.randint(x,y)
        elements[sj].click()



    '''根据元素个数中取随机数'''

    def random_randint(self,loc):
        elements = self.find_elements(loc)
        sj = random.randint(0, len(elements) - 1)
        return sj

    def random_randint_datail(self,loc):
        elements = self.find_elements(loc)
        member = self.random_randint(loc)
        elements[member].click()
        print("选择随机数",member)

    # def random_randint_datail(self, loc):
    #     elements = self.find_elements(loc)
    #     member = self.random_randint(loc)
    #     # self.driver.execute_script("arguments[%s].scrollIntoView();" % member, elements)
    #     elements[member].click()
    #     print("选择地址随机数",member)

    def click(self,locator):
        '''点击操作'''

        element=self.find_element(locator)
        element.click()

    # def click(self,locator):
    #     '''点击操作'''
    #
    #     target=self.find_element(locator)

    #     self.driver.execute_script("arguments[0].scrollIntoView();", target)
    #     target.click()

    def clicks(self,locator,n):
        elements=self.find_elements(locator)
        elements[n].click()

    # def clicks(self,locator,n):
    #     '''点击操作'''
    #
    #     elements = self.find_elements(locator)
    #     self.driver.execute_script("arguments[%s].scrollIntoView();"%n,elements)
    #     elements[n].click()

    def send_keys(self,locator,text):
        '''发送文本,清空后输入'''
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def sends_keys(self, locator, n,text):
        '''发送文本,清空后输入'''
        elements = self.find_elements(locator)
        elements[n].clear()
        elements[n].send_keys(text)

        # 判断元素是否存在
    def is_element_exist(self, css):
        s = self.driver.find_elements_by_css_selector(css)
        if len(s) == 0:
            # print("元素未找到:%s" % css)
            return False
        # elif len(s) == 1:
        #     return True
        else:
            # print("找到%s个元素:%s" % (len(s),css))
            return True

    def is_text_in_element(self,locator,text,timeout=10):
        '''判断文本在元素里，没定位到元素返回False,定位到返回判断结果布尔值'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
        except TimeoutException:
            # print("元素没定位到："+str(locator))
            return False
        else:
            return result

    def is_or_elements(self,locator,timeout=10):
        '''判断元素是否存在dom里，没定位到元素返回False,定位到返回结果布尔值'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            # print("元素没定位到："+str(locator))
            return False
        else:
            return True

    def is_text_in_element01(self,locator,value,timeout=10):
        '''判断元素的value值，没定位到元素就返回Flase,定位到返回判断结果布尔值'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))

        except TimeoutException:
            # print("元素没定位到:"+str(locator))
            return False
        else:
            return result
    def is_title(self,title,timeout=10):
        '''判断title完全等于'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
        return result

    def is_contains(self,title,timeout=10):
        '''判断title包含'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.title_contains(title))
        return result

    def is_selected(self,locator,timout=10):
        '''判断元素被选中一般用在下拉框，返回布尔值'''
        result=WebDriverWait(self.driver,timout,1).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self,locator,selected=True,timeout=10):
        '''判断元素的选中状态是否符合预期，selected是期望的参数True/False,返回布尔值'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
        return result

    def is_alert_present(self,timeout=10):
        '''判断页面是否有alert
        有返回alert（注意这里是返回alert,不是True
        没有返回Flase'''

        result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
        return result

    def is_visibility(self,locator,timeout=10):
        '''元素可见返回True，不可见返回Fasle'''
        try:
            the_element=WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))
            assert the_element(self.driver)
            flag = True
        except:
            flag = False
        return flag

    # def is_element_visible(self, element):
    #     driver = self.driver
    #     try:
    #         the_element = EC.visibility_of_element_located(element)
    #         assert the_element(driver)
    #         flag = True
    #     except:
    #         flag = False
    #     return flag
    def is_displayed(self,loc):
        '''判断元素是否显示'''
        dis=self.find_element(loc)
        return dis.is_displayed()

    # def is_selected:
    #     .is_selected()：判断元素是否选中状态


    def is_invisibility(self,locaotr,timeout=10):
        '''元素可见返回本身，不可见返回Fasle,没找到元素也返回Fasle'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(locaotr))
        return result

    def is_clickable(self,locator,timeout=10):
        '''元素可以点击is_enabled返回本身，不可点击返回FALSE'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self,locator,timeout=10):
        '''判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def refresh(self):
        '''刷新页面'''
        self.driver.refresh()

    def back(self):
        '''back to old window'''
        self.driver.back()
        time.sleep(3)

    def forward(self):
        '''forward to old window'''
        self.driver.forward()

    def close(self):
        '''close the window'''
        self.driver.close()

    def quit(self):
        '''quit the driver and close all the windows'''

        self.driver.quit()
    def get_title(self):
        '''获取title'''
        return self.driver.title


    def get_text(self,locator):
        '''获取文本'''
        element=self.find_element(locator)
        return element.text

    def get_attribute(self,locator,name):
        '''获取属性'''

        element=self.find_element(locator)
        return element.get_attribute(name)

    def get_attributes(self,locator,n,name):
        '''获取属性'''

        elements=self.find_elements(locator)
        text=elements[n].get_attribute(name)
        return text

    def js_execute(self,js):
        '''执行js'''
        return self.driver.execute_script(js)

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_focus_elements(self,locator,n):
        '''聚焦元素'''
        target=self.find_elements(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target[n])


    def js_focus_elements_suji(self,locator):
        '''聚焦元素'''
        n=self.random_randint(locator)
        target=self.find_elements(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target[n])
        self.clicks(locator, n)

    def js_clicks(self,loc,n):

        '''js点击操作'''
        target = self.find_elements(loc)
        self.driver.execute_script("arguments[0].click();", target[n])

        # js3 = 'document.querySelectorAll(%s)[0].click();'%css
        # js3 = 'document.querySelector(%s).click();'%css
        # self.driver.execute_script(js3)




    def js_send_keys(self,css,text):
        '''js输入操作'''
        # target = self.find_elements(loc)
        # self.driver.execute_script("arguments[0].value(text);", target)

        # js3 = 'document.getElementsByClassName("input-text")[1].value="xxx";'
        # driver.execute_script(js3)

        js4 = 'document.querySelectorAll("%s")[0].value="%s";'%css%text
        self.driver.execute_script(js4)

    def js_scroll_top(self):
        '''滚动到顶部'''
        if driver.name == "chrome":
            js="var q=document.body.scrollTop=0"
        else:
            js ="var q=document.documentElement.scrollTop=0"

        return self.js_execute(js)

    def js_scoll_end(self):
        '''滚动到底部'''

        if driver.name == "chrome":
            js = "var q=document.body.scrollTop=10000"
        else:
            js = "var q=document.documentElement.scrollTop=10000"

        return self.js_execute(js)

    def select_by_index(self,locator,index):
        '''通过索引，index是索引第几个，从0开始'''
        element=self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element=self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
       ''' 通过文本值定位'''
       element=self.find_element(locator)
       Select(element).deselect_by_visible_text(text)

    def get_window_handle(self,locator):
        h=self.driver.current_wondow_handle
        print(h)
        self.click(locator)
        all_h=driver.window_handles
        print(all_h)



    #appium模拟手指滑动

    # 通过get_window_size函数获取尺寸
    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return (x,y)

    # 上滑

    '''t 持续时间，n 滑动次数'''
    def swipe_up(self,t=500,n=1):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.5,screen[1]*0.75,screen[0]*0.5,screen[1]*0.25,t)

    # 下滑
    def swipe_down(self,t=500,n=1 ):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.5,screen[1]*0.25,screen[0]*0.5,screen[1]*0.75,t)

    # 左滑
    def swipe_left(self,t=500,n=1):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.75,screen[1]*0.5,screen[0]*0.25,screen[1]*0.5,t)

    # 右滑
    def swipe_right(self,t=500,n=1):
        screen=self.get_size()
        for i in range(n):
            self.driver.swipe(screen[0]*0.25,screen[1]*0.5,screen[0]*0.75,screen[1]*0.5,t)

    # 判断页面上是否存在toast
    def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
        '''is toast exist, return True or False
        :Agrs:
         - driver - 传driver
         - text   - 页面上看到的文本内容
         - timeout - 最大超时时间，默认30s
         - poll_frequency  - 间隔查询时间，默认0.5s查询一次
        :Usage:
         is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    # 切换到webview

    def switch_webview(self):
        contexts=self.driver.contexts
        if len(contexts)>1:
            self.driver.switch_to.context(contexts[1])


        else:
            self.driver.switch_to.context("NATIVE_APP")

    def switch_native(self):
        # contexts=self.driver.contexts
        self.driver.switch_to.context("NATIVE_APP")

    def get_activity(self):
        #app启动完成进入主页面
        ac=self.driver.current_activity
        print("当前页面的activity",ac)
        self.driver.wait_activity(ac,30)

    def android_find_element(self,loc,timeout=10):
        result=WebDriverWait(self.driver,timeout,1).until(lambda x : x.find_element_by_android_uiautomator(loc))
        return result

    def android_click(self,loc):
        element = self.android_find_element(loc)
        element.click()



if __name__=="__main__":
    driver=browser()
    driver_n=Lee(driver)#返回类的实例：打开浏览器
    driver_n.open("https://www.baidu.com/")
    input_loc=("id","kw")
    print(driver_n.get_title())
    el=driver_n.find_element(input_loc)
    driver_n.send_keys(input_loc,"yoyo")































