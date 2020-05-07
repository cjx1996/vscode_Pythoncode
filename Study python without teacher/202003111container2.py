#容器的高级用法
'''
容器的嵌套
'''
#列表中存储列表
lists=[]
rap=['Kanye West','Jay Z','Eminem','Nas']
rock=['Bob Dylan','The Beatles','Led Zeppelin']
djs=['Zeds Dead','Tiesto']
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)
rap.append('Kendrick Lamar')
print(rap)
print(lists)


#列表中存储元组
locations=[]

la=(34.0522,188.2437)
chicago=(41.8781,87.6298)
locations.append(la)
locations.append(chicago)
print(locations)

#元组中存储列表
eights=['Edgar Allan Poe','Charles Dickens']
nines=['Hemingway','Fitzgerald','Orwell']
authors=(eights,nines)
print(authors)

#列表中存储字典
bday={'Hemingway':'7.31.1899','Fitzgerald':'9.24.1896'}
my_list=[bday]
print(my_list)

#元组中存储字典
my_tuple=(bday,)
print(my_tuple)

#字典中存储列表和元组及字典
ny={'locations':
    (40.7128,
    74.0059),
    'celebs':
    ['W.Allen',
    'Jay Z',
    'K. Bacon'],
    'facts':
    {'state':
    'NY',
    'country':
    'America'
    }
}
print(ny)

#对集合set的一些用法

my_set=set()
my_set={'python','c++','c','java'}
my_set.add('php')
my_set.update('matlab')    #add和update都可以添加新元素，但update可以用以添加列表、元组、字典等

my_set.discard('c')
my_set.discard('c#')
my_set.pop()                #pop与diacard都可以删除，pop随机删除，diacard指定删除
my_set.clear()              #clear the set
my_set2={'html','javascript','python','basic'}

print(my_set|my_set2)      #myset与my_set2包含的所有元素，合集
print(my_set2-my_set)      #包含于my_set2，但不在my_set中的元素，差集
print(my_set^my_set2)      #不同时属于两个集合的元素，交集的补集
print(my_set2&my_set)      #同时属于两个集合的元素，交集

















































