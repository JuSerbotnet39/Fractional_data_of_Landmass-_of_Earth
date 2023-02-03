import matplotlib.pyplot as plt

# List of countries in Europe and their landmass percentage
countries = ['Russia', 'Norway', 'Sweden', 'Finland', 'France', 'Spain', 'Germany', 'Italy', 'Poland', 'Other countries']
percentages = [45, 5, 4, 3, 9, 8, 7, 7, 6, 10]

# Plotting the pie chart
plt.pie(percentages, labels=countries, startangle=90, shadow=True, explode=(0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0), autopct='%1.1f%%')

# Adding title and labels
plt.title("Landmass Percentage of Countries in Europe")
plt.legend(countries, loc='best')

# Showing the pie chart
plt.axis('equal')
plt.show()
