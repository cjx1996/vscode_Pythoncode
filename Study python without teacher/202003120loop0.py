'''
In this file ,we will study the use of loop which is usually used in the period of programm.
'''


#for loop    iterating


 #遍历字符串
name='Ted'                 
for character in name:
    print(character)

#遍历列表
shows=['GOT','Narcos','Vice']       
for show in shows:
    print(show)

#遍历元组
coms=('A. Development',             
      'Friends',
      'Always Sunny'
        )
for show in coms:
    print(show)

#遍历字典中的key
people={                            
        'G. Bluth II':
        'A. Development',
        'Barney':
        'HIMYM',
        'Dennis':
        'Always Sunny'
}
for character in people:
    print(character)

#使用索引变量（index variable）跟踪元素
tv=[               
    'GOT',
    'Narcos',
    'Vice'
]
i=0
for show in tv:
    tv[i]=tv[i].upper()
    i+=1
print(tv)

#使用enumerate函数进行索引与迭代
tv=[                        
    'GOT',
    'Narcos',
    'Vice'
]
for i,show in enumerate(tv):
    tv[i]=tv[i].upper()
print(tv)


#在可变迭代对象间传递数据
tv=['GOT','Narcos','Vice']
coms=['Arrested Development','friends','Always Sunny']
all_shows=[]
for show in tv:
    show=show.upper()
    all_shows.append(show)
for show in coms:
    show=show.upper()
    all_shows.append(show)
print(all_shows)


#range函数
for i in range(1,11):
    print(i)

#while循环
x=10
while x>0:
    print('{}'.format(x))
    x-=1
print("Happy New Year!")

#定义死循环
'''
while  True:
    print('Hello World!')
'''

#break语句
for i in range(0,100):
    print(i)
    break

#break与while结合
qs=[
    "What is your name?",
    'What is your fav.color?',
    "What is your quest?"
]
n=0
'''
while True:
    print("Type q to quit")
    a=input(qs[n])
    if a=="q":
        break
    n=(n+1)%3
'''


#continue语句 遇到continue终止当前迭代，并进入下一次迭代
'''for循环加上continue语句'''
for i in range(1,6):
    if i==3:
        continue
    print(i)

'''while循环加上continue语句'''
i=1
while i<=5:
    if i==3:
        i +=1
        continue
    print(i)
    i+=1


#嵌套循环 out loop 及inner loop
for i in range(1,3):
    print(i)
    for letter in ['a','b','C']:
        print(letter)


list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]
for i in list1:
    for j in list2:
        added.append(i+j)
    
print(added)


#while与for嵌套
'''
while input('y or n?')!='n':
    for i in range(1,6):
        print(i)
'''






