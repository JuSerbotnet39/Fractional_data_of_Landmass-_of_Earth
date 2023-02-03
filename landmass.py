import matplotlib.pyplot as plt

# Data for the pie chart of land area of continents
labels = ['Asia', 'Africa', 'North America',
          'South America', 'Antarctica', 'Europe', 'Australia']
sizes = [44, 30, 24, 17, 13, 7, 5]
colors = ['yellowgreen', 'gold', 'lightcoral',
          'lightskyblue', 'red', 'purple', 'orange']

# Plotting the pie chart for land area of continents
plt.subplot(1, 2, 1)
plt.pie(sizes, labels=labels, colors=colors, startangle=90,
        shadow=True, explode=(0, 0, 0, 0, 0, 0, 0.1), autopct='%1.1f%%')
plt.title("Land Area of Continents")

# Data for the pie chart of surface area of ocean and land
labels = ['Ocean', 'Land']
sizes = [71, 29]
colors = ['blue', 'brown']

# Plotting the pie chart for surface area of ocean and land
plt.subplot(1, 2, 2)
plt.pie(sizes, labels=labels, colors=colors, startangle=90,
        shadow=True, explode=(0, 0.1), autopct='%1.1f%%')
plt.title("Surface Area of Ocean and Land")

# Showing the plots
plt.show()
