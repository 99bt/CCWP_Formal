import os
import time


ATP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path=os.path.join(ATP_PATH,"ccwp_log")
nowTime = time.strftime("%Y%m%d.%H.%M.%S")
screenshot=os.path.join(ATP_PATH,"ccwp_screenshot\%s.jpg"%nowTime)
print(os.path.abspath(os.path.dirname(__file__)))