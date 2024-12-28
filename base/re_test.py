#!/usr/bin/python

import re
'''
# 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())  # (0, 3)

# 不在起始位置匹配
print(re.match('com', 'www.run oob.com'))  # None

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

# group() 匹配
if matchObj:
    print("matchObj.group() : ", matchObj.group())  # Cats are smarter than dogs
    print("matchObj.group(1) : ", matchObj.group(1))  # Cats
    print("matchObj.group(2) : ", matchObj.group(2))  # smarter
else:
    print("No match!!")

# re.search()
# 在起始位置匹配
print(re.search('www', 'www.runoob.com').span())  # (0, 3)

# 不在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # (11, 14)


phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)  # 2004-959-559

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)  # 2004959559

# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))  # A46G8HFD1134
'''

result1 = re.findall(r'\d+', 'runoob 123 google 456')

pattern = re.compile(r'\d+')  # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
print(result3)