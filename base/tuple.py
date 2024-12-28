# 与list类似，但不能修改元组的元素，故只能进行相应的查找
# 使用 - ()
my_tuple = (1, 'yzq', True, 3.1415926)
print(my_tuple) # (1, 'yzq', True, 3.1415926)

# 下标、切片
my_tuple1 = (1, 'yzq', True, 3.1415926)
print(my_tuple1[2]) # True
print(my_tuple1[1:3:1]) # ('yzq', True)

# 定义空元组
my_tuple2 = ()
my_tuple3 = tuple()
print(my_tuple2, type(my_tuple2)) # () <class 'tuple'>
print(my_tuple3, type(my_tuple3)) # () <class 'tuple'>

# 定义一个数据元素的元组
my_tuple4 = (3, ) # 需要加一个逗号，否则是int类型，单个传参
print(my_tuple4, type(my_tuple4, )) # (3,) <class 'tuple'>

