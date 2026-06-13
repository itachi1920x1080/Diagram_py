import matplotlib.pyplot as plt

# ទិន្នន័យ
Typeofshoes = ['NIke','Adidas','Reebok','Asics','Other']
values = [250,150,100,200,300]

# បង្កើត Piecchart
plt.pie(values, 
        labels=Typeofshoes, 
        autopct='%1.1f%%',
        startangle=90)

plt.title('Piecchart of Type of Shoes Sold')
plt.axis('equal')  # ធ្វើឱ្យ Piecchart ជារង្វត
plt.show()