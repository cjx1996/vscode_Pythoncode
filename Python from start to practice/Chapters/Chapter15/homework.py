import matplotlib.pyplot as plt



#question  15-1
def draw_cubic(length):
    '''
    :param length, int  the length of x_label
    :return a figure 
    '''
    x_values =list(range(1,length+1))
    y_values = [x**3 for x in x_values]
    plt.figure()
    plt.scatter(x_values, y_values, edgecolor = 'red', c= y_values,cmap= plt.cm.Blues)
    plt.title('Cubic Nubers', fontsize = 24)
    plt.xlabel('Value', fontsize = 14)
    plt.ylabel('Cubic of Value', fontsize = 14)
   # plt.axis([0,int((length+1)/10+1)*10,0,(int((length+1)/10)+1)**3+100])
 
    plt.show()

draw_cubic(5)
draw_cubic(5000)














