import pandas as pd
import matplotlib.pyplot as plt
import os




boston = pd.read_csv(filepath_or_buffer='data/housing.data', sep='\\s+', header=0)
#print(boston.to_string())
#print(boston.info())
#print(boston.describe())
#print(boston.corr().to_string())


os.makedirs('plots', exist_ok=True)

plt.hist(boston['TAX'], bins=30, color='b')
plt.title('TAX by Index')
plt.xlabel("Index")
plt.ylabel('full-value property-tax rate per $10,000')
plt.savefig(f'plots/tax_by_index.png', format='png')
plt.clf()

plt.scatter(boston['MEDV'], boston['RM'], color='g')
plt.title('Price by # of rooms')
plt.xlabel("Median value of owner-occupied homes in $1000's")
plt.ylabel('# of rooms')
plt.savefig(f'plots/cost_by_room.png', format='png')

plt.close()

