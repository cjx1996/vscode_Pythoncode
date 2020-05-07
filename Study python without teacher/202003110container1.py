'''
字典dictionary   链接两个对象  键（key）和值（value）
将一个对象链接至另一个对象，称为映射（mapping）,产生一个键值对（key-value-pair）
字典是无序的

'''

#定义
my_dict=dict()
my_dict={}

fruit={'Apple':'Red','Banana':'Yellow'}

facts=dict()
#添加键-值对
facts['code']='fun'

#添加键-值对
facts['Bill']='Gates'

#添加键-值对
facts['founded']=1776

#查找键对应的值
print(facts['Bill'])

#查找键对应的值
print(facts['founded'])





bill=dict({"Bill Gates":'charitable'})
print('Bill Gates' in bill)

print('Bill Doors' not in bill)

books={'Dracula':'Stoker','1984':'Orwell','The Trial':'Kafka'}
print(books)

del books['The Trial']
print(books)

rhymes={'1':'fun','2':'blue','3':'me','4':'floor','5':'live'}
n=input('Type a number:')
if n in rhymes:
    print(rhymes[n])
else:
    print("Not found.")












