'''
# 列表 - 数据可以是任意类型
# 定义[]

# 空列表
my_list = []
print(my_list, type(my_list)) # [] <class 'list'>

my_list1 = list()
print(my_list1, type(my_list1)) # [] <class 'list'>

# 带数据列表，数据元素之间用逗号隔开
my_list2 = [1, 2.0, 3.1415926, True, 'yzq']
print(my_list2) # list[1, 2.0, 3.1415926, True, 'yzq']
'''
import random

'''
# 求列表中数据元素的个数，即列表长度
my_list = [1, 2.0, 3.1415926, True, 'yzq']
num = len(my_list) 
print(num) # 5
'''

'''
# 列表支持下标和切片 - 同string
my_list = [1, 2.0, 3.1415926, True, 'yzq']
print(my_list[0]) # 1
print(my_list[-1]) # yzq
print(my_list[1:4:2]) # [2.0, True]
print(my_list[-5:-1:3]) # [1, True]
print(my_list[4:1:-2]) # ['yzq', 3.1415926]
print(my_list[-1:-5:-2]) # ['yzq', 3.1415926]
'''

'''
# 与string不同 - string不能使用下标去修改其中的数据，而列表可以修改数据
my_list = [1, 2.0, 3.1415926, True, 'yzq']
my_list[0] = 'xiaoyang'
print(my_list) # ['xiaoyang', 2.0, 3.1415926, True, 'yzq']
'''

'''
# 列表的遍历
my_list = ['xiaoyang', 2, 3.1415926, True, 'yzq']
for i in my_list:
    print(i)

j = 0
while j < len(my_list):
    print(my_list[j])
    j += 1
'''

'''
# 列表中添加数据 - 都是在原列表中添加，不会返回新的列表
# list.append() 向列表尾部添加数据
my_list = ['yzq', 1, True]
my_list.append('xiaoyang')
print(my_list) # ['yzq', 1, True, 'xiaoyang']

# list.insert(下标， 数据)  在指定的位置添加
my_list1 = ['yzq', 1, True]
my_list1.insert(1, 'hahah~')
print(my_list1) # ['yzq', 'hahah~', 1, True]

# list.extend(可迭代对象)  列表，将可迭代对象中的数据逐个添加到原列表的末尾
my_list2 = ['yzq', 1, True]
my_list2.extend('hahah~')
print(my_list2) # ['yzq', 1, True, 'h', 'a', 'h', 'a', 'h', '~']

my_list2.extend(['yzq', 1, True])
print(my_list2) # ['yzq', 1, True, 'h', 'a', 'h', 'a', 'h', '~', 'yzq', 1, True]
'''

'''
# 列表中的数据查询操作
# index() 根据数据值，查找元素所在的下标，找到返回元素的下标，没有找到，程序报错
# 列表中没有find()方法，只有index()方法
my_list = [1, 2.0, 3.1415926, True, 'yzq']
num = my_list.index(3.1415926)
print(num) # 2
#num = my_list.index(1000) # 程序报错，数据不存在

# count() 统计出现的次数
my_list1 = ['yzq', 1, 2.0, 3.1415926, True, 'yzq']
num1 = my_list1.count('yzq') # 2
print(num1)

# in / not in 判断是否存在，存在返回True，不存在返回False
my_list2 = [1, 2.0, 3.1415926, True, 'yzq']
num2 = 'yzq' in my_list2
print(num2) # True

num3 = 1 not in my_list2
print(num3) # False
'''

'''
# 列表中的删除操作
# 1.1 根据元素的数据值删除
# remove()，直接删除原列表中的数据
my_list = [1, 2.0, 3.1415926, True, 'yzq']
my_list.remove(2.0)
print(my_list) # [1, 3.1415926, True, 'yzq']
# my_list.remove(2.0) # 不存在，报错

# 1.2 根据下标删除
# 1.2.1 pop(下标) 默认删除最后一个数据，返回删除内容
num = my_list.pop()
print(num) # yzq
print(my_list) # [1, 3.1415926, True]

num1 = my_list.pop(1)
print(num1) # 3.1415926
print(my_list) # [1, True]
# my_list.pop(1000) # 报错

# 1.2.2 del 列表[下标]
del my_list[1]
print(my_list) # [1]
# del my_list[10000] 不存在下标，报错
'''

'''
# 列表的排序
# 前提：列表的类型需要是一致的，否则，无法比较大小
# 列表.sort() 直接在原列表进行排序
my_list = [1, 9, 5, 8, 6]
my_list.sort()
print(my_list) # [1, 5, 6, 8, 9]

my_list.sort(reverse=True) # 逆序
print(my_list) # [9, 8, 6, 5, 1]

# sorted(列表) 会得到一个新的列表
my_list1 = [1, 9, 5, 8, 6]
my_list2 = sorted(my_list1)
print(my_list1) # [1, 9, 5, 8, 6]
print(my_list2) # [1, 5, 6, 8, 9]
'''

