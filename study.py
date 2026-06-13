import matplotlib.pyplot as plt
import numpy as np
import math


#Data 
Score = [1,2,3,4,5,6,7,8,9,10]
F= [1,5,7,8,9,10,11,12,13,14]
total = sum (F)
rel_freq = [x * 100 / total for x in F]

plt.bar(Score,F, color='skyblue', tick_label=Score)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Bar Chart')
# for i, v in enumerate(rel_freq):
#     plt.text(Score[i], v + 0.5, f"{v:.1f}%", ha='center', va='bottom')

plt.show()