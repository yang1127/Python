'''
# 文件：可以永久保存数据
# 文件在硬盘中存储的格式是二进制
# 操作步骤：打开文件、读写文件、关闭文件

# 1、打开文件：文件从磁盘中存到内存中
# open(file, mode='r', encoding=None)
# file：要操作的文件名字 - 字符串
# mode：文件打开的方式 - r只读、r只写、a追加打开
# encoding：文件的编码格式，常见的编码格式有两种，一种为gbk、一种为utf-8
# 返回值，文件对象

# 以只读的方式打开当前目录中的。test.txt 文件，文件不存在会报错
f = open('test.txt', 'r')

# 2、读文件  文件对象.read()
buf = f.read()
print(buf)

# 3、关闭文件  文件.close()  将内存中的三大文件同步到硬盘中
f.close()
'''

'''
# 1、打开文件，文件不存在则创建、文件存在则覆盖
f = open('xiaoyang.txt', 'w', encoding='utf-8')

# 2、写入：windows默认是gbk，pycharm默认为utf-8，需统一处理为一种编码
f.write('hello xiaoyang\n')
f.write('hello yzq\n')
f.write('小杨吖～～\n')

# 再读
f = open('xiaoyang.txt', 'r')
buf = f.read()
print(buf)

# 3、关闭
f.close()
'''

'''
# 追加打开，在文件末尾写入内容
f = open('xiaoyang.txt', 'a', encoding='utf-8')
f.write('杨芝琪\n')

f = open('xiaoyang.txt', 'r')
buf = f.read()
print(buf)

f.close()
'''

'''
# 1、打开文件
f = open('xiaoyang.txt', 'r', encoding='utf-8')

# 2、读写文件 文件对象.read(n) n 一次读取多少字节的内容
buf = f.read(10)
print(buf) # hello xiao

# 3、关闭文件
f.close()
c
'''

'''
# 1、打开文件
f = open('xiaoyang.txt', 'r', encoding='utf-8')

# 2、读写文件
# 文件对象.readline() 一次读取一行内容，返回值为str
# 文件对象.readlines() 一次读取所有行，返回值为列表，列表中的每一项是一个字符串

buf = f.readline()
# buf = f.readlines()
print(buf) 

# 3、关闭文件
f.close()
'''

'''
# 模拟读取大文件
# 有规律的文件
f = open('test1.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf: # if len(buf) > 0, 容器可以直接作为判断条件，容器有内容，为True
        print(buf, end='')
    else:
        # 文件读完
        break
f.close()

# 无规律文件
f = open('test2.txt', 'r', encoding='utf-8')
while True:
    buf = f.read(4)
    if buf: # if len(buf) > 0, 容器可以直接作为判断条件，容器有内容，为True
        print(buf, end='')
    else:
        # 文件读完
        break
f.close()
'''

'''
# 二进制文件操作
# encode() 转为二进制
f = open('test3.txt', 'wb')
f.write('你好'.encode())
f.close()


f1 = open('test3.txt', 'rb')
buf = f1.read()
print(buf)  # 二进制
print(buf.decode()) # 转为字符串
f1.close()
'''

'''
# open() 完整语法格式
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 参数说明
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符
'''

'''
file 对象：file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：


1、file.close() 关闭文件。关闭后文件不能再进行读写操作。

2、file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3、file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4、file.isatty() 如果文件连接到一个终端设备返回 True，否则返回 False。

5、file.next() 返回文件下一行。Python 3 中的 File 对象不支持 next() 方法。

6、file.read([size]) 从文件读取指定的字节数，如果未给定或为负则读取所有。

7、file.readline([size]) 读取整行，包括 "\n" 字符。

8、file.readlines([sizeint]) 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

9、file.seek(offset[, whence]) 移动文件读取指针到指定位置

10、file.tell() 返回文件当前位置。

11、file.truncate([size]) 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。

12、file.write(str) 将字符串写入文件，返回的是写入的字符长度。

13、file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用
# 所以，为了保证无论是否出错都能正确地关闭文件，可以使用try ... finally来实现
# 但是每次都try ... finally写太繁琐，所以，Python引入了with语句来自动调用close()方法：

with open('test.txt', 'r') as f:
    print(f.read())














