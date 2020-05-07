
#函数复用例1
def even_odd(x):
    if x%2==0:
        print("even")
    else:
        print("odd")


even_odd(2)
even_odd(3)


#函数复用例2

def even_odd1():   #此处由于python是预编译函数，所以python中不存在函数重载问题
    n=input("type a numbe:")
    n=int(n)
    if n%2 == 0:
        print("n is even.")
    else:
        print("n is odd.")


#函数可选参数示例     required parameter   and   optional parameter
def f(x=2):
    return x**x


print(f())
print(f(4))



def add_it(x,y=10):
    return x+y
result=add_it(2)
print(result)


#函数作用域示例   scope    global scope    local scope
x=1
y=2
z=3
def g():
    print(x)
    print(y)
    print(z)
g()

#局部作用域中使用写全局变量会怎么样
x=100
y=200
def t():
    global x      #在局部作用域中读全局变量，直接读即可，但如果需要写，需要申明global关键字
    x+=1
    z=y+1
    print(z)
    print(x)
t()


#input函数的异常处理      exception handling   使用异常处理关键字try   except
def KelvinToFahrenheit(Temperature):
    assert(Temperature>=0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32
'''print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))'''


#不要在except中使用try语句定义的变量，因为异常可能是在变量定义之前发生的
try:
    a=input("type a number:")
    b=input("type another:")
    a=int(a)
    b=int(b)
    print(a/b)
except  (ZeroDivisionError,ValueError) :
    print("Invalid input.")



#在函数顶部留下注释解释每个参数应该为何种类型。这些注释称为"文档字符串"（docstring）
def add(x,y):
    """
    返回x+y的值
    ：param x: int.
    : param y: int.
    : return: int, x 与 y 之和
    """
    return x+y
   
















