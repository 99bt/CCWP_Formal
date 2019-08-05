# encoding: utf-8

import os,time
import logging


ATP_PATH = os.path.dirname(os.path.abspath(__file__))
log_path=os.path.join(ATP_PATH,"ccwp_log")
print(log_path)

class Log():
    def __init__(self):
        #文件的命名
        self.logname=os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d_%H_%M_%S'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #日志输出格式
        self.formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s")

    def _console(self,level,message,exc_info=True):
        #创建一个handler,用于写入日志
        fh=logging.FileHandler(self.logname,'a+',encoding='utf-8')#a是追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        #创建一个SteamHandler,用于输出到控制台

        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level=='info':
            self.logger.info(message,exc_info=True)

        elif level=='debug':
            self.logger.debug(message,exc_info=True)

        elif level=='warning':
            self.logger.warning(message,exc_info=True)

        elif level=='error':
            self.logger.error(message,exc_info=True)

        elif level=='critical':
            self.logger.critical(message,exc_info=True)

        #避免日志输出重复的问题

        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        #关闭打开的文件

        fh.close()

    def debug(self,message):
        self._console('debug',message)

    def info(self,message):
        self._console('info',message)

    def warning(self,message):
        self._console('warning',message)

    def error(self,message):
        self._console('error',message)

    def critical(self,message):
        self._console('critical',message)

if __name__=="__main__":
    log=Log()
    log.info("----测试开始----")
    log.error("---输入密码---")
    log.critical("---测试结束---------")




