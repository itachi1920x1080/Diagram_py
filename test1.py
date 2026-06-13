import matplotlib.pyplot as plt

# --- ទិន្នន័យសម្រាប់លំហាត់ទី ១ (Pie Chart) ---
labels_1 = ['A', 'B', 'C', 'D']
values_1 = [90, 140, 30, 20]
colors_1 = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] # កំណត់ពណ៌ឱ្យស្អាត

# --- ទិន្នន័យសម្រាប់លំហាត់ទី ២ (Bar Chart) ---
age_groups = ['15-18', '18-21', '21-24', '24-27'] # ថ្នាក់អាយុ
frequencies = [5, 15, 12, 8] # ប្រេកង់

# បង្កើតផ្ទាំងរូបភាពមួយដែលមានក្រាហ្វពីរ (1 ជួរ, 2 ជួរឈរ)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# === ក្រាហ្វទី ១៖ Pie Chart ===
ax1.pie(values_1, labels=labels_1, colors=colors_1, autopct='%1.1f%%', startangle=90)
ax1.set_title('លំហាត់ទី ១: សង់ដ្យាក្រាមរង្វង់ (Pie Chart)')

# === ក្រាហ្វទី ២៖ Bar Chart (តំណាងឱ្យប្រេកង់) ===
bars = ax2.bar(age_groups, frequencies, color='#4CAF50')
ax2.set_title('លំហាត់ទី ២: របាយប្រេកង់តាមអាយុ')
ax2.set_xlabel('អាយុ (ថ្នាក់)')
ax2.set_ylabel('ចំនួន (ប្រេកង់)')

# បន្ថែមលេខនៅលើក្បាលរបារនីមួយៗ
for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')

# បង្ហាញក្រាហ្វ
plt.tight_layout()
plt.show()