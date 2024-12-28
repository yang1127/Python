# 异常：程序运行过程中，代码遇到错误，给出错误提示
# 捕获异常：在程序代码运行过程中，遇到错误，不让程序代码终止，让其继续运行
#         同时可以给使用者一个提示信息，并记录该错误，便于后期改进

"""
捕获单个异常：

try：
    可能发生异常的代码
except 异常类型：
    发生异常执行的代码


num = input("请输入一个数字：")
try:
    num = 10 / int(num)
    print('计算结果是：', num)
except ZeroDivisionError:  # ZeroDivisionError - 异常类型
    print("输入有误，再次输入")

print("其他代码～")
"""

"""
捕获多个异常：
方法一：
try：
    可能发生异常的代码
except (异常的类型1, 异常的类型2, ....)：
    发生异常执行的代码

num = input("请输入一个数字：")
try:
    num = 10 / int(num)
    print('计算结果是：', num)
except (ZeroDivisionError, ValueError):  # ZeroDivisionError - 异常类型
    print("输入有误，再次输入")

print("其他代码～")
"""

"""
方法二：
try：
    可能发生异常的代码
except 异常类型1：
    发生异常1, 执行的代码
except 异常类型2：
    发生异常2, 执行的代码


num = input("请输入一个数字：")
try:
    num = 10 / int(num)
    print('计算结果是：', num)
except ZeroDivisionError:  # ZeroDivisionError - 异常类型
    print("输入有误，再次输入")
except ValueError:
    print("输入有误，再次输入")

print("其他代码～")
"""

"""
打印异常信息

try：
    可能发生异常的代码
except（异常类型1, 异常类型2, ...） as 变量名:
    发生异常执行的代码
    print(变量名)


num = input("请输入一个数字：")
try:
    num = 10 / int(num)
    print('计算结果是：', num)
except (ZeroDivisionError, ValueError) as e:
    print("输入有误，再次输入", e)

print("其他代码～")
"""

"""
捕获所有的异常：
try:
    可能发生异常的代码
except: 
    发生异常执行的代码
    
缺点：不能获取异常的描述信息
---------------------------------
try:
    可能发生异常的代码
except Exception as e:
    发生异常执行的代码
    print(e)
    pass
    
Exception:常见异常类的父类

num = input("请输入一个数字：")
try:
    num = 10 / int(num)
    print('计算结果是：', num)
except Exception as e:
    print("输入有误，再次输入", e)

print("其他代码～")
"""

"""
print("其他代码～")

num = input("请输入一个数字：")
try:
    num = 10 / int(num)
    print('计算结果是：', num)
    f = open("1.txt", "r")
except Exception as e:
    print("输入有误，再次输入", e)
else:
    print("没有异常，我会执行")
finally:
    print("不管有没有异常，我都会执行")

print("其他代码～")
"""


# 抛出自定义异常
# eg：定义自定义类，密码长度不足的异常
class PasswordLengthError(Exception):
    pass


def get_password():
    password = input("请输入密码：")
    if len(password) >= 8:
        print("密码合格")
    else:
        # 抛出异常
        raise PasswordLengthError('密码不足8位')


try:
    get_password()
except PasswordLengthError as e:
    print(e)

get_password()  # 调用系统函数



