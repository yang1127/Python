# 队列的简单模式实现

# 1、定义头节点
class Head(object):
    def __init__(self):
        self.left = None
        self.right = None


# 2、节点
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# 队列相关操作
class Queue(object):
    # 3、初始化
    def __init__(self):
        self.head = Head()

    # 4、插入一个节点
    def push_queue(self, value):
        nw = Node(value)
        p = self.head
        if p.right:
            # 如果队列不为空，引入tmp临时节点
            tmp = p.right
            p.right = nw
            tmp.next = nw
        else:
            # 如果队列为空，直接插入
            p.right = nw
            p.left = nw

    # 5、删除一个节点
    def pop_queue(self):
        p = self.head
        if p.left and (p.left == p.right):
            # 队列中只有一个元素
            tmp = p.left
            p.left = p.right = None  # 置为空
            return tmp.value
        elif p.left and (p.left != p.right):
            # 队列中元素不止一个
            tmp = p.left
            p.left = tmp.next
            return tmp.value
        else:
            # 队列为空
            raise LookupError('queue is empty!')

    # 6、判断是否为空
    def empty(self):
        if self.head.left:  # 节点有值即不为空
            return False
        else:
            return True

    # 7、队头元素
    def top(self):
        if self.head.left:
            return self.head.left.value
        else:
            raise LookupError('queue is empty!')




if __name__ == "__main__":
    queue = Queue()
    queue.push_queue("hello")
    queue.push_queue("xiao")
    queue.push_queue("yang")
    queue.pop_queue()
    queue.empty()
    queue.top()

    while not queue.empty():
        print(queue.pop_queue())

