'''
# 单引号
name = 'yzq'
print(name)

# 双引号
name = "yzq"
print(name)

# 三引号
#name = ''''''
#print(name)

name = """yzq"""
print(name)

# 叠用
my_name = "hahah~'yzq'"
print(my_name)
'''

'''
# 字符串拼接 - 字符串 * 整数
name = 'yzq'
res = name * 3
print(res)
'''

'''
# 字符串的输入输出
name = input('请输入名字：')
#print('我的名字是%s' % name)
print(f'我的名字是{name}')
'''

'''
# 下标 - 索引
my_str = 'hello python'
print(my_str[0]) # h
print(my_str[-1]) # n

# len()函数，得到字符串的长度
print(len(my_str)) # 12
print(my_str[len(my_str) - 1]) # n
'''

'''
# 切片 - 获取一段数据 - 得到新的字符串
# 语法 num[start:end:step] 不包含end，左闭右开
my_str = 'hello python'
# 不写step
print(my_str[0:2]) # he

# 加step
print(my_str[1:5:2]) # el

# 不写start - 默认从索引为0开始
print(my_str[:3]) # hel

# end不写 - 可取到最后一个
print(my_str[0:]) # hello pytho

# 负数下标
print(my_str[:-1]) # hello pytho
print(my_str[-4:-1]) # tho
print(my_str[0:-1:2]) # hlopto
print(my_str[:-1] + my_str[-1]) # hello python

# 均不写
print(my_str[::]) # hello python
'''

'''
# step为负数
my_str = 'hello python'
print(my_str[2:0:-1]) # le
print(my_str[-10:-12:-1]) # le

# 字符串逆转
print(my_str[::-1]) # nohtyp olleh
'''

'''
# 字符串相关操作
# find() - 检测str是否包含在mystr中，如果是，返回开始的索引值，否则返回-1
# find(sub_start, start, end)
# sub_start：要在字符串中查找的内容，类型str
# start：开始位置，从哪里开始查找，默认为0
# end：结束的位置，查找到哪里结束，默认是len()
my_str = 'hello python and hello world'
print(my_str.find('hello')) # 0
print(my_str.find('and', 20)) # -1 从下标为20的位置找，没有找到返回-1
print(my_str.find('and', 10)) # 13 找到，返回开始索引下标

# rfind() - 反向查找
my_str = 'hello python and hello world'
print(my_str.rfind('hello')) # 17
'''

'''
# index() - 检测str是否包含在mystr中，如果是，返回开始的索引值，否则报错
# index(sub_start, start, end)
# sub_start：要在字符串中查找的内容，类型str
# start：开始位置，从哪里开始查找，默认为0
# end：结束的位置，查找到哪里结束，默认是len()
my_str = 'hello python and hello world'
print(my_str.index('hello')) # 0
print(my_str.index('and', 10)) # 13 找到，返回开始索引下标
print(my_str.index('and', 20)) # -1 没有找到，报错

# rindex() - 反向查找
print(my_str.rindex('hello')) # 17
'''

'''
# count() - 统计出现的次数
# count(sub_start, start, end)
my_str = 'hello python and hello world'
print(my_str.count('hello')) # 2
print(my_str.count('hello', 10)) # 1
print(my_str.count('hello', 10, 12)) # 0
'''

'''
# repalce() - 替换
# repalce(old_str, new_str, count)
# old_str:将要替换的字符串
# new_str:新的字符串，替换的字符串
# count:替换次数，默认全部替换
# 返回值:得到一个新字符串
my_str = 'hello python and hello world'
my_str1 = my_str.replace('hello', 'hahah~') # hahah~ python and hahah~ world
print(my_str1)

my_str2 = my_str.replace('hello', 'hahah~', 1) # hahah~ python and hello world
print(my_str2)
'''

'''
# split() - 字符串的分割
# split(sub_str, count) - 将mystr按照sub_str进行切割
# sub_str:按照什么内容切割字符串，默认为空白字符，空格，tab键
# count:切割次数，默认为全部切割
# 返回值：列表[]
my_str = 'hello python and hello world'

# 按照空白字符切割
res1 = my_str.split()
print(res1) # ['hello', 'python', 'and', 'hello', 'world']

# 按照内容切割、次数
res2 = my_str.split('llo', 1)
print(res2) # ['he', ' python and hello world']

# 反向切割rsplit()
res3 = my_str.rsplit('llo')
print(res3) # ['he', ' python and he', ' world']
'''

'''
# join() - 字符串连接,不会改变原字符串
# join(可迭代对象)
# 可迭代对象：str，列表（需要列表中的每一个数据都是字符串类型）
# 将my_str这个字符串添加到可迭代对象的两个元素之间
# 返回值：一个新的字符串
my_str = '_'.join('hello')
print(my_str) # h_e_l_l_o

# 定义列表
my_list = ['hello', 'world']
print('_'.join(my_list)) # hello_world
print(' '.join(my_list)) # hello world
'''

'''
# 其他操作
# 6.1 capitalize() - 把字符串的第一个字符大写
my_str = 'hello'
print(my_str.capitalize()) # Hello

# 6.2 title() - 把字符串的每个单词首字母大写
my_str = 'hello world'
print(my_str.title()) # Hello World

# 6.3 startswith() - 检查字符串是否是以某字符串开头, 是则返回 True，否则返回 False
my_str = 'hello world'
print(my_str.startswith('hello')) # True

# 6.4 endswith() - 检查字符串是否以某字符结束，如果是返回True,否则返回 False
my_str = 'hello world'
print(my_str.endswith('world')) # True

# 6.5 lower() - 将所有大写转为小写
my_str = 'Hello World'
print(my_str.lower()) # hello world

# 6.6 upper() - 将所有小写转为大写
my_str = 'Hello World'
print(my_str.upper()) # HELLO WORLD

# 6.7 调整输出位置
# ljust() - 返回一个原字符串左对齐,并使用空格填充至长度width的新字符串
# rjust() - 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# center() - 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print("'hello'".ljust(30))
print("'hello'".rjust(30))
print("'hello'".center(30))

# 6.8 删除空白字符
# lstrip() - 删除 mystr 左边的空白字符
# rstrip() - 删除 mystr 字符串末尾的空白字符
# strip() - 删除mystr字符串两端的空白字符
print("        'hello'".lstrip())
print("'hello'          ".rstrip())
print("   'hello'      ".strip())

# 6.9 分割
# partition() - 把mystr以str分割成三部分,str前，str和str后
# rpartition() - 从右边开始
print('hello world'.partition('lo')) # ('hel', 'lo', ' world')
print('hello world'.rpartition('or')) # ('hello w', 'or', 'ld')

# 6.10 splitlines() - 按照行分隔，返回一个包含各行作为元素的列表
print('hello world \n haha~ \n xiaoyang'.splitlines()) # ['hello world ', ' haha~ ', ' xiaoyang']
'''

'''
# 6.11 判断数字、字母、空格
# isalpha() - 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
print('hello world'.isalpha()) # False，有空格

# isdigit() - 如果 mystr 只包含数字则返回 True 否则返回 False
print('123456'.isdigit()) # True

# isalnum() - 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
print('hello world 123'.isalnum()) # False，有空格

# isspace() - 如果 mystr 中只包含空格，则返回 True，否则返回 False
print('     '.isspace()) # True
'''


