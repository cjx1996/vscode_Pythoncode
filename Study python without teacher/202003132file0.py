import os
x_path=os.path.join('E:\\','code','vscode_Pythoncode','test2.txt')

#使用open()函数打开文件，就必须使用close()关闭文件
st=open(x_path,'r')
st.close()


#使用with自动关闭文件
with open(x_path,'w') as f:
    f.write('Hi from Python!')

#读取文件
with open(x_path,'r')as f:
    print(f.read())

'''
没有关闭又重新打开文件的情况下，只能调用文件对象的read方法一次
如果后续需要，应该将文件内容保存 在一个变量或容器中
'''
my_list=list()
with open(x_path,'r') as f:
    my_list.append(f.read())
print(my_list)



'''
处理csv文件
相关术语：
csv    逗号分割值
delimiter   分隔符     ,|
'''
import csv

#写入文件
csv_path=os.path.join('e://','code','vscode_Pythoncode','tieba.csv')
with open(csv_path,'w',newline='\n') as f:      #此处需要注意newline参数的设置，如果缺省，每两行之间将会出现空行
    w=csv.writer(f,delimiter=',')
    w.writerow(['one','two','three'])
    w.writerow(['four','five','six'])


#读取文件
with open(csv_path,'r',newline='')as f:
    r=csv.reader(f,delimiter=',')
    for row in r:
        print(','.join(row))












