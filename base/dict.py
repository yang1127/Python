'''
# 字典dict使用 {} 定义，由键值对<key, value>组成
# 变量 = {key1:value1, key2:value2, ... } 一个key:value键值对是一个元素
# 字典的key可以为 字符串 和 数字类型（int, float） 不能为列表
# value值可以为任何类型

# 定义空字典
my_dict = {}
print(my_dict, type(my_dict)) # {} <class 'dict'>

# 定义带数据的字典
my_dict1 = {'name': 'yzq', 'age': 18, 'like': ['学习', '购物', '游戏'], 1: {2, 5, 8}}
print(my_dict1)

# 访问value值，字典中，没有下标的概念，使用key值去访问value值
print(my_dict1['name']) # yzq
print(my_dict1['like'][1]) # 购物，访问like，value为元组，可以使用下标再去访问

# key值不存在
# print(my_dict1['xiaoyang']) # 报错
print(my_dict1.get('xiaoyang')) # None
'''

'''
# my_dict.get(key, value) 如果key存在，返回value值，不存在返回None
my_dict = {'name': 'yzq', 'age': 18, 'like': ['学习', '购物', '游戏'], 1: {2, 5, 8}}
print(my_dict.get('name')) # yzq
print(my_dict.get('xiaoyang', 'hahah~')) # hahah~  key不存在，返回相应值
print(my_dict.get('age', 'hahah~')) # 18 key存在，返回key对应的值
'''

'''
# 求长度 - 键值对的多少
print(len(my_dict)) # 4
'''

'''
# 字典中的添加和修改数据，使用key值进行添加和修改
# 字典[key] = 数据，如果key存在，就修改，不存在，就添加
# 注意key值中 int的1 与 float的1.0 是一个值
my_dict = {'name': 'yzq'}
my_dict['name'] = 'xiaoyang'
my_dict['age'] = 18
print(my_dict) # {'name': 'xiaoyang', 'age': 18}
'''

'''
# 删除数据
# del 字典名[key]
my_dict = {'name': 'xiaoyang', 'age': 18}
del my_dict['name']
print(my_dict) # print(my_dict)

# 字典.pop(key)
my_dict1 = {'name': 'xiaoyang', 'age': 18}
print(my_dict1.pop('age')) # 18
print(my_dict1) # {'name': 'xiaoyang'}

# 字典.clear() 清空字典
my_dict2 = {'name': 'xiaoyang', 'age': 18}
my_dict2.clear()
print(my_dict2) # {}

# del 字典 - 直接删除这个字典，不能再使用这个字典
my_dict3 = {'name': 'xiaoyang', 'age': 18}
del my_dict3
'''

'''
# 遍历
# for循环
my_dict = {'name': 'xiaoyang', 'age': 18}
# 遍历key值
for key in my_dict:
    print(key) # name, age

# 遍历键值对，通过key去访问value
for key in my_dict:
    print(key, my_dict[key]) # name xiaoyang, age 18
'''

'''
# 字典.keys() 获取所有key值，得到的类型为 dict_keys
# <class 'dict'>该类型具有以下特点：
# 1、可以使用list() 进行类型转换，转为列表类型
# 2、可以使用for循环进行遍历
my_dict = {'name': 'xiaoyang', 'age': 18}
my_dict1 = my_dict.keys()
print(my_dict1, type(my_dict1)) # {'name': 'xiaoyang', 'age': 18} <class 'dict_keys'>

for key in my_dict.keys():
    print(key) # name, age

# 字典.values() 获取所有的value，特点同 字典.keys()
for value in my_dict.values():
    print(value) # xiaoyang, 18
'''

'''
# 字典.items() 获取所有的键值对，特点同 字典.keys()
my_dict = {'name': 'xiaoyang', 'age': 18}
my_dict1 = my_dict.items()
print(my_dict1, type(my_dict1)) #dict_items([('name', 'xiaoyang'), ('age', 18)]) <class 'dict_items'>

# 拆包
for item in my_dict.items():
    print(item[0], item[1]) # name xiaoyang, age 18

for k, v in my_dict.items():
    print(k, v) # name xiaoyang, age 18
'''

'''
# enum
# erate() 将可迭代序列中的元素所在的下标和具体元素结合在一期，变成元组
my_list = ['a', 'b', 'c', 'd']
for i in my_list:
    print(my_list.index(i), i)
# 0 a
# 1 b
# 2 c
# 3 d

for i in enumerate(my_list):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
'''

'''
>>>>>>> test-python
# 字典中比较的是key的大小，min()、max()
my_dict = {'a': 30, 'b': 20, 'c': 10}
my_max = max(my_dict)
print(my_max) # c

my_min = min(my_dict)
print(my_min) # a
<<<<<<< HEAD

=======
'''

# 字典推导式
# 变量 = {生成字典的规则(key: value) for 临时变量 in xxx}
my_dict1 = {f'name{i}': i for i in range(5)}
print(my_dict1)
# {'name0': 0, 'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4}

my_dict2 = {f'name{i}': i for i in range(2) for j in range(2)}
print(my_dict2)
# 字典中key相同，修改数据
# {'name0': 0, 'name1': 1}}

my_dict3 = {f'name{i}{j}': i for i in range(2) for j in range(2)}
print(my_dict3)
# {'name00': 0, 'name01': 0, 'name10': 1, 'name11': 1}



