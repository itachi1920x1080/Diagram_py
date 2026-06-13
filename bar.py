import matplotlib.pyplot as plt


values= [14,11,16,16,16]
year = [0,5,10,15,20]
name = ['A','B','C','D','E']
colors = ['red', 'green', 'blue', 'orange', 'purple'] 


plt.bar(year,values, color=colors, tick_label=name)
# plt.xticks(year, name)
plt.xlabel('Values')
plt.ylabel('Year')
plt.title('Bar Chart')
plt.show()