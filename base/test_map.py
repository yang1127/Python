# map - 内置高阶函数 x^2
# 格式：map(function,iterable,...)
# 第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合

# 注意：map()函数不改变原有的list，而是返回一个新的list。

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 利用map()函数，可以把一个list转换为另一个list，只需要传入转换函数
# 由于list包含的元素可以是任何类型
# 所以map()它可以处理包含任意类型的list，只要传入的函数f可以处理这种数据类型

# 1、将有数字转为字符串，结果放入list中
res = list(map(str, [1, 2, 3, 4, 5]))
print(res)  # ['1', '2', '3', '4', '5']

# 2、字符串转换为数字
res1 = list(map(int, "12345"))
print(res1)  # [1, 2, 3, 4, 5]

# 3、将元组转换成list
res2 = list(map(int, (1, 2, 3, 4, 5)))
print(res2)  # [1, 2, 3, 4, 5]

res3 = map(int, (1, 2, 3, 4, 5))
print(list(res3))  # [1, 2, 3, 4, 5]

# 4、取字典中的key值，将结果放入list中
res4 = map(int, {1: "yzq", 2: "aqi"})
print(list(res4))  # [1, 2]
