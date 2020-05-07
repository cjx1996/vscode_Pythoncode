#question1
import os
import csv
x_path=os.path.join('e://','code','vscode_Pythoncode','平凡的世界','第一部 第一章.txt')

with open (x_path,'r',newline='',encoding='utf-8')as f:
    r=f.read()
    print(r)
    

#question2
x_q="What is your name?"
y_q="How old are you?"
'''
x_a=input(x_q)
y_a=input(y_q)
new_file=os.path.join('E://','code','vscode_Pythoncode','id.txt')
with open(new_file,'w',newline='',encoding='utf-8')as f:
    f.write(x_q+x_a)
    f.write('\n')
    f.write(y_q+y_a)
'''

#question3
film_path=os.path.join('E://','code','vscode_Pythoncode','tieba.csv')
with open(film_path,'w',newline='\n')as f:
    w=csv.writer(f,delimiter=',')
    film=[['Top Gun','Risky Business','Minority Report'],['Titanic','The Revenant','Inception'],['Training Day','Man on Fire','Flight']]
    w.writerows(film)




