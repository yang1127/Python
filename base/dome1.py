# \n转义
# print(r"hello world\n hello xiaoyang")

# enter退出
# input("\n\n按下 enter 键后退出。")

# 一行显示多条语句
#import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# def reverseWords(input):
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
#
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords = inputWords[-1::-1]
#
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#
#     return output
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     print(rw)

# 排序
# set = {'yzq', 'zdz', 'yzq', 'hahah~'}
# print(set)

# 原来顺序-list、set、sort()

# a = ['yzq', 'zdz', 'yzq', 'hahah~']
# b = list(set(a))
# b.sort(key = a.index)
# print(b)

# 变量的定义
# name = '杨芝琪'
# print(name)
#
# name = 'yzq'
# print(name)

# type()函数得到类型
# int类型
# result = 10
# print(type(result))

# bool类型 True、False需要大写
# result = True
# print(type(result))


# 输入输出
'''
name = 'yzq'
age = 10
height = 3.1415926
print('我的身高是%fcm' % height) # command + D 快速复制一行

# %.nf 保留n位小数
print('我的身高是%.2fcm' % height)
print('我的名字是%s，年龄是%d，身高是%.2fcm'% (name, age, height))

# 格式化输出%，需要两个%%
print('及格人数占比%d%%' % 50)

# 3.6版本支持使用f-string，占位同一使用{}占位，填充数据写在{}中
print(f'我的名字是{name},年龄是{age}岁，身高是{height}cm')
'''

'''
# input()+类型转换
price = input('请输入价格：')
weight = input('请输入重量：')
result = float(price) * float(weight) # 将str类型进行float类型转换
print(f'价格是{price}元/斤，重量{weight}斤，重价格{result}元')

# 类型转换 - 不会改变原始数据，生成一个新的数据
# 转换为int类型
# float -> int
pi = 3.1415926
num = int(pi)
print(type(num))
# str -> int
str = '10'
num = int(str)
print(type(num))

# 转换为float类型
# int -> float
a = 10
b = float(a)
print(type(b))
# 数字类型转换为float
a1 = float("3.14")
print(type(a1))

# eval() 还原原来的数据类型，去掉字符串的引号
num = eval('100')
print(type(num)) # int
'''

# 算术运算
# 特殊几个类型：// 整除、** 指数
# 优先级：**  > * > / > % > // > (+/-)

# 条件判断语句
'''
# if
age = input('输入年龄：')
if int(age) > 18: # input输入的是str类型，需要与18比较的时候，转换为int类型
    print('Nice!!!')

# if、else
age = input('输入年龄：')
if int(age) > 18:
    print('Nice!!!')
else:
    print('Ai~~')

# if、elif、else
# age = input('输入年龄：')
# if (int(age) >= 18) and (int(age) <= 60):
#     print('Nice!!!')
# elif int(age) > 60:
#     print('Good!!!')
# else:
#     print('Ai~~')

age = eval(input('输入年龄：'))
if (age >= 18) and (age <= 60):
    print('Nice!!!')
elif age > 60:
    print('Good!!!')
else:
    print('Ai~~')
'''

# debug调试
# 1、打断点
# 2、右键debug运行代码
# 3、点击下一步，查看代码运行

'''
# 三目运算
a = eval(input('请输入一个数字：'))
b = eval(input('请输入一个数字：'))
# if（a>b） 成立，则执行if条件前的结果，若不成立，执行if条件后面的结果
result = (a - b) if a > b else (b - a) 
print(result)
'''

'''
# 循环语句
# while
a = int(input('请输入一个数字：'))
count = 0 # 记录次数与输入的数字做比较
while count < a:
    print('hahah~~')
    count += 1

# 无限循环
while Ture:
    代码段

# 1-100的累加和
a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1
print(sum)

# 1-100的偶数累加和
a = 0
sum = 0
while a <= 100:
    sum += a
    a += 2
print(sum)

# 1-100的偶数累加和-变形
a = 1
sum = 0
while a <= 100:
    a += 1
    if a % 2 == 0: # 能被2整除，余数为0
        sum += a
print(sum)

# 循环嵌套-外层执行一次，内层执行多次
i = 0
num = 0
while i <= 5:
    j = 0 # 内层的判断次数需要写在内层
    while j <= 5:
        num += 1
        j += 1
    i += 1
print(num)
'''
'''
# for
# for循环格式 - 遍历
# for 临时变量 in 列表或者字符串等可迭代对象:
#     循环满足条件时执行的代码

name = 'hello world'
for i in name: # 一次循环打印字符串的一个字母

# range(n) 会生成[0, n)的数据序列，不包含n
for i in range(5):
    print(i) # 0,1,2,3,4    print(i)

# range(a, b) 会生成[a, b)的数据序列，不包含b
for i in range(1, 6):
    print(i) # 1,2,3,4,5

# range(a, b, step) 会生成[a,b)的数据序列，不包含b，每次跨度为step
for i in range(1, 6, 2):
    print(i) # 1,3,5
    
# 外层循环5次，内层每循环3次
for i in range(5):
    print('hahah~~')
    for j in range(3):
        print('xixix~~')

# 打印正方形
n = int(input('输入n:'))
for i in range(n):
    for j in range(n):
        print('*', end =' ') # end = ' ' 使输出的数据放置一行
    print()

# 打印直角三角形
n = int(input('输入n:'))
for i in range(n): # 外循环根据输入n循环次数、控制行数
    for j in range(i + 1): # 内循环根据外循环的第n次，内循环去循环n+1次，range()左闭右开，控制一行的循环次数
        print('*', end=' ')
    print()
'''
