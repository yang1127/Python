'''
import time
t = time.time()
print(t)

# 获取当前时间
import datetime
t1 = datetime.datetime.now()
print(t1)

# 产生随机数
import random
a = random.randint(1, 100)
print(a)

import  os
print(os.getcwd()) # 获取当前工作目录，即当前python脚本工作的目录路径
'''

'''
# 方法一： import 模块名
# 使用：模块名.功能名
import mode

print(mode.num)  # 使用mode中的变量
mode.func()  # 调用mode重的func函数
dog = mode.Dog()  # 调用mode中类创建对象
dog.show()
'''

'''
# 方法二：from 模块名 import 功能名1，功能名2，...
# 使用：功能名
# 注意：如果存在同名的方法名，则会被覆盖

from mode import func, num
from mode1 import num

func()
print(num)
'''

'''
# 方法三：from 模块名 import *
# 将模块的所有导入

from mode import *

func()
print(num)
'''

'''
# as：起别名，可对模块、功能起别名
# 注意：如果使用as别名，就不能使用原来的名字

import mode as num1

num1.func()
'''

# __all__ 变量，类型为元祖、列表，会影响方法三：from 模块名 import *
# 定义__all__ 变量，只能导入变量中定义的内容
# 没有定义，模块所有的功能都能导入

'''
# 方法一：import 包名.模块名

import test.mode
test.mode.func()
'''

'''
# 方法二：from 包名.模块名 import 功能名
from test.mode import func

func()
'''


# 方法三：from 包名 import *
# 导入的是 __init__.py 中的内容
















































