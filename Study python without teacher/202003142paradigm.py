'''
不同编程范式根本区别，就是对状态（state）的处理。全局状态（global state）
过程式编程（procedural programming）
函数式编程（functional programming）
面向对象编程（object-oriented）    类（class）
前面已经讨论过前两种了，本部分主要讨论面向对象编程。
'''
class Orange:
    def __init__(self,w,c):       #下划线包围的方法，被称为魔法方法(magic method)，即Python用于创建对象等特殊用途的方法
        '''
        重量的单位是盎司
        '''

        self.weight=w
        self.color=c
        self.mold=0
        print('Created!')

    def rot(self,days,temp):
        self.mold=days*temp    
#创建新对象的过程，被称为创建类的实例
or1=Orange(10,'dark orange')
print(or1)
print(or1.color)

#修改创建好的对象的参数
or1.weight=100
or1.color='light orange'
print(or1.color)
print(or1.weight)


#创建多个对象
or1=Orange(4,'light orange')
or2=Orange(8,'dark orange')
or3=Orange(14,'yellow')



#给对象添加腐烂属性以及处理该属性的方法(method)
or4=Orange(6,'orange')
print(or4.mold)
or4.rot(10,98)
print(or4.mold)





#定义一个关于长方形的类
class Rectangle():
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def area(self):
        return self.width*self.len

    def change_size(self,w,l):
        self.width=w
        self.len=l

rectangle=Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())

















































