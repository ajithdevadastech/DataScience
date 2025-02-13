#Importing Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Reading Dataset
car=pd.read_csv('Car_sales.csv')
print(car.head())
print(car.shape)

# Number of vehicle types in the dataset
print(set(car['Vehicle type']))

### 1. Line plot

# Number of vehicle types in the dataset
print(set(car['Vehicle type']))

#Plotting 'sales in thousands' for different vehicle types
vt_car=car[car['Vehicle type']=='Car']['Sales in thousands']
vt_passenger=car[car['Vehicle type']=='Passenger']['Sales in thousands']
plt.plot(np.arange(len(vt_car)),vt_car,linestyle='--',label='Car') # Dashed line
plt.plot(np.arange(len(vt_passenger)),vt_passenger,linestyle='-.', label='Passenger') # dash-dot line
plt.ylabel('Sales')
plt.title('Sales in thousands for different vehicle types')
plt.xlabel('Model')
plt.xticks(np.arange(0,150,10))
plt.yticks(np.arange(0,600,50))
plt.legend(['Car','Passenger'])
plt.show()

#### The above graph shows that vehicle type *'Car'* is more expensive than *'Passenger'* type. Graph also shows that there are more number of *'Passenger'* type models.

### 2. Barplot

# Mean 4-year resale value and price in thousands for each manufacturer
plt.figure(figsize=(10,8))
for group,data in car.groupby('Manufacturer'):
    plt.barh(group,data['4-year resale value'].mean(),color='b')
    plt.barh(group,data['Price in thousands'].mean(),left=data['4-year resale value'].mean(),color='c')
plt.title('Mean 4-year resale value and price in thousands for each Manufacturer')
plt.xlabel('Price')
plt.ylabel('Manufacturer')
plt.legend(['4-year resale value','Price in thousands'])
plt.show()


#### From the above stacked bar graph we can conclude that almost all the Manufacturer have bad resale value except for *'Porche'* which has almost equal value.


## 3. Pie chart

#Matplotlib also provides colormaps which can be checked using colormaps() function
cmap = plt.get_cmap('Spectral')
#Generating list of colors from colormap
clist = [cmap(i) for i in np.linspace(0,1,len(set(car.Manufacturer)))]

m_dict=dict()
plt.figure(figsize=(10,8))
for manufacturer in set(car.Manufacturer):
    m_dict[manufacturer]=car[car.Manufacturer==manufacturer].Manufacturer.count()
plt.pie(m_dict.values(),labels=m_dict.keys(),colors=clist)
plt.show()

#### The pie chart shows that *'Ford'* and *'Dodge'* launched more number of models while *'Jaguar'* and *'infiniti'* launched very less

## 4. Scatter Plot

plt.scatter(car['Fuel capacity'],car['Fuel efficiency'],marker='^')
plt.show()

#### From the above scatter plot we can see that as *'Fuel capacity'* increases the *'Fuel efficiency'* gradually decreases.
