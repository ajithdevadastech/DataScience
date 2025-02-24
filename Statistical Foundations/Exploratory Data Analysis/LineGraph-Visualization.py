#Step1: Import the required library
import matplotlib.pyplot as plt

#Step2: Enter the data
year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_china = [667.07, 818.32, 981.24, 1135.20, 1262.60, 1337.70]
pop_india = [449.48, 553.58, 696.78, 870.13, 1053.10, 1231.00]
pop_usa = [180.67, 205.05, 227.23, 249.62, 282.162, 309.34]

#This is the population data (in millions) sourced from <b>Google Public Data</b>.

#Step3: Plot the data points on the line graph
plt.plot(year, pop_china, color='y')                           #(x,y)
plt.plot(year, pop_india, color='g')
plt.plot(year, pop_usa, color='b')
plt.xlabel('Countries')                                       #Add labels and title to the plot
plt.ylabel('Population in million')
plt.title('China-India-America Population till 2010')
plt.show()