'''
# 逆置
my_list3 = ['a', 'd', 'e', 'c']
my_list4 = my_list3[::-1]
print(my_list3)
print(my_list4)

# reverse() 在原列表逆置
my_list3.reverse()
print(my_list3) # ['c', 'e', 'd', 'a']
'''

'''
# 列表的嵌套
school_names = [['北大', '清华'],
               ['南开', '天津大学', '天津示范大学'],
               ['山东大学', '中国海洋大学']]
print(school_names[1]) # ['南开', '天津大学', '天津示范大学']
print(school_names[1][1]) # 天津大学
print(school_names[1][1][1]) # 津

for school in school_names:
    print(school)
# ['北大','清华']
# ['南开', '天津大学', '天津示范大学']
# ['山东大学', '中国海洋大学']

for school in school_names:
    for name in school:
        print(name)

# 北大
# 清华
# 南开
# 天津大学
# 天津示范大学
# 山东大学
# 中国海洋大学

for school in school_names:
    for name in school:
        for s in name:
            print(s)
'''

'''
# 例题：八个老师，随机进入三个办公室
schoolrooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for teacher in teachers:
    num = random.randint(0, 2) # 产生随机数，相当于办公室的下标
    schoolrooms[num].append(teacher)

print(schoolrooms)
for office in schoolrooms:
    print(f'该办公室老师的个数为：{len(office)},办公室老师的名字为：')
    for teacher in office:
        print(teacher, end=' ')
    print()
'''

'''
# 列表排序中的key - 列表中镶嵌字典
list1 = [{'name': 'd', 'age': 19},
        {'name': 'b', 'age': 16},
        {'name': 'a', 'age': 16},
        {'name': 'c', 'age': 22}]

# sort(self, key, reverse) - 按照key类型排序
# key为name类型进行排序
# 匿名函数的形参是列表中的每一个数据 - 列表放的是每一个字典，x类型为字典
list1.sort(key=lambda x: x['name'])
print(list1)
# [{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'c', 'age': 22}, {'name': 'd', 'age': 19}]

# key为age类型进行排序
list1.sort(key=lambda x: x['age'])
print(list1)
# [{'name': 'a', 'age': 16}, {'name': 'b', 'age': 16}, {'name': 'd', 'age': 19}, {'name': 'c', 'age': 22}]
'''

'''
list2 = ['a', 'bc', 'def', 'abide']
list2.sort()
print(list2) # ['a', 'abide', 'bc', 'def']

# 根据字符串的长度进行排序
# list2.sort(key=len)
list2.sort(key=lambda x: len(x))
print(list2) # ['a', 'bc', 'def', 'abide']
'''

<<<<<<< HEAD



=======
'''
# 列表排序中的key - 列表中镶嵌字典
list1 = [{'name': 'd', 'age': 19},
        {'name': 'c', 'age': 16},
        {'name': 'a', 'age': 16},
        {'name': 'b', 'age': 19}]

# sort(key = lambda 形参：(排序规则1，排序规则2，... ))
# 当第一个规则形同时，会按照第二个规则排序
# 先年龄排序，再名字排序
list1.sort(key=lambda x: (x['age'], x['name']))
print(list1)
'''

'''
# 列表推导式，为了快速生成一个列表
# 1、变量 = [生成数据的规则 for 临时变量 in xxx]
# 每循环一次，就会创建一个数据
my_list1 = [i for i in range(5)]
print(my_list1)
# [0, 1, 2, 3, 4]

my_list2 = ['hello' for i in range(5)]
print(my_list2)
# ['hello', 'hello', 'hello', 'hello', 'hello']

my_list3 = [f'num{i}' for i in my_list1]
print(my_list3)
# ['num0', 'num1', 'num2', 'num3', 'num4']

my_list4 = [i+i for i in range(5)]
print(my_list4)
# [0, 2, 4, 6, 8]
'''

'''
# 2、变量 = [生成数据的规则 for 临时变量 in xxx if xxx]
# 每循环一次，并且if条件为True，生成一个数据

my_list1 = [i for i in range(5) if i % 2 == 0]
print(my_list1)
# [0, 2, 4]
'''

'''
# 3、变量 = [生成数据的规则 for 临时变量 in xxx for j in xxx]
# 第二个for，每循环一次，生成一个数据

my_list1 = [(i, j) for i in range(3) for j in range(2)]
print(my_list1)
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
'''
>>>>>>> test-python





