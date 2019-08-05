# encoding: utf-8

class Desired(object):


    def desired_caps(self):
        pack='com.inspur.icity.icityapp'
        activict='com.inspur.icity.icityapp.modules.startup.view.SplashActivity'
        desired_caps={
            'platformName':'Android',
            'deviceName':'127.0.0.1:21503',
            'platformVersion':'5.1.1',
            #apk包名
            'appPackage':pack,
            # 'appPackage': 'com.UCMobile',
            'appActivity':activict,
            # 'appActivity': 'com.UCMobile.main.UCMobile',
            'unicodeKeyboard':True,
            'reserKeyboard':True,
            'automation':'Uiautomator2',
            'noReset':True
        }
        return desired_caps
