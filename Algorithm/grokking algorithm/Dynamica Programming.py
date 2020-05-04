'''背包问题FAQ
假设一个小偷，背着可装4磅东西的背包。
可盗窃三个商品，音响（3000$，4磅）、笔记本电脑（2000$，3磅）、吉他（1500$，1磅），
如何盗窃价值最高？'''
gitar=[1500,1]
pc=[2000,3]
audio=[3000,4]
iphone=[2000,1]

goods=[gitar,pc,audio,iphone]
#定义整个网格
cells=[]
#gitar加入可选列表
line1=[]
#pc加入可选列表
line2=[]
#audio加入可选列表
line3=[]
#iphone加入可选列表
line4=[]
#将各行加入网络
cells=[line1,line2,line3,line4]
#定义名称列表
names=['gitar','pc','audio','iphone']
def compute_the_table(weight_of_bag):
    if weight_of_bag==0:
        print("This is an empty bag!")
    elif weight_of_bag>0:
        for i in range(len(cells)):
            for j in range(weight_of_bag):
                #如果是第一行，数值全部为gitar的价值
                if i==0:
                    cells[0].append([gitar[0],'gitar'])
                #如果背包的重量小于新添商品的重量，直接等于上一行该数值
                elif j+1<goods[i][1]:
                    cells[i].append(cells[i-1][j])
                #如果背包的重量等于新添商品的重量，将两者比较，选择较大的
                elif j+1==goods[i][1]:
                    if cells[i-1][j][0]>goods[i][0]:
                        cells[i].append(cells[i-1][j])
                    else:
                        cells[i].append([goods[i][0],names[i]])
                #如果背包重量大于新添商品重量，比较上一行数值与新添商品重量加上多余重量最大价值
                elif cells[i-1][j][0]>=(goods[i][0]+cells[i-1][j-goods[i][1]][0]):
                    cells[i].append(cells[i-1][j])
                elif cells[i-1][j][0]<(goods[i][0]+cells[i-1][j-goods[i][1]][0]):
                    cells[i].append([goods[i][0]+cells[i-1][j-goods[i][1]][0]])
                    cells[i][len(cells[i])-1].append(names[i])
                    for k in range(1,len(cells[i-1][j-goods[i][1]])):
                        if k==1:
                            cells[i][len(cells[i])-1].append(' and '+cells[i-1][j-goods[i][1]][k])
                        else:
                            cells[i][len(cells[i])-1].append(cells[i-1][j-goods[i][1]][k])
    return cells

        



def What_be_choice(weight_of_bag):
    cells=compute_the_table(weight_of_bag)
    biggest_value=cells[len(names)-1][weight_of_bag-1][0]
    Be_choice=''
    for i in range(1,len(cells[len(names)-1][weight_of_bag-1])):
        Be_choice=Be_choice+cells[len(names)-1][weight_of_bag-1][i]


    print("The biggest value is:",end="")
    print(biggest_value)
    print('Choose following good:'+Be_choice)   

What_be_choice(4)










