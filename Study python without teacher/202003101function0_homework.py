#question 1
def square():
    '''
    返回输入数的平方
    ：param x :int
    :return int 
    '''
    x=input("Enter a number")
    x=int(x)
    return(x**x)
  
'''
a=square()
print(a)
'''


#question 2
def printstr(x):
    '''
    打印字符串
    ：param x:str
    '''
    print(x)

'''
x='Hello world!'
printstr(x)
'''


#question 3
def find_the_smaller(a,b):
    '''
    返回a、b中较小的值
    :param a:int
    :param b:int
    :return :int，a、b中较小值
    '''
    if a<b:
        return a
    else:
        return b

def find_the_smallest(a,b,c,d=1,e=5):
    ''' 
    返回a、b、c、d、e中的最小的数
    :param a:int
    :param b:int 
    :param c:int
    :param d:int
    :parma e:int
    :return :int,a/b/c/d/e中最小数
    '''
    f=find_the_smaller(a,b)
    f=find_the_smaller(f,c)
    f=find_the_smaller(f,d)
    f=find_the_smaller(f,e)
    return f
'''
smallest=find_the_smallest(3,2323,887)
print(smallest)
'''

#question 4
def divide2(x):
    '''
    返回x的一半
    :param x:int
    :return :float or int,x的一半
    '''
    if (x/2-int(x/2))==0:
        return int(x/2)
    else:
        return x/2

def multiply4(x):
    '''
    返回x的四倍
    ：param x：int
    : return :int ,4x
    '''
    if type(x) is int:
        return (4*x)
    else:
        print("The wrong input!")
    
'''   
a=input("Enter a number:")
a=int(a)
a=divide2(a)
a=multiply4(a)
print(a)
'''

#question 5
def str2float(x):
    '''
    将字符串转换为浮点数
    :param x:str
    :return :float,将x转换为float
    '''
    try:
        return float(x)
    except ValueError:
        print("This is a wrong input!")



'''
str1=input("Enter a string number:")
print(str2float(str1))
'''




















