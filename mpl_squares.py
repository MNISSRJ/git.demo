#plot()函数可以根据数字绘制出有意义的图形
import matplotlib.pyplot as plt
#使用scatter()绘制散点图并设置样式
plt.scatter(2,4,s=200)#在（2，4）出画了点用实参s设置了绘制图形时使用的点的尺寸
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.scatter(input_values,squares,s=200)
#给plot()提供输入值和默认值
plt.plot(input_values,squares,linewidth=5)#linewidth决定了plot()会知道线条的粗细
#设置图表标题，并给坐标轴加上标签
plt.title("VVVVVV",fontsize=24)#函数title()给图标指定标题，fontsize指定了文字大小
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.show()