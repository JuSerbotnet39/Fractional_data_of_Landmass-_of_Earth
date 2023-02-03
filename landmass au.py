import matplotlib.pyplot as plt

labels = ['Australia', 'Papua New Guinea', 'Indonesia', 'Timor-Leste']
sizes = [89.9, 6.5, 2.5, 1.1]
colors = ['red', 'yellow', 'green', 'blue']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')

plt.axis('equal')
plt.title("Australia Landmass Percentage")
plt.show()
