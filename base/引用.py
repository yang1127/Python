# 引用 - 内存地址的别名 - 类似C语言指针
# 通过id()来判断两个变量是否为同一个值的引用
# python中数据值的传递的是引用
# 赋值运算符可以改变变量的引用

'''
# eg：将数据10 存储到变量a 中，本质是将数据10 所在的内存的引用地址保存到变量a 中
a = 10
# 将变量a 中保存的引用地址给到b
b = a
print(a, b) # 10 10
print(id(a), id(b)) # 140663103560272 140663103560272

a = 20
print(id(a), id(b)) # 140295833525136 140295833524816
'''

'''
my_list = [1, 2, 3] # 将列表的引用地址保存到变量my_list中
my_list1 = my_list # 将my_list变量中的存储的引用地址给到my_list1
print(my_list, id(my_list))
print(my_list1, id(my_list1))
# [1, 2, 3] 140707147117952
# [1, 2, 3] 140707147117952

my_list.append(4) # 向列表中添加数据4，将数据4 的引用保存到列表中
print(my_list, id(my_list))
print(my_list1, id(my_list1))
# [1, 2, 3, 4] 140367576266112
# [1, 2, 3, 4] 140367576266112

my_list[0] = 5
print(my_list, id(my_list))
print(my_list1, id(my_list1))
# [5, 2, 3, 4] 140434716554624
# [5, 2, 3, 4] 140434716554624
'''

'''
# 类型的可变与不可变：在不改变变量引用的前提下，能否改变变量中的引用中的数据
# 能改变是可变类型，如果不能改变是不可变类型
# int float bool str list tuple dict
# 不可变类型：int float bool str tuple (元组的数据不能修改)
# 可变类型：list dict

a = 10
b = 10
# python中的内存优化，对于不可变类型进行
print(id(a), id(b))
# 140720993344080 140720993344080

print(id(a) == id(b))
# True

my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
print(id(my_list1), id(my_list2))
# 140569639974144 140569640284736

print(id(my_list1) == id(my_list2))
# False
'''

'''
# 元组不可修改，元组套列表、字典可修改
my_tuple1 = (1, 2, [3, 4])
print(my_tuple1) # (1, 2, [3, 4])

my_tuple1[2][1] = 66
print(my_tuple1) # (1, 2, [3, 66])

# 字典dict    key：value
my_tuple2 = (1, 2, {'age': 18, 'name': 'yzq'})
print(my_tuple2)

my_tuple2[2]['name'] = 'xiaoyang'
print(my_tuple2)
'''

# 函数传参传递的也是引用
my_list = [1, 2, 3] # 全局变量


def fun1(a):
    a.append(4)


def fun2():
    my_list.append(5)


def fun3():
    global my_list # global改变变量的值
    my_list = [1, 2, 3]


def fun4(a):
    # += 对于列表来说，类似列表的extend方法，不会改变变量的引用地址
    a += a


fun1(my_list) # [1, 2, 3, 4]
fun2() # [1, 2, 3, 4, 5]
fun3() # [1, 2, 3]
fun4(my_list) # [1, 2, 3, 1, 2, 3]
print(my_list)


b = 10 # 不可变类型
fun4(b)
print(b) # 10




















