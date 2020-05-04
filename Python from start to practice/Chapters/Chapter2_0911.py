newline='*************************************************************************************************************************'


#1、列表的使用
''' 列表的创建    '''
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1]+'\t索引-1代表最后一个元素')
message="My first bicycle was a "+bicycles[0].title()+'.'
print(message)
print(newline)


''' 列表的修改、添加、删除'''
motercycles=['honda','yamaha','suzuki']
print(motercycles)
motercycles[0]='ducati'
print(motercycles)
print(newline)


motercycles=['honda','yamaha','suzuki']
print(motercycles)
motercycles.append('ducati')
print(motercycles,end='')
print('\t\t在列表尾添加新元素')
print(newline)


motercycles=[]
motercycles.append('honda')
motercycles.append('yamaha')
motercycles.append('suzuki')
print(motercycles,end='')
print('\t\t创建空列表然后添加新元素')
print(newline)


motercycles=['honda','yamaha','suzuki']
motercycles.insert(0,'ducati')
print(motercycles,end='')
print('\t\tinsert相当于特定位置插队')
print(newline)

motercycles=['honda','yamaha','suzuki']
print(motercycles)
del motercycles[0]
print(motercycles,end='')
print('删除特定位置元素')
print(newline)

motercycles=['honda','yamaha','suzuki']
print(motercycles)
del motercycles[1]
print(motercycles,end='')
print('删除特定位置元素')
print(newline)


motercycles=['honda','yamaha','suzuki','ducati']
print(motercycles)
motercycles.remove("ducati")
print(motercycles,end='')
print('删除特定元素值')
print(newline)



motercycles=['honda','yamaha','suzuki','ducati']
print(motercycles)
too_expensive="ducati"
motercycles.remove(too_expensive)
print(motercycles,end='')
print('\nA'+too_expensive.title()+' is too expensive for me')
print('删除特定元素值后根据其变量名可继续使用')
print(newline)











































