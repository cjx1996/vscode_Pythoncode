'''
In this part, we study the use of string.
'''
author='Kafka'
#字符串的索引
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

#字符串的负索引
print(author[-1])

#字符串不可变，若修改，必须直接创建一个新的
ff='F.Fitzgerald'
ff='F.Scott Fitzgerald'
print(ff)

#字符串的拼接
print('cat'+'in'+'hat')

print('cat'+' in'+' the'+' hat')

#字符串乘法
print("Sawyer"*3)
print(type('Sawyer'*3))

#字符串大写
print('We hold these truthe...'.upper)

#字符串小写
print('SO IT GOES.'.lower())

#首字母大写
print('four score and...'.capitalize())


#格式化
print('William {}'.format('Faulkner'))

last='Faulkner'
print('William {}'.format(last))

author='William Faulkner'
year_born='1897'
print('{} was born in {}.'.format(author,year_born))



"""
n1=input("Enter a noun:")
v=input("Enter a verb:")
adj=input("Enter an adj:")
n2=input("Enter a noun:")
r='''The {} {} the {} {} 
    '''.format(
        n1,
        v,
        adj,
        n2
    )
print(r)

"""




#分割
print('I jumped over the puddle. It was 12 feet!'.split('.')) #分割后返回列表


#连接
first_three='abc'
resut='+'.join(first_three)

words=[
    'The',
    'fox',
    'jumped',
    'over',
    'the',
    'fence',
    '.'
]
one=' '.join(words)
print(one)                                        #将列表连接为字符串



#去除空格
s='          The      '
s=s.strip()
print(s)

#替换字符
equ='All animals are equal.'
equ=equ.replace('a','@')
print(equ)

#索引
print('animals'.index('n'))

try:
    print('animals'.index('z'))
except ValueError:
    print('Not found!')

#in关键字
print('cat' in 'cat in the hat.')

print('Bat' in 'Cat in the hat.')

print('Potter'not in 'Harry')

#字符串转义
'''
下面的错误语句：
print("She said "Surely."")
'''
print("She said \"Surely.\"")

print('She said "Surely."')
print("She said 'Surely.")

#换行符
print("line1\nline2\nline3")

#切片 slicing   (起始索引starting index   结束索引end index)
fict=[
    'Tolstoy',
    'Camus',
    'Orwell',
    'Huxley',
    'Austin'
]
print(fict[0:3])

ivan='In the place of death there was light.'
print(ivan[0:17])
print(ivan[17:33])

print(ivan[:17])
print(ivan[17:])
print(ivan[:])



























































