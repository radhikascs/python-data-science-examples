import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and the slices will represent the cities
labels = 'Delhi', 'Patna', 'Gwalior', 'Raipur'
sizes = [45, 30, 15, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Top polluted cities")
plt.show()