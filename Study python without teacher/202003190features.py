#封装(encapsulation)
'''
1.python并没有在语法层面强制信息隐瞒。
2.python中没有私有变量。
3.python中通过命名解决该问题，如果某个方法或变量以下划线开头， 就应该知道他们不该被使用。
'''
class PublicPrivateExample:
    def __init__(self):
        self.public='safe'
        self.unsafe='unsafe'


    def public_method(self):
        #客户端可以使用
        pass

    def _unsafe_method(self):
        #客户端不应使用
        pass





#抽象(abstraction)
'''
剥离事物的诸多特征，使其只保留最基本的特质
'''


#多态(polymorphism)
'''
为不同的基础形态(数据类型)提供相关接口的能力
'''
#以print举例，不同的数据类型都可以输入得到执行
print('Hello, World!')
print(200)
print(200.1)

#以type举例
type('Hello, World!')
type(200)
type(200.1)



'''


#不要执行

#未使用多态的代码画图

shapes=[trl,sql,crl]
for a_shape in shapes:
    if  type(a_shape) =='Triangle':
        a_shape.draw_triangle()
    if type(a_shape) =='Square':
        a_shape.draw_square()
    if type(a_shape) =='Circle':
        a_shape.draw_Circle()


#使用多态的代码画图
shapes=[trl,sql,crl]
for a_shape in shapes:
    a_shape.draw()

'''


#继承(inheritance)
'''
创建类时，该类可以从另一个类那里继承方法和变量
被继承的类称为父类(parent class)
继承的类称为子类(child class)



'''


class Shape():
    def __init__(self, w, l):
        self.width= w
        self.len= l
    

    def print_size(self):
        print('''{} by {} '''.format(self.width,self.len))


my_shape= Shape(20, 25)
my_shape.print_size()


class Square(Shape):
    def area(self):
        return self.width*self.len


    #方法覆盖(method overriding)
    def print_size(self):
        print(
            '''I am {} by {}'''
            .format(self.width, self.len)
                

        )


a_square=Square(20, 20)
a_square.print_size()
print(a_square.area())



#组合(composition)
class Dog():
    def __init__(
        self,
        name,
        breed,
        owner
                ):
        self.name= name
        self.breed= breed
        self.owner= owner



class Person():
    def __init__(self, name):
        self.name= name


mick=Person('Mick Jagger')
stan=Dog('Stanley','Bulldog',mick)
print(stan.owner.name)







































































