#Step1: Import the required libraries
import pandas as pd
import numpy as np         #for calculating percentile
import scipy.stats         #for calculating z-score

#Step2: Read data from the uploaded csv file
cars = pd.read_csv("mtcars.csv")

#Step3: Display the dataframe
print(cars)

#Step4: Calculate the percentile
print(np.percentile(cars[['mpg','disp']], 50, axis=0))     #50th percentile of mpg and disp columns

#Step5: Calculate the quartile
print(cars.iloc[:,1:].quantile(0.25))                               #1st quartile or quantile of order 0.25

#Step6: Calculate the z-score
"""
A "z-score" in statistics is a standardized measure that indicates how many standard deviations a data point is away from the mean of a distribution; essentially, 
it tells you how far a specific data point is from the average value in terms of standard deviations, 
with positive z-scores signifying values above the mean and negative z-scores indicating values below the mean.
 
"""

from scipy.stats import zscore
print(zscore(cars.mpg, axis=0))       #z-score of each element in the mpg column