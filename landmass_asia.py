import matplotlib.pyplot as plt

# Data for the pie chart of land area of countries in Asia
labels = ['China', 'India', 'Indonesia', 'Pakistan', 'Bangladesh', 'Japan', 'Philippines', 'Vietnam', 'Turkmenistan', 'Other Countries']
sizes = [7.6, 3.3, 1.8, 1.5, 1.5, 0.9, 0.8, 0.6, 0.5, 18.6]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'brown', 'purple']

# Plotting the pie chart for land area of countries in Asia
plt.pie(sizes, labels=labels, colors=colors, startangle=90, counterclock=False, wedgeprops={"edgecolor":'black'})
plt.title("Land Area of Countries in Asia")

# Showing the plot
plt.show()

