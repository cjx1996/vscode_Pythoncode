import math
#question1
class Apple:
    def __init__(self,c,w,o,p):
        '''
        创建苹果实例，初始化需要以下几个数据
        :param c :str 
        :param w :int
        :param o :str
        :param p :int
        '''
        self.color=c
        self.weight=w
        self.origin=o
        self.price=p





#question2
class Circle:
    def __init__(self,r):
        '''
        :param r:float
        '''
        self.round=r
    
    def area(self):
        return (2*math.pi*self.round)

c1=Circle(2.3)
print(c1.area())


#question3
class Triangle:
    def __init__(self,w,l):
        '''
        :param w:float
        :param l:float
        '''
        self.width=w
        self.len=l

    def area(self):
        return self.width*self.len
    

tr1=Triangle(2.4,34.2)
print(tr1.area())


#question4
class Hexagon:
    def __init__(self,sl):
        '''
        :param sl:float
        '''
        self.side_length=sl

    def cacculate_perimeter(self):
        return 6*self.side_length
    

h1=Hexagon(4.5)
print(h1.cacculate_perimeter())





















































