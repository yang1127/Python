# 统计字符出现的个数
my_str = "hello world"
my_dict = {}
for i in my_str:
    if i == ' ':
        continue
    my_dict[i] = my_str.count(i)

print(my_dict)


