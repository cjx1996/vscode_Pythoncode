names=['Chenyanxi','Wangxiang','Qingjiakun','Wangqi','Wangpu']
newname=input("The name you wang to add:")
name=names.append(newname)
for i in range(0,len(names)):
    print('Hello '+names[i]+',how are you today?')