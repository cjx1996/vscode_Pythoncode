#coding:utf8
import csv

#Test the use of readlines
with open('E:/code/vscode_Pythoncode/spider/tsxt.txt','r',encoding='utf-8') as f:
    content_list=f.readlines()
   
    for i in range(len(content_list)):
        print(content_list[i])
    f.close()


#Test the use of read
with open('E:/code/vscode_Pythoncode/spider/tsxt.txt','r',encoding='utf-8') as f:
    content_list2=f.read()
    print(len(content_list2))
    print(content_list2)
    f.close()


#test the use of write
with open('E:/code/vscode_Pythoncode/spider/tsxt.txt','a',encoding='utf-8')as f:
    content_write='\nI want to be a programmer.'
    f.write(content_write)
    f.close()
    

#Test the result of write
with open('E:/code/vscode_Pythoncode/spider/tsxt.txt','r',encoding='utf-8') as f:
    content_list2=f.read()
    print(len(content_list2))
    print(content_list2)
    f.close()





























