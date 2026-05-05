#colormap
import matplotlib.pyplot as plt
x_values=list(range(1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,edgecolor='none',s=15)
#自动保存图表
plt.savefig('squares_plot.png',bbox_inches='tight')#第一个实参指定保存的文件名，第二个实参指定图像的边界框