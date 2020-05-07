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
#question1
sk1= Stack()
for c in 'yesterday':
    sk1.push(c)
str1 =''
for c in range(sk1.size()):
    str1+=sk1.pop()
print(str1)



#question2
sk2= Stack()
ls1=[1,2,3,4,5]
for item in ls1:
    sk2.push(item)
for i in range(sk2.size()):
    ls1[i]=sk2.pop()
print(ls1)






















