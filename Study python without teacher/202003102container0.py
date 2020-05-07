'''
In this file,we will learn the use of containers,which contain list、tuple and dictionary.
Of course,we will learn the use of method only can be use in  objects.
'''

#这是对列表list一些method的尝试使用
'''定义'''
a=list()
a=[1,2,3,4]
a=[]
a=[1,2,3,4]

colors=['blue','green','yellow']
colors1=['blue','green','yellow']
colors2=['orange','pink','black']
colors3=colors1+colors2
if 'green' in colors:
    print("'green' is in colors!")
    
if "black" not in colors:
    print("'black' is not in colors!")

print(len(colors3))

guess=input("Guess a color:")
if guess in colors3:
    print("You guessed correctly!")
else:
    print("Wrong!Try again.")


#下面是对元组tuple的一些method的使用
'''定义'''
a=tuple()
a=()

'''一些method的使用'''
a=(9)
b=('9')
c=('9',)   #type(a) is int;type(b) is str ;type(c) is tuple

dys=['1984','Brave New World','Fahrenheit 451']
print(dys[2])

print('1984' in dys)

print('Handmaid' not in dys)




































































































































































































