import matplotlib.pyplot as plt

# ទិន្នន័យ (Data)
frequencies = [20, 15, 10, 5]
edges = [-0.5, 4.5, 9.5, 14.5, 19.5] # ព្រំដែនថ្នាក់ (សម្រាប់គណនាទទឹង)
midpoints = [2, 7, 12, 17] # ចំណុចកណ្តាល

# បង្កើត Histogram
plt.figure(figsize=(8, 6))
plt.bar(midpoints, frequencies, width=5, edgecolor='black', color='skyblue', alpha=0.7, label='Histogram')

# --- បន្ថែម៖ បង្ហាញចំណុចកណ្តាល (Midpoints) ---
# គូរចំណុចពណ៌ក្រហមនៅកំពូលសសរ
plt.plot(midpoints, frequencies, color='red', marker='o', linestyle='-', linewidth=2, label='Frequency Polygon')

# កំណត់ចំណុចលើអ័ក្ស (Ticks) ឱ្យបង្ហាញ Midpoints
plt.xticks(midpoints) 
plt.yticks(range(0, 22, 2))

# ដាក់ឈ្មោះ
plt.xlabel('Midpoints (Number of Bottles)')
plt.ylabel('Number of Customers (Frequency)')
plt.title('Histogram with Midpoints shown')
plt.legend() # បង្ហាញឈ្មោះ (Legend)

# បង្ហាញ
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()