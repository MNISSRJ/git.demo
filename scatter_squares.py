import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=(1,0,1),edgecolor='none',s=10)#edgecolor='none'可以删除数据点的轮廓
#(x,y,z)分别表示红绿蓝的分量
plt.axis([0,1100,0,1100000])#设置每个坐标轴的取值范围
plt.show()