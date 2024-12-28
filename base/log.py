'''
import logging

logging.basicConfig(filename='log.txt', format='%(asctime)s %(message)s', filemode='w')

# 初始化log对象
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')
'''

'''
import logging.handlers

# 初始化log对象
logger = logging.getLogger(__name__)

# 标准输出 STDOUT
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename='log1.txt')

# 设置级别 NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
logger.setLevel(logging.DEBUG)  # 设置级别为DEBUG以上
handler1.setLevel(logging.WARNING)  # 设置级别为WARNING以上
handler2.setLevel(logging.DEBUG)  # 设置级别为DEBUG以上

# 定义log信息的顺序,结构和内容
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

# 将对应的handler添加到logger对象中
logger.addHandler(handler1)
logger.addHandler(handler2)

# 打印日志
logger.debug("This is debug message.")
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')
'''


import logging.handlers

# 初始化log对象
logger = logging.getLogger(__name__)

# 标准输出 STDOUT
handler1 = logging.StreamHandler()
handler2 = logging.handlers.RotatingFileHandler("log2.txt", mode='w', maxBytes=100, backupCount=3)
logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)

logger.debug("This is debug message.")
logger.info('This is info message')
logger.warning('This is warning message')
logger.error('This is error message')
logger.critical('This is critical message')