# 简单实现栈

class Stack(object):
    # 1、构造函数，空栈
    def __init__(self):
        self.my_stack = []

    # 2、判断是否为空
    def is_empty(self):
        return self.my_stack == []

    # 3、插入
    def push(self, ms):
        self.my_stack.append(ms)

    # 4、删除
    def pop(self):
        # return self.my_stack.pop()
        if self.my_stack:
            return self.my_stack.pop()
        else:
            print("stack is empty!")

    # 5、栈顶元素
    def peek(self):
        # return self.my_stack[len(self.my_stack) - 1]
        return self.my_stack[-1]

    # 6、栈大小
    def size(self):
        return len(self.my_stack)

    def print(self):
        for i in self.my_stack:
            print(i)


if __name__ == "__main__":
    stack = Stack()
    stack.push("hello")
    stack.push("xiao")
    stack.push("yang")
    stack.print()
    stack.peek()
    print(f'栈顶元素: {stack.peek()}')
    stack.size()
    print(f'栈大小: {stack.size()}')
    stack.pop()

