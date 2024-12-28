'''
# 集合 set 定义使用 {}, {数据， 数据}
# 1、集合中的数据必须是不可变类型
# 2、集合是可变类型
# 3、集合是无序的（数据的添加顺序和输出顺序是否一致）
# 4、集合中没有重复数据（去重）

my_set1 = {1, 3.14, True, 'hello', (1, 2)}
print(my_set1) # {3.14, 1, (1, 2), 'hello'}

my_set2 = {1, 3.14, 1, 'hello', 'hello'}
print(my_set2) # {1, 3.14, 'hello'}
'''

'''

my_set = {1, 2, 3, 4}

# 添加
my_set.add(5)
print(my_set) # {1, 2, 3, 4, 5}

# 删除
my_set.remove(1)
print(my_set) # {2, 3, 4, 5}

# 弹出、删除
my_set.pop()
print(my_set) # {3, 4, 5}

# 清除
my_set.clear()
print(my_set) # set()

# 修改 - 先删除、再添加
'''

# 集合、列表、元组 三者之间可以转换

