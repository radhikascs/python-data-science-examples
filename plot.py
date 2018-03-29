from matplotlib import pyplot as plt
years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10298.7, 14958.3]

#creating a line chart years will be x axis and gdp will be on y axis

plt.plot(years,gdp,color="green",marker='o',linestyle='solid')
plt.ylabel('Billions of $')
plt.show()
