#Step1: Import the required library

import pandas as pd
import statistics

#Step2: Read data from the uploaded csv file
cars = pd.read_csv("mtcars.csv", index_col=False)

#Step3: Display the dataframe
print(cars)

print(cars['mpg'].dtype)

print(cars.dtypes)

#Step4: Calculate the mean
print(cars.iloc[:,1:].mean())   #mean of all columns using pandas. skipped the first column using iloc

print(cars['cyl'].mean())           #mean of a given column using pandas

from statistics import mean
print(mean(cars["vs"]))              #mean of a given column using pandas

#Step5: Calculate the median
print(cars.iloc[:,1:].median())             #median of all columns using pandas

#Step6: Calculate the mode
print(cars.mode())

cars1 = cars.drop('model', axis=1)
print(cars1.head())

print(cars1.mode())

print(cars1['disp'].mode())           #mode of a given column using pandas

print(cars1['hp'].mode())           #mode of a given column using pandas

print(cars.describe())



