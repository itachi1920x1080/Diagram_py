import matplotlib.pyplot as plt

# ទិន្នន័យ
name = ['VCD','CD']
moth = ['Jan','Feb','Mar','Apr']
vlaues_vcd = [350,310,360,200]
vlaues_cd = [300,2400,280,400]

plt.bar(moth,vlaues_vcd, color='blue', width=0.5, label='VCD', align='center')
plt.bar(moth,vlaues_cd, color='orange', width=0.5, label='CD', align='edge')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Values')
plt.title('Bar Chart VCD and CD')
plt.show()