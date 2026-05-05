import matplotlib.pyplot as plt
x_values=list(range(5001))
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=15)
plt.plot(x_values,y_values,c=(0.5,0.2,1),linewidth=2)
plt.title("Cube of Numbers")
plt.xlabel("Numbers")
plt.ylabel("Cube")
plt.savefig('cubed_numbers.png',bbox_inches='tight')