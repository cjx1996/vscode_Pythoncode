import matplotlib.pyplot as plt

x_values = list(range(1,100))

y_values = [x**2 for x in x_values]
#s 参数表示点的大小  edgecolor设置数据点的轮廓颜色及有无  c 参数设置数据点的颜色
plt.scatter(x_values, y_values, s = 20, edgecolors= 'red',c = y_values, cmap= plt.cm.Blues)

#设置图标标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of Value', fontsize =14)

#设置刻度标记的大小
plt.tick_params(axis= 'both', which = 'major', labelsize = 14)

#设置每个坐标轴的取值范围
'''axis()要求提供四个参数：x和y坐标轴的最小值和最大值'''
plt.axis([0, 110, 0, 11000])









plt.savefig('vscode_Pythoncode/Python from start to practice/Chapters/Chapter15/squares_plot.png',bbox_inches = 'tight')

























