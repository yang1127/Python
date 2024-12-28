# 斐波那契数
# # 1 1 2 3 5 8 13
# def fun(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fun(n - 1) + fun(n - 2)
#
#
# num = int(input('请输入相应数字：'))
# print(fun(num))

#
# # 阶乘
# def fun1(n):
#     if n == 1:
#         res = 1
#     else:
#         res = fun1(n - 1) * n
#
#     return res
#
#
# num = int(input('请输入相应数字：'))
# print(fun1(num))

'''
# 匿名函数 - lambda关键字定义
# lambda 参数列表：表达式
# 1、无参数无返回值
# 2、无参数有返回值
# 3、有参数无返回值
# 4、有参数有返回值

# 1、无参数无返回值
a = int(input('请输入a：')) # 10
b = int(input('请输入b：')) # 20
f1 = lambda: print(a + b)
f1() # 30

# 2、无参数有返回值
f2 = lambda: 1 + 2
print(f2()) # 3

# 3、有参数无返回值
f3 = lambda name: print(name)
f3('hello') # hello

# 4、有参数有返回值
f4 = lambda *args: args
print(f4(1, 2, 3, 4, 5)) # (1, 2, 3, 4, 5)
'''


'''
# 匿名函数作为函数的参数传递
def my_calc(a, b, func):
    """
    进行四则运算
    :param a: 第一个数据
    :param b: 第二个数据
    :param func: 函数，要进行的运算
    :return: 运算结果
    """
    num = func(a, b)
    print(num)


def add(a, b):
    return a + b


# 调用
my_calc(10, 20, add)

# 匿名函数
my_calc(10, 20, lambda a, b: a - b)
my_calc(10, 20, lambda a, b: a * b)
my_calc(10, 20, lambda a, b: a / b)
my_calc(10, 20, lambda a, b: a + b ** 2)
'''





