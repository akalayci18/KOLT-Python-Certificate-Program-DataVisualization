from matplotlib import pyplot as plt
import pandas as pd


#2.4.1 Importing Data
lemon_data = pd.read_csv("ahmets_lemons.csv")

months = lemon_data['months']
visits_per_month = lemon_data['visits_per_month']
citron_lemons_per_month = lemon_data['citron_lemons_per_month']
sweet_lemons_per_month = lemon_data['sweet_lemons_per_month']
lisbon_lemons_per_month = lemon_data['lisbon_lemons_per_month']

#2.4.2 Understand the Data and Set Up Subplots
#2.4.3 Page Visits Over Time
#2.4.4 Plotting Multiple Lemon Species
#2.4.5 Labeling and Saving

#star and square commented out;however, figures included in the submitted file
plt.figure(figsize=(12, 8))

x1 = [1]
y1 = [1]

x2 = [1]
y2 = [1]


ax1 = plt.subplot (1, 2, 1)
#star
#plt.plot (x1, y1, marker = "*", markersize = 60)

x_values = (months)
y_values = (visits_per_month)

plt.plot(x_values, y_values, marker = "s")

plt.title('Visits per Month')
plt.xlabel('Months')
plt.ylabel('# of Visits')


ax2 = plt.subplot (1, 2, 2)
#square
#plt.plot (x2, y2, marker = "s", markersize = 35)

y1_values = (citron_lemons_per_month)
y2_values = (sweet_lemons_per_month)
y3_values = (lisbon_lemons_per_month)

plt.plot(x_values, y1_values, marker = "o", label = 'Citron lemons')
plt.plot(x_values, y2_values, marker = "o", label = 'Sweet lemons')
plt.plot(x_values, y3_values, marker = "o", label = 'Lisbon lemons')

plt.title('Lemon Sales per Month')
plt.xlabel('Months')
plt.ylabel('# of Lemons')

ax1.set_xticklabels(months)
ax2.set_xticklabels(months)

plt.suptitle('Ahmet\'s Lemons') 
plt.legend()
plt.savefig('project_figures.png')
plt.show()







