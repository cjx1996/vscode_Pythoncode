#深入面向对象编程


'''
pyton中的每个类，都是type类的一个实例对象
'''

class Square:
    pass
print(Square)


'''
类中有两种类型的变量：
类变量(class variable)
实例变量(instance variable)
'''
class Rectangle():
    recs = []



    def __init__(self, w, l):
        self.width= w
        self.len= l
        self.recs.append((self.width,self.len))



    def print_size(self):
        print('{} by {}'
        .format(self.width,self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()



'''
类变量属于python为每个类定义创建的对象以及类本身创建的对象
类变量必须在类内部定义
类变量可以在不使用全局变量的情况下，在类的所有实例之间共享数据
'''
r1=Rectangle(10, 24)
r2=Rectangle(20, 40)
r3=Rectangle(100, 200)
print(Rectangle.recs)


#魔方方法
class Lion():
    def __init__(self, name):
        self.name= name



'''
    #可以尝试激活该段代码的运行结果
    def __repr__(self):
        return self.name
'''



lion=Lion('Dilbert')
print(lion)

class AlwaysPositive:
    def __init__(self,number):
        self.n = number
    def __sub__(self,other):
        return (self.n-other.n)

    def __add__(self, other):
        return (self.n + other.n)

x=AlwaysPositive(-20)
y=AlwaysPositive(10)
print(x+y)
print(x-y)


#is关键字
class Person:
    def __init__(self):
        self.name= 'Bob'
    

bob= Person()
same_bob= bob
print(bob is same_bob)


another_bob= Person()
print(bob is another_bob)


x=10
if x is None:
    print('x is None:(')
else:
    print('x is not None.')

x=None
if x is None:
    print('x is None.')
else:
    print('x is not None:(')













