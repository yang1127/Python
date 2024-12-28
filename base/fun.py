'''
# 函数的定义：使用关键字def
# def 函数名字():
#       函数代码(函数体)

# 函数的定义
def func():
    print('hahah~')


# 函数的调用
func()
'''

'''
# 文档说明
help(print)
'''

'''
# 带参数的函数
# a、b称为形式参数，简称形参
def add(a, b):
    # a = 10
    # b = 20
    c = a + b
    print(f"求和的结果{c}")


# 函数调用，如果函数在定义的时候有形参，在函数调用的时候，必须传递参数值
# 该参数值称为实际参数，简称实参，在函数调用的时候，将实参传递给形参
add(1, 2) # 3
add(100, 200) # 300
'''

'''
# 局部变量：作用域为当前函数的内部
# 局部变量的生存周期：在函数调用的时候被创建，函数结束的时候被销毁
# 函数变量只能在当前函数的内部使用，不能在函数的外部使用

# 全局变量：函数外部定义的变量
# 在函数内部可以访问全局变量的值，如果想要修改全局变量的值，需要使用 global 关键字声明
num = 100


def fun():
    global num
    num = 300
    print(num)


fun()
'''
'''
# 返回值
# 在函数中定义的局部变量，或者通过计算得到的局部变量，想要在函数外部访问和使用，此时就可以使用 return 关键字，将这个返回值返回

# 带返回值的函数


def fun(a, b):
    c = a + b
    return c


res = fun(100, 200)
print(f"{res}")
'''

'''
# 遇到return停止，如何多次返回？
def fun(a, b):
    c = a + b
    d = a - b
    return [c, d]
    # return c, d 默认组成元组进行返回的

    # return (c, d)、return ('c': c, 'd': d)、return (0: c, 1: d)


res = fun(10, 20)
print(f"a+b的结果是{res[0]},a-b的结果是{res[1]}")
'''

'''
# 函数嵌套
def fun2(a, b):
    d1 = a - b
    return d1


def fun1(a, b):
    c = a + b
    d = fun2(a, b)
    return c, d


res = fun1(10, 20)
print(f"a+b的结果是{res[0]},a-b的结果是{res[1]}")
'''

'''
# 函数传参
# 位置传参，按照形参的位置顺序将实参的值传递给形参
def fun(a, b, c):
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")


fun(1, 2, 3)
# a:1
# b:2
# c:3

# 关键字传参，指定实参给到哪个形参，关键字必须是函数的形参名
fun(a=10, b=20, c=30)
# a:10
# b:20
# c:30

# 混合使用,先写位置传参，再写关键字传参
fun(1, b=20, c=30)
# a:1
# b:20
# c:30
'''

'''
# 缺省传参 - 在函数定义的时候，给形参一个默认值，这个形参就是缺省参数
# 缺省参数要写在普通参数后边
# 特点：在函数调用的时候，如果给缺省参数传递实参值，使用的是传递的实参值，如果没有传递，使用默认值


def func(a, b, c=10):  # 形参c称为缺省形参
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"c:{c}")


func(1, 2) # 没有给c 传递实参，使用默认值10
func(1, 2, 3) # 给c 传递实参值，使用传递的数据3

def fun(a=10, b, c): # 报错，缺省参数要写在普通参数后边
'''

'''
# 不定长参数
# 在形参前面加一个*，该形参变为不定长元组形参，可以接收所有的位置实参，类型是元组
# 在形参前面加两个**，该形参变为不定长字典形参，可以接收所有关键字实参，类型是字典
def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4)
# (1, 2, 3, 4)
# {}

func(a=1, b=2, c=3)
# ()
# {'a': 1, 'b': 2, 'c': 3}

func(1, 2, 3, a=4, b=5, c=6)
# (1, 2, 3)
# {'a': 4, 'b': 5, 'c': 6}


# 求和
def fun(*args, **kwargs):
    num = 0
    for i in args:
        num += i

    for j in kwargs.values():
        num += j

    print(f"求和的结果为{num}")


fun(1, 2, 3, a=4, b=5, c=6) 
# 求和的结果为21
'''

'''
# 函数形参的完整格式
# 普通形参
def func(a, b):

# 缺省形参
def func1(a, b=1):

# 不定长元组形参
def func2(a, b=1, *args): # 语法上不会报错，但b=1，缺省参数不能使用默认值
def func3(a, *args, b=1): # 语法正确

# 不定长字典形参
def func4(a, *args, b=1, **kwargs): # 完整格式：普通、缺省、不定长元组、不定长字典
'''

'''
# sep
print(1, 2, 3)
print(1, 2, 3, sep='--')
print(1, 2, 3, sep=' ') # 默认
# 1 2 3
# 1--2--3
# 1 2 3
'''

'''
# 组包 - 将多个数据值，组成元组，给到一个变量
a = 1, 2, 3
print(a) # (1, 2, 3)

# 拆包 - 将容器的数据分别给到多个变量，需要注意：数据的个数和变量的个数要保持一致
a1 = 4, 5, 6
b, c, d = a1
print(b, c, d) # 4 5 6

e, f = [10, 20]
print(e, f) # 10 20

my_dict = {'name': 'yzq', 'age': 18 }
g, h = my_dict
print(my_dict) # {'name': 'yzq', 'age': 18}

# 交换两值
a = 10
b = 20
a, b = b, a
print(a, b) # 20 10
'''


















