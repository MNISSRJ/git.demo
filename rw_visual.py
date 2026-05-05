import matplotlib.pyplot as plt
 
from random_walk import RandomWalk
#使用while循环模拟多次随机漫步
while True:
# 创建一个RandomWalk实例
    rw = RandomWalk(50000)
    rw.fill_walk()
    #设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))#函数figure()指定图表的宽度，高度，分辨率，背景色，形参dpi传递分辨率
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolor='none',s=1)
    #突出起点和终点 
    plt.scatter(0,0,c='blue',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolor='none',s=100)
    #隐藏坐标轴
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running=input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
