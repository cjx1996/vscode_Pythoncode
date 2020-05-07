import time
import random
'''
In this chapter, we study the fundamental knowledge about structure.
'''
#stack
class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        '''
        返回是否空栈
        '''
        return self.items == []
    
    def push(self, item):
        '''入栈'''
        self.items.append(item)
    
    def pop(self):
        '''
        出栈
        '''
        return self.items.pop()
    
    def size(self):
        '''
        返回栈大小
        '''
        return len(self.items)

    def peek(self):
        '''
        返回栈顶元素
        '''
        
        if self.items == []:
            return 'This is an empty stack.'
        if self.items:
            return self.items[len(self.items)-1]

stack= Stack()

print(stack.is_empty())
print(stack.peek())


print(stack.is_empty())
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

for i in range(0,6):
    stack.push(i)
print(stack.size())
print(stack.peek())



#使用栈进行字符串逆转
sk1=Stack()
for c in 'Hello':
    sk1.push(c)

reverse = ''
for i in range(len(sk1.items)):
    reverse += sk1.pop()
print(reverse)




#queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        '''
        返回是否为空队列
        '''
        return len(self.items) == 0
    
    def enqueue(self, item):
        '''
        入队
        '''
        self.items.insert(0,item)

    def dequeue(self):
        '''
        出队
        '''
        return self.items.pop()

    def size(self):
        '''
        返回队列大小
        '''
        return len(self.items)

    #用来表示购买电影票，不是队列的固有属性
    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []
        for i in range(10):
            pq.enqueue('person' + str(i))
        
        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)
        return tix_sold
que1 = Queue()
print(que1.is_empty())

for i in range(5):
    que1.enqueue(i)

print(que1.size())

for i in range(5):
    print(que1.dequeue())

print(que1.size())




que2 = Queue()
sold = que2.simulate_line(5,1)
print(sold)












