import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

car=pd.read_csv('Car_sales.csv')
print(car.head())
print(car.shape)

### 1. Line plot

#Sorting dataset by 'Sales in thousands'
car=car.sort_values('Sales in thousands')

#Plotting simple line plot to see thre trend of 'Sales in thousands'
plt.plot(car['Sales in thousands'])
plt.show()

#### We can say that *'sales in thousands'* slowly increase from 0-120 then it spikes really high

### 2. Barplot

#Mean 4-year resale value for each Manufacturer
plt.figure(figsize=(10,8)) # Creates a new figure and allows you to set different parameters like figuresize()
for group,data in car.groupby('Manufacturer'):
    plt.barh(group,data['4-year resale value'].mean())
plt.show()

#### We can see that most of the manufacturers do not have *'4-year resale value'* more than 20, only a few in the range of 20-30 while Porche has best *'4-year resale value'*.

#plotting Vehicle type Manufacturer make
vt_dict=dict()
for i in set(car['Vehicle type']):
    vt_dict[i]=car[car['Vehicle type']==i].Manufacturer.count()
plt.bar(vt_dict.keys(),vt_dict.values())
plt.show()

#### We can see that manufacturers manufacture more number of *'Passenger'* type of cars

# Mean 4-year resale value and Price in thousands for each Manufacturer
plt.figure(figsize=(10, 8))
for group, data in car.groupby('Manufacturer'):
    plt.barh(group, data['4-year resale value'].mean())
    plt.barh(group, data['Price in thousands'].mean(), left=data['4-year resale value'].mean())
plt.show()

#### From the above stacked bar graph we can conclude that almost all the Manufacturer have bad resale value except for *'Porche'* which has almost equal value.

#### The stacked bar graph is quite confusing bescause of all the random colors and it is hard to analyse it. This can be fixed using fixed colors and legends which is covered in next demo.

## 3. Histogram

car.Horsepower=car.Horsepower.fillna(car.Horsepower.mean())
plt.hist(car.Horsepower, bins=10)
plt.show()

## 4. Pie chart

m_dict=dict()
plt.figure(figsize=(10,8))

for manufacturer in set(car.Manufacturer):
    m_dict[manufacturer]=car[car.Manufacturer==manufacturer].Manufacturer.count()
plt.pie(m_dict.values(),labels=m_dict.keys())
plt.show()

#### The pie chart shows that *'Ford'* and *'Dodge'* launched more number of models while *'Jaguar'* and *'infiniti'* launched very less

## 5. Scatter Plot

plt.scatter(car['Fuel capacity'],car['Fuel efficiency'])
plt.show()

### From the above scatter plot we can see that as *'Fuel capacity'* increases the *'Fuel efficiency'* gradually decreases.

## 6. Boxplot

print(car['Curb weight'].isna().any())

car['Curb weight']=car['Curb weight'].fillna(car['Curb weight'].mean())
plt.boxplot(car['Curb weight'])
plt.show()


# Checking for any null values as boxplot will be empty if there are any  ull values
car.Wheelbase.isna().any()

car.Wheelbase=car.Wheelbase.fillna(car.Wheelbase.mean())
plt.boxplot(car.Wheelbase)
plt.show()

### We can see most of the wheelbases are around 100-110 while some being exception, that is, outliers.