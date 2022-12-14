# utils/logger.py

import os
import time
import logging
import json as _json
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 建立一个filehandler来把日志记录在文件里，级别为debug以上
fh = logging.FileHandler("{}/logs/{}.log".format(root_path, time.strftime('%Y%m%d', time.localtime())))
fh.setLevel(logging.DEBUG)
# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# 将相应的handler添加在logger对象中
logger.addHandler(ch)
logger.addHandler(fh)