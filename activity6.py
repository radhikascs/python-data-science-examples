import matplotlib.pyplot as plt

labels= 'Delhi','Patna','Gwalior','Raipur'
sizes = [45,30,15,10]
explode =(0,0.1,0,0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode,labels=labels, autopct ="% 1.1f %%",shadow=True,startangle=90)
ax1.axis('equal')
plt.title("Pollution rank among cities")
plt.show()