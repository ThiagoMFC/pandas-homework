import pandas as pd

insurance = pd.read_csv(filepath_or_buffer='data/insurance.csv', sep=',', header=0)

##2
#print(insurance.to_string())
#print(insurance.columns)
#print(insurance.index) #no index
#print(insurance.dtypes)
#print(insurance.info())
#print(insurance.describe())

##3
#print(insurance['age'])

##4
#print(insurance[['age', 'children', 'charges']])

##5
#print(insurance.head(5)[['age', 'children', 'charges']])

##6
#print(insurance['charges'].min())
#print(insurance['charges'].mean())
#print(insurance['charges'].max())

##7
#line = (insurance[(insurance['charges'] == 10797.3362)])
#print(line[['age', 'sex', 'smoker']])

##8
#max_charge = insurance['charges'].max()
#line = (insurance[(insurance['charges'] == max_charge)])
#print(line['age'])

##9
#print(insurance['region'].value_counts())

##10
#print(insurance['children'].sum())

##11
#the older the person the higher the charges
#the higher the bmi the higher the charges
#the more children the higher the charges

##12
#print(insurance.corr().to_string())